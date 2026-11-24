#!/usr/bin/env python3
"""Check your own JPEG or PNG files with c2patool and build a local viewer page for them.

For each file, this runs c2patool twice, offline, inside a macOS sandbox that denies all network access. It uses the
sandbox profile, the offline settings file and the report summary of the actual-C2PA runner
(actual_c2pa/run_actual_c2pa.py):
  - policy A: no trust anchors;
  - policy B: the C2PA TEST trust anchors from the sample/ folder of the c2patool release. This is never production
    trust.
It then writes one self-contained HTML page: src/template.html with the results and the checked files embedded. The
page runs no validation and loads nothing from the network. Nothing is uploaded anywhere.

Needs macOS (for sandbox-exec), Python 3 (standard library only) and the extracted c2patool 0.27.23 release folder
(the folder that holds the c2patool binary and its sample/ folder). The checker refuses other files: the page's
explanations were checked against this release only.

Usage, from the repository root:
  python3 -I -B viewer/src/check_files.py --c2patool-dir DIR --out REPORT.html FILE [FILE ...]
"""

import argparse
import base64
import datetime
import hashlib
import json
import os
import platform
import struct
import subprocess
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(SRC))
sys.path.insert(0, SRC)
sys.path.insert(0, os.path.join(REPO, "actual_c2pa"))
from derived_facts import claims_from_report, derive  # noqa: E402
import run_actual_c2pa as rac  # noqa: E402

SANDBOX_EXEC = "/usr/bin/sandbox-exec"
TEMPLATE = os.path.join(SRC, "template.html")
PLACEHOLDER = "/*__EVIDENCE_DATA__*/null"
MAX_BYTES = 25 * 1024 * 1024
POLICIES = ("no_trust_anchors", "test_trust_anchors")
# The c2patool release this checker is tested with. The binary's SHA-256 is the one the actual-C2PA runner recorded in
# results/actual_c2pa/actual_c2pa_results.json; trust_anchors.pem holds two self-signed C2PA Test Root CA
# certificates marked FOR TESTING ONLY. The page's statements hold for these exact files, so other files are refused.
TESTED_RELEASE = {
    "name": "c2patool 0.27.23 (c2patool-v0.27.23-universal-apple-darwin.zip)",
    "sha256": {
        "c2patool": "e16692d25664b8c5a192bb2d8a784a500fd745701577f33c85e49a555941f8e7",
        "sample/trust_anchors.pem": "a800641aeb9d04c603ba4d20ef676a3da2c243ab8267318356737f7afb189fcf",
        "sample/store.cfg": "472aae5c0cd22412bb8b44a98b20e923be1b3a08a3a7c260410d12b4c8153d27",
    },
}
POLICY_TEXT = {
    "no_trust_anchors": {
        "name": "Policy A: no trust anchors",
        "summary": "c2patool was given no trust list. It still checks the manifest, the binding and the signature, but "
                   "any signer is reported as untrusted (signingCredential.untrusted).",
    },
    "test_trust_anchors": {
        "name": "Policy B: C2PA test anchors",
        "summary": "c2patool was given the test trust anchors that ship with c2patool 0.27.23 (sample/trust_anchors.pem "
                   "and sample/store.cfg). A signer that chains to them is reported as \"Trusted\". These are public "
                   "C2PA test roots, and the matching test private key ships in the same release, so anyone can produce "
                   "a \"Trusted\" result under this policy. It is not production trust.",
    },
}


class Refusal(Exception):
    """A reason not to check the files, reported without a traceback. No page is written, except that a page whose
    writing fails partway is left in place, and the message says so."""


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def sha256_file(path):
    return sha256_bytes(read_bytes(path))


def jpeg_size(data):
    """(width, height) from the first start-of-frame marker of a JPEG."""
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker == 0xFF:
            i += 1
            continue
        if marker in (0x01, 0xD8) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg_len = struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            height, width = struct.unpack(">HH", data[i + 5:i + 9])
            return width, height
        i += 2 + seg_len
    return None, None


