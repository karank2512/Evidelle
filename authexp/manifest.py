"""A toy signed provenance manifest. It is NOT C2PA and must not be read as C2PA conformance.

It borrows three ideas from C2PA-style provenance so their limits can be shown offline:
- signed claims made by a key holder;
- a hard binding (SHA-256 over decoded pixels and dimensions);
- a trust list of known signer keys, optionally with revocation.

Verification returns a state, not a verdict about the depicted scene.
"""

import base64
import json

from . import keys
from .imageio import MANIFEST_CHUNK, read_png

FORMAT = "toy-provenance-manifest/0.1 (illustrative; NOT C2PA)"

NO_MANIFEST = "NO_MANIFEST"
MALFORMED = "MALFORMED"
SIGNATURE_INVALID = "SIGNATURE_INVALID"
BINDING_MISMATCH = "BINDING_MISMATCH"
VALID_UNTRUSTED = "VALID_UNTRUSTED"
VALID_REVOKED = "VALID_REVOKED"
VALID_TRUSTED = "VALID_TRUSTED"

STATES = (NO_MANIFEST, MALFORMED, SIGNATURE_INVALID, BINDING_MISMATCH, VALID_UNTRUSTED, VALID_REVOKED, VALID_TRUSTED)


def canonical(body: dict) -> bytes:
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


def build_manifest(img, claims: dict, key: dict, claimed_key_id: str = None) -> bytes:
    """Sign `claims` plus a pixel binding with `key`. `claimed_key_id` lets a test forge the key id."""
    body = {
        "format": FORMAT,
        "claims": claims,
        "binding": {"alg": "sha256", "covers": "decoded 8-bit RGB pixels + dimensions", "hash": img.pixel_digest()},
        "signer_key_id": claimed_key_id or key["key_id"],
    }
    signature = keys.sign(key["priv_path"], canonical(body))
    manifest = dict(body)
    manifest["signer_public_key_pem"] = key["pub_pem"]
    manifest["signature_b64"] = base64.b64encode(signature).decode()
    return json.dumps(manifest, sort_keys=True, indent=1).encode()


def manifest_chunk(manifest_bytes: bytes):
    return (MANIFEST_CHUNK, manifest_bytes)


def verify_png(path, trust_list=(), revoked=(), check_revocation=True) -> dict:
    img, _text, chunks = read_png(path)
    return verify_image(img, chunks, trust_list, revoked, check_revocation)


def verify_image(img, chunks, trust_list=(), revoked=(), check_revocation=True) -> dict:
    found = [data for ctype, data in chunks if ctype == MANIFEST_CHUNK]
    if not found:
        return {"state": NO_MANIFEST}
    try:
        m = json.loads(found[0].decode())
        body = {k: m[k] for k in ("format", "claims", "binding", "signer_key_id")}
        pub_pem = m["signer_public_key_pem"]
        signature = base64.b64decode(m["signature_b64"])
    except (ValueError, KeyError, TypeError):
        return {"state": MALFORMED}
    result = {"claims": body["claims"], "signer_key_id": body["signer_key_id"]}
    if keys.key_id_from_pub_pem(pub_pem) != body["signer_key_id"]:
        return dict(result, state=SIGNATURE_INVALID, detail="declared key id does not match the embedded public key")
    if not keys.verify(pub_pem, canonical(body), signature):
        return dict(result, state=SIGNATURE_INVALID, detail="signature does not verify over the claims and binding")
    if img.pixel_digest() != body["binding"]["hash"]:
        return dict(result, state=BINDING_MISMATCH, detail="pixels differ from the signed binding")
    kid = body["signer_key_id"]
    if kid in trust_list:
        if check_revocation and kid in revoked:
            return dict(result, state=VALID_REVOKED)
        return dict(result, state=VALID_TRUSTED)
    return dict(result, state=VALID_UNTRUSTED)
