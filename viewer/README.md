# Evidence viewer: check your own files locally

The local C2PA evidence viewer shows, for each file, whether it carries a C2PA Content Credential that is intact for
these exact bytes, who signed it, whether the signer chains to a configured trust list, and what stays unknown. It is a
provenance viewer only: there is no detector, no real-or-fake verdict and no AI-probability score.

## Check your own files

You need macOS (the checker runs c2patool inside `sandbox-exec` with network access denied), Python 3 and the
extracted c2patool 0.27.23 release folder for macOS (`c2patool-v0.27.23-universal-apple-darwin.zip` from
https://github.com/contentauth/c2pa-rs/releases/tag/c2patool-v0.27.23): the folder that holds the `c2patool` binary
and its `sample/` folder. This repository does not include c2patool. The checker compares the binary,
`sample/trust_anchors.pem` and `sample/store.cfg` with that release by SHA-256 and refuses other files, because the
page's explanations were checked against that release only.

From the repository root:

    python3 -I -B viewer/src/check_files.py --c2patool-dir PATH/TO/c2patool --out report.html photo.jpg other.png

The checker:
- accepts JPEG and PNG files of up to 25 MB each, and refuses anything else;
- runs c2patool twice per file, offline, in a network-denied sandbox, with the runner's offline settings
  (`actual_c2pa/settings/offline.toml`: no remote manifest fetch, no OCSP fetch). Policy A has no trust anchors;
  policy B uses the C2PA test anchors from c2patool's `sample/` folder;
- prints each file's c2patool state and the facts derived from it;
- writes one self-contained page to `--out` (the file must not exist yet; it is created readable only by you), with
  the results and the checked files embedded. Open it in a browser. The page runs no validation and loads nothing from
  the network. Nothing is uploaded. If writing fails partway, the checker says so and leaves the incomplete page in
  place rather than deleting anything; do not open it.

Privacy: the page replaces local folder paths with placeholders such as `<input-folder>`, but it embeds each file
exactly as it is, including any metadata inside it (for example camera details or a location), and it records the
time and time zone of the check and the macOS and Python versions. Share the page only as you would share the files.

## Files

- `src/check_files.py`: the checker described above. It reuses the actual-C2PA runner's sandbox profile, offline
  settings and report summary (`actual_c2pa/run_actual_c2pa.py`).
- `src/template.html`: the viewer page template. Its `overall()` function picks the summary label:
  - "Intact" only when c2patool's own state is Valid or Trusted, the data hash matched and the claim signature
    validated;
  - "Doesn't match" when the data hash does not match these bytes;
  - "Fails validation" for any other result that c2patool reports as Invalid;
  - "No credential" when there is no manifest, and "Unknown" for everything else, including output the checker cannot
    read and states it does not know.

  For files from the checker, `localReading()` adds the "can and cannot conclude" text from fixed rules keyed on that
  label, the same rules for every file.
- `src/derived_facts.py`: `derive()`, which turns one c2patool summary (state, success codes, failure codes) into the
  facts `overall()` reads, and `claims_from_report()`, which reads the signer's declared fields from a raw report. Both
  are copied unchanged from the viewer's capture script.
- `tests/test_overall_label.py`: runs the template's own `overall()` under node on synthetic state/code patterns, and
  checks that the previous `overall()` labelled two of those patterns "Intact".
- `tests/test_check_files.py`: runs the checker end to end with a stub c2patool that prints synthetic reports. It
  checks the embedded data, the labels and readings from the template's own functions, the page script rendering every
  file, the removal of folder paths, unreadable tool output and the refusals. Two refusals are not tested: c2patool
  taking longer than 180 seconds, and a failure partway through writing the page.

## Run the tests

Needs Python 3 (standard library only), node and macOS `sandbox-exec`. Nothing is installed or downloaded.

    cd viewer
    python3 -I -B -m unittest discover -s tests -v

The checker starts its own sandbox, so do not run these tests inside another `sandbox-exec`. One test runs the real
c2patool on the two sample images bundled with it. It runs only when `EVIDELLE_C2PATOOL_DIR` points to the extracted
c2patool 0.27.23 release folder, and is skipped otherwise.

With `EVIDELLE_KEEP_TEST_FILES=1`, the tests delete nothing: every temporary folder and file they create is left in
place, inside `TMPDIR` (set it to a folder of your choice).

## Limits

- "Trusted" under policy B means only that the signer chains to the public C2PA test roots shipped with c2patool,
  whose private key is public. No production trust list is configured or fetched, so a production signer shows as
  untrusted.
- No certificate revocation status is fetched (OCSP fetching is off), and remote (cloud) manifests are not fetched: a
  file whose credential is stored outside the file may show as having no credential, or as a result the checker
  cannot use. c2patool's own timestamp checks run, but how it decides timestamp-authority trust was not examined.
- macOS only, c2patool 0.27.23 only, JPEG and PNG only, and up to 25 MB per file.
- Only data-hash bindings (`assertion.dataHash`) are recognised. A file bound to its credential another way, for
  example by a box hash, shows as Unknown.
- The labels and the "can and cannot conclude" text come from fixed rules applied to c2patool's codes. They describe
  credential checks only. They are not real-or-fake verdicts.
- The test fixtures are hand-written synthetic patterns and a stub c2patool. They are not measured validation results
  and not evidence of accuracy.
