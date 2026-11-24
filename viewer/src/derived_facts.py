"""Per-policy C2PA check facts for the evidence viewer's summary label.

derive() turns one c2patool summary from the actual-C2PA runner (its state plus its success and failure status
codes) into the facts that overall() in template.html reads: manifest, binding, signature and signer_trust. It is
copied unchanged from the viewer's capture script, so the label tests need none of its acquisition code.
"""


def derive(summary):
    """Per-policy check outcomes, derived only from the codes in the runner's summary."""
    state = summary.get("state")
    if state in ("NO_MANIFEST", "ERROR"):
        return {"state": state, "manifest": "absent" if state == "NO_MANIFEST" else "unknown",
                "binding": "not_checked", "signature": "not_checked", "signer_trust": "not_checked"}
    succ = set(summary.get("success_codes") or [])
    fail = set(summary.get("failure_codes") or [])
    if "assertion.dataHash.match" in succ:
        binding = "match"
    elif any(c.endswith("dataHash.mismatch") for c in fail):
        binding = "mismatch"
    else:
        binding = "unknown"
    if "claimSignature.validated" in succ:
        signature = "validated"
    elif "claimSignature.mismatch" in fail:
        signature = "mismatch"
    else:
        signature = "unknown"
    if "signingCredential.trusted" in succ:
        trust = "trusted"
    elif "signingCredential.untrusted" in fail:
        trust = "untrusted"
    else:
        trust = "unknown"
    return {"state": state, "manifest": "present", "binding": binding, "signature": signature, "signer_trust": trust}
