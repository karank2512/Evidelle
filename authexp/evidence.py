"""Map observed signal states to the strongest statement each one supports.

The mapping never issues a real/fake verdict. When a signal does not support a statement about
origin, the output is an explicit abstention.
"""

import re

from . import manifest as mf

PROVENANCE = {
    mf.VALID_TRUSTED: ("supports-specific-claim",
                       "The holder of a trust-listed key signed these claims, and the pixels are unchanged since signing. "
                       "This does not establish that the depicted scene is real or that the signed claims are true."),
    mf.VALID_UNTRUSTED: ("limited",
                         "Someone holding this key signed these claims, and the pixels are unchanged since signing. "
                         "The signer's identity is not established because the key is not on the trust list."),
    mf.VALID_REVOKED: ("abstain", "The signing key is on the revocation list, so the signed claims are not supported."),
    mf.BINDING_MISMATCH: ("abstain",
                          "The pixels changed after signing. Benign re-encoding and deliberate edits both produce this state, "
                          "so no conclusion about origin is supported."),
    mf.SIGNATURE_INVALID: ("abstain", "The manifest fails its signature or key checks, so no conclusion is supported."),
    mf.MALFORMED: ("abstain", "The manifest cannot be parsed, so no conclusion is supported."),
    mf.NO_MANIFEST: ("abstain", "No provenance information is present. Its absence is not evidence either way."),
}

WATERMARK = {
    True: ("supports-specific-claim-spoofable",
           "The toy watermark pattern for this key was detected. This is consistent with output from the key holder's "
           "generator, but a copied mark produces the same result (see the copy-attack results)."),
    False: ("abstain",
            "The toy watermark for this key was not detected. This does not indicate authenticity: other generators, "
            "processing and removal all produce the same result."),
}

DETECTOR = ("unevaluated", "No AI-image detector was available offline, so no detector result is reported.")
C2PA = ("unevaluated", "No C2PA verification tool was available offline, so C2PA conformance was not evaluated.")

# Affirmative verdict phrasing that the mapping must never produce. Negated caveats such as
# "does not establish that the depicted scene is real" are allowed.
VERDICT_PATTERNS = (
    r"\b(?:image|video|file|content|media|item|photo|picture)\s+is\s+(?:real|fake|authentic|genuine|ai-generated|synthetic)\b",
    r"\bproves?\b",
    r"\bcertif",
    r"\bverdict:\s*(?:real|fake)",
)


def summarize(provenance_state=None, watermark_detected=None) -> dict:
    statements = []
    if provenance_state is not None:
        level, text = PROVENANCE[provenance_state]
        statements.append({"signal": "provenance (toy manifest)", "state": provenance_state, "level": level, "statement": text})
    if watermark_detected is not None:
        level, text = WATERMARK[bool(watermark_detected)]
        statements.append({"signal": "watermark (toy scheme)", "state": "DETECTED" if watermark_detected else "NOT_DETECTED",
                           "level": level, "statement": text})
    statements.append({"signal": "AI-image detector", "state": "UNEVALUATED", "level": DETECTOR[0], "statement": DETECTOR[1]})
    statements.append({"signal": "C2PA verification", "state": "UNEVALUATED", "level": C2PA[0], "statement": C2PA[1]})
    overall = "abstain" if all(s["level"] in ("abstain", "unevaluated") for s in statements) else "partial-support-only"
    return {"overall": overall, "real_or_fake_verdict": "not issued", "statements": statements}


def contains_verdict_language(text: str) -> bool:
    low = text.lower()
    return any(re.search(p, low) for p in VERDICT_PATTERNS)
