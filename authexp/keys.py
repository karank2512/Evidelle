"""Deterministic Ed25519 TEST keys and signing via the OpenSSL command-line tool.

The private keys are derived from public labels, so they are NOT secret. They exist only so the
experiment is reproducible byte-for-byte. Never use them for anything else.
"""

import base64
import hashlib
import os
import subprocess
import tempfile

# PKCS#8 DER prefix for an Ed25519 private key; the 32-byte seed follows.
_ED25519_PKCS8_PREFIX = bytes.fromhex("302e020100300506032b657004220420")


def _run(args, **kw):
    return subprocess.run(args, check=True, capture_output=True, **kw)


def openssl_version() -> str:
    return _run(["openssl", "version"]).stdout.decode().strip()


def make_test_key(name: str, out_dir: str) -> dict:
    seed = hashlib.sha256(("authexp-test-key:" + name).encode()).digest()
    der = _ED25519_PKCS8_PREFIX + seed
    b64 = base64.b64encode(der).decode()
    pem = "-----BEGIN PRIVATE KEY-----\n" + "\n".join(b64[i:i + 64] for i in range(0, len(b64), 64)) + "\n-----END PRIVATE KEY-----\n"
    priv_path = os.path.join(out_dir, name + ".key.pem")
    with open(priv_path, "w") as f:
        f.write(pem)
    pub_pem = _run(["openssl", "pkey", "-in", priv_path, "-pubout"]).stdout.decode()
    return {"name": name, "priv_path": priv_path, "pub_pem": pub_pem, "key_id": key_id_from_pub_pem(pub_pem)}


def key_id_from_pub_pem(pub_pem: str) -> str:
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "pub.pem")
        with open(p, "w") as f:
            f.write(pub_pem)
        der = _run(["openssl", "pkey", "-pubin", "-in", p, "-outform", "DER"]).stdout
    return hashlib.sha256(der).hexdigest()[:32]


def sign(priv_path: str, message: bytes) -> bytes:
    with tempfile.TemporaryDirectory() as d:
        m = os.path.join(d, "msg.bin")
        s = os.path.join(d, "sig.bin")
        with open(m, "wb") as f:
            f.write(message)
        _run(["openssl", "pkeyutl", "-sign", "-inkey", priv_path, "-rawin", "-in", m, "-out", s])
        with open(s, "rb") as f:
            return f.read()


def verify(pub_pem: str, message: bytes, signature: bytes) -> bool:
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "pub.pem")
        m = os.path.join(d, "msg.bin")
        s = os.path.join(d, "sig.bin")
        with open(p, "w") as f:
            f.write(pub_pem)
        with open(m, "wb") as f:
            f.write(message)
        with open(s, "wb") as f:
            f.write(signature)
        res = subprocess.run(
            ["openssl", "pkeyutl", "-verify", "-pubin", "-inkey", p, "-rawin", "-in", m, "-sigfile", s],
            capture_output=True,
        )
        return res.returncode == 0