def image_kind(data):
    """(format, MIME type, width, height) for PNG or JPEG bytes; None for anything else."""
    if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR" and len(data) >= 24:
        width, height = struct.unpack(">II", data[16:24])
        return "PNG", "image/png", width, height
    if data[:3] == b"\xff\xd8\xff":
        width, height = jpeg_size(data)
        return "JPEG", "image/jpeg", width, height
    return None


def printable(text):
    """Text that can always be printed and stored as UTF-8: characters that are not valid there become U+FFFD."""
    return text.encode("utf-8", "surrogatepass").decode("utf-8", "replace")


def sanitizer(pairs):
    """Replace local folder paths with placeholders wherever they appear, longest path first.

    A folder directly under the root, such as /tmp, is too short and too common to replace safely, so it is left as
    it is.
    """
    expanded = set()
    for path, label in pairs:
        for p in (path, os.path.realpath(path)):
            if p and p.strip(os.sep).count(os.sep) >= 1:
                expanded.add((p, label))
    ordered = sorted(expanded, key=lambda x: -len(x[0]))

    def sanitize(text):
        for p, label in ordered:
            text = text.replace(p, label)
        return text
    return sanitize


def run_c2patool(tool, args, cwd):
    """Run c2patool offline in the network-denied sandbox. Returns (command, exit code, stdout, stderr)."""
    cmd = [SANDBOX_EXEC, "-p", rac.SANDBOX_PROFILE, tool, "--settings", rac.SETTINGS] + args
    try:
        res = subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=180)
    except subprocess.TimeoutExpired:
        raise Refusal("c2patool did not finish within 180 seconds")
    return cmd, res.returncode, res.stdout.decode("utf-8", "replace"), res.stderr.decode("utf-8", "replace")


def tool_version(tool):
    try:
        res = subprocess.run([SANDBOX_EXEC, "-p", rac.SANDBOX_PROFILE, tool, "--version"], capture_output=True,
                             timeout=60)
    except subprocess.TimeoutExpired:
        raise Refusal("c2patool --version did not finish within 60 seconds")
    lines = res.stdout.decode("utf-8", "replace").strip().splitlines()
    if res.returncode != 0 or not lines:
        raise Refusal("could not run c2patool --version inside the sandbox (exit code %d)" % res.returncode)
    return lines[0].strip()


def unreadable(rc):
    return {"state": "ERROR", "exit_code": rc, "message": "c2patool output could not be read"}


def summarize(rc, stdout, stderr, name):
    """The runner's summary of one c2patool run. Output it cannot read becomes ERROR instead of stopping the check."""
    try:
        # Paths to the file are masked so that a name containing "No claim found" cannot change the state. Only the
        # name after a "/" is masked, so a short name such as "found" cannot alter c2patool's own message.
        summary = rac.summarize_report(rc, stdout, stderr.replace("/" + name, "/<file>"))
    except (AttributeError, TypeError, ValueError, RecursionError):
        return unreadable(rc)
    for key in ("failure_codes", "informational_codes", "success_codes"):
        if key in summary:
            summary[key] = [c for c in summary[key] if isinstance(c, str)]
    return summary


