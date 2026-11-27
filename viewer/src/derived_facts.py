"""Per-policy C2PA check facts for the evidence viewer.

derive() turns one c2patool summary from the actual-C2PA runner (its state plus its success and failure status
codes) into the facts that overall() in template.html reads: manifest, binding, signature and signer_trust.
claims_from_report() reads the active manifest's declared fields from one raw c2patool report, for the page's
"Signer and declared claims" card. Both are copied unchanged from the viewer's capture script, so the label tests
and check_files.py need none of its acquisition code.
"""

import json


def claims_from_report(stdout):
    """The active manifest's declared fields, as c2patool reported them."""
    d = json.loads(stdout)
    active = (d.get("manifests") or {}).get(d.get("active_manifest") or "", {})
    actions = []
    for a in active.get("assertions") or []:
        if str(a.get("label", "")).startswith("c2pa.actions"):
            for act in (a.get("data") or {}).get("actions") or []:
                actions.append({k: act[k] for k in ("action", "digitalSourceType", "softwareAgent", "when", "parameters")
                                if k in act})
    return {
        "title": active.get("title"),
        "format": active.get("format"),
        "claim_generator": active.get("claim_generator"),
        "claim_generator_info": active.get("claim_generator_info"),
        "signature_info": active.get("signature_info") or {},
        "assertion_labels": [a.get("label") for a in active.get("assertions") or []],
        "actions": actions,
        "ingredients": [{k: i.get(k) for k in ("title", "format", "relationship")} for i in active.get("ingredients") or []],
        "manifest_count": len(d.get("manifests") or {}),
        "validation_state": d.get("validation_state"),
    }


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