def check(paths, tool_dir, out_path):
    """Check each file, write the page and return the lines of the terminal summary."""
    if not os.path.isfile(SANDBOX_EXEC):
        raise Refusal("this version runs c2patool only inside the macOS sandbox (%s), which this system does not have"
                      % SANDBOX_EXEC)
    tool_dir = os.path.realpath(tool_dir)
    if not os.path.isdir(tool_dir):
        raise Refusal("no c2patool folder at %s" % tool_dir)
    hashes = {}
    for rel, expected in TESTED_RELEASE["sha256"].items():
        path = os.path.join(tool_dir, rel)
        if not os.path.isfile(path):
            raise Refusal("%s is missing from the c2patool folder %s" % (rel, tool_dir))
        hashes[rel] = sha256_file(path)
        if hashes[rel] != expected:
            raise Refusal("%s in %s is not the file from %s, the release this checker is tested with (SHA-256 %s "
                          "expected, %s found)" % (rel, tool_dir, TESTED_RELEASE["name"], expected, hashes[rel]))
    tool = os.path.join(tool_dir, "c2patool")
    anchors = os.path.join(tool_dir, "sample", "trust_anchors.pem")
    store = os.path.join(tool_dir, "sample", "store.cfg")
    if not os.access(tool, os.X_OK):
        raise Refusal("c2patool in %s is not executable" % tool_dir)
    out_path = os.path.abspath(out_path)
    if os.path.lexists(out_path):
        raise Refusal("will not overwrite %s; choose a new file name" % out_path)
    if not os.path.isdir(os.path.dirname(out_path)):
        raise Refusal("the folder for %s does not exist" % out_path)

    inputs, seen = [], set()
    for given in paths:
        real = os.path.realpath(given)
        if not os.path.isfile(real):
            raise Refusal("not a file: %s" % given)
        if real in seen:
            raise Refusal("listed twice: %s" % given)
        seen.add(real)
        if os.path.getsize(real) > MAX_BYTES:
            raise Refusal("larger than 25 MB, which this version does not embed: %s" % given)
        try:
            data = read_bytes(real)
        except OSError as e:
            raise Refusal("cannot read %s: %s" % (given, e.strerror))
        kind = image_kind(data)
        if kind is None:
            raise Refusal("not a JPEG or PNG file (this version checks only those): %s" % given)
        inputs.append((os.path.abspath(given), real, data, kind))

    version = tool_version(tool)
    started = datetime.datetime.now().astimezone()
    home = os.path.expanduser("~")
    trust_args = ["trust", "--trust_anchors", anchors, "--trust_config", store]
    cases, lines = [], []
    for i, (given_abs, real, data, (fmt, mime, width, height)) in enumerate(inputs, 1):
        # The file is named as it was given (a symbolic link keeps its own name); c2patool reads it from its folder.
        folder, name = os.path.split(given_abs)
        sanitize = sanitizer([(folder, "<input-folder>"), (os.path.dirname(real), "<input-folder>"),
                              (tool_dir, "<c2patool>"), (REPO, "<evidelle>"), (home, "<home>")])
        policies, claims = {}, None
        for pol in POLICIES:
            # "./" keeps a file name that starts with "-" from being read as an option.
            args = ["./" + name] + (trust_args if pol == "test_trust_anchors" else [])
            cmd, rc, stdout, stderr = run_c2patool(tool, args, folder)
            stdout, stderr = sanitize(stdout), sanitize(stderr)
            summary = summarize(rc, stdout, stderr, name)
            declared = None
            if rc == 0:
                try:
                    declared = claims_from_report(stdout)
                except (ValueError, AttributeError, TypeError, RecursionError):
                    summary = unreadable(rc)
            if declared is not None:
                text = stdout if stdout.endswith("\n") else stdout + "\n"
                claims = claims if claims is not None else declared
            else:
                text = "c2patool exit code %d\n--- stdout ---\n%s\n--- stderr ---\n%s\n" % (rc, stdout, stderr)
            policies[pol] = {
                "runner_summary": summary,
                "derived": derive(summary),
                "exit_code": rc,
                "command": [sanitize(c) for c in cmd],
                "working_directory": "<input-folder>",
                "report_text": text,
                "report_sha256": sha256_bytes(text.encode("utf-8")),
                # Kept separately when the report itself is JSON, so that the page still shows everything printed.
                "stderr_text": stderr if declared is not None and stderr.strip() else None,
            }
        try:
            unchanged = sha256_file(real) == sha256_bytes(data)
        except OSError:
            unchanged = False
        if not unchanged:
            raise Refusal("%s changed or disappeared while it was being checked" % name)
        image = {"original_name": printable(name), "format": fmt, "width": width, "height": height, "bytes": len(data),
                 "sha256": sha256_bytes(data),
                 "data_uri": "data:%s;base64,%s" % (mime, base64.b64encode(data).decode("ascii"))}
        cases.append({"id": "file-%d" % i, "origin": "local",
                      "source": {"kind": "Your file, read on this computer. It was not uploaded anywhere."},
                      "transform": "None. Checked exactly as found.", "image": image, "claims": claims,
                      "policies": policies})
        lines.append("%d. %s: %s, %d bytes, SHA-256 %s" % (i, image["original_name"], fmt, len(data), image["sha256"]))
        for pol, letter in zip(POLICIES, "AB"):
            d = policies[pol]["derived"]
            lines.append("   policy %s: c2patool state %s; binding %s, signature %s, signer %s"
                         % (letter, d["state"], d["binding"], d["signature"], d["signer_trust"]))
    finished = datetime.datetime.now().astimezone()

    template = read_bytes(TEMPLATE).decode("utf-8")
    if template.count(PLACEHOLDER) != 1:
        raise Refusal("the template's data placeholder is missing or repeated")
    settings_text = read_bytes(rac.SETTINGS).decode("utf-8")
    mac = platform.mac_ver()[0]
    data = {
        "mode": "local_check",
        "run": {
            "started": started.isoformat(timespec="seconds"),
            "finished": finished.isoformat(timespec="seconds"),
            "python": platform.python_version(),
            "os": ("macOS " + mac) if mac else platform.platform(),
            "tool": {"reported_version": version, "binary_sha256": hashes["c2patool"],
                     "tested_release": TESTED_RELEASE["name"], "release": rac.TOOL_SOURCE["release_url"],
                     "license": rac.TOOL_SOURCE["license"]},
            "offline_controls": {"sandbox_profile": rac.SANDBOX_PROFILE},
            "settings": {"file": "actual_c2pa/settings/offline.toml",
                         "sha256": sha256_bytes(settings_text.encode("utf-8")), "text": settings_text},
            "trust_policies": {
                "no_trust_anchors": {"extra_arguments": []},
                "test_trust_anchors": {"extra_arguments": ["trust", "--trust_anchors", "<c2patool>/sample/trust_anchors.pem",
                                                           "--trust_config", "<c2patool>/sample/store.cfg"],
                                       "files": {"sample/trust_anchors.pem": hashes["sample/trust_anchors.pem"],
                                                 "sample/store.cfg": hashes["sample/store.cfg"]}},
            },
            "checker": {"file": "viewer/src/check_files.py", "file_sha256": sha256_file(os.path.abspath(__file__))},
        },
        "policies": POLICY_TEXT,
        "cases": cases,
    }
    # ASCII only, and no "<" at all, inside the page's script element. Text that is not valid UTF-8 (such as an
    # undecodable file name) is escaped too, so writing the page cannot fail on it.
    try:
        payload = json.dumps(data, ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c")
    except RecursionError:
        raise Refusal("a c2patool report is nested too deeply to embed in the page; no page was written")
    html = template.replace(PLACEHOLDER, payload).encode("utf-8")
    try:
        fd = os.open(out_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise Refusal("will not overwrite %s; choose a new file name" % out_path)
    except OSError as e:
        raise Refusal("cannot create %s: %s" % (out_path, e.strerror))
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(html)
    except OSError as e:
        # Nothing is deleted: the incomplete page stays where it is, and the message says not to use it.
        raise Refusal("could not finish writing %s: %s. The incomplete page was left in place; do not open it, and "
                      "choose a new file name" % (out_path, e.strerror))
    lines.append("Wrote %s (%d bytes, readable only by you). Open it in a browser: it shows these results and loads "
                 "nothing from the network." % (out_path, len(html)))
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check JPEG or PNG files with c2patool 0.27.23, offline, and build a local "
                                             "viewer page. Nothing is uploaded.")
    ap.add_argument("--c2patool-dir", required=True, metavar="DIR",
                    help="the extracted c2patool 0.27.23 release folder (it holds the c2patool binary and sample/)")
    ap.add_argument("--out", required=True, metavar="REPORT.html", help="the page to write; it must not exist yet")
    ap.add_argument("files", nargs="+", metavar="FILE", help="JPEG or PNG files to check")
    args = ap.parse_args(argv)
    try:
        lines = check(args.files, args.c2patool_dir, args.out)
    except Refusal as e:
        print(printable("check_files: %s" % e), file=sys.stderr)
        return 2
    print(printable("\n".join(lines)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
