# Actual C2PA results (official c2patool; offline)

This is separate from the toy preparation in RESULTS.md. It uses the official `c2patool` 0.27.23 binary (release https://github.com/contentauth/c2pa-rs/releases/tag/c2patool-v0.27.23; asset SHA-256 `380647e657ed16bb7e61982bd52f6c0b49a1cd92f09dbef49febd0f4c439a673`, matching GitHub's recorded digest).

**Offline controls:** every run is in a macOS sandbox that denies all network access. Remote-manifest and OCSP fetching are disabled. Trust anchors are local files only, and no timestamp authority was used when signing.

**Trust conditions:**
- *No trust anchors:* nothing is configured as trusted.
- *Test trust anchors:* the C2PA **test** root bundled with c2patool (FOR TESTING ONLY). "Trusted" therefore means "chains to the test root" here, not to any production trust list.

**These states describe signatures, bindings and trust configuration. They are not verdicts on whether a scene is real.** AI-image detectors, SynthID and production watermarks remain unevaluated.

## 1. Official C2PA test files and bundled samples

| File | Documented expectation | No trust anchors | Failure codes (no anchors) | Test trust anchors |
|---|---|---|---|---|
| adobe-20220124-CA.jpg | Valid claim with one ingredient; signed with C2PA Tool's test certificate | `Valid` | signingCredential.untrusted | `Trusted` |
| adobe-20220124-E-sig-CA.jpg | Invalid credentials: invalid signature | `Invalid` | signingCredential.untrusted, claimSignature.mismatch | `Invalid` |
| adobe-20220124-E-dat-CA.jpg | Invalid credentials: hard binding hash mismatch | `Invalid` | signingCredential.untrusted, assertion.dataHash.mismatch | `Invalid` |
| adobe-20220124-E-uri-CA.jpg | Invalid credentials: assertion URI hash mismatch | `Invalid` | signingCredential.untrusted, assertion.hashedURI.mismatch | `Invalid` |
| truepic-20230212-landscape.jpg | Example of camera capture details (production signer, not the test certificate) | `Valid` | signingCredential.untrusted | `Valid` |
| c2patool sample/C.jpg | Bundled with c2patool (sample/); expectation not documented, observed only | `Valid` | signingCredential.untrusted | `Trusted` |
| c2patool sample/image.jpg | Bundled with c2patool (sample/); expectation not documented, observed only | `NO_MANIFEST` | Error: No claim found | `NO_MANIFEST` |

Sources: https://github.com/c2pa-org/public-testfiles (`legacy/1.4/image/jpeg`, CC-BY-SA-4.0), plus the `sample/` folder in the c2patool release zip. Each downloaded test file matched the git blob hash GitHub records for it.

## 2. Synthetic images signed with TEST credentials, then processed

| Case | What was done | C2PA chunk present (PNG) | No trust anchors | Failure codes (no anchors) | Test trust anchors | Declared source type |
|---|---|---|---|---|---|---|
| A01_png_signed_intact | Synthetic landscape signed with TEST credentials, declared algorithmicMedia; unchanged. | True | `Valid` | signingCredential.untrusted | `Trusted` | algorithmicMedia |
| A02_png_lossless_recompress | Same pixels, IDAT re-compressed (zlib level 1); C2PA chunk kept in place. | True | `Invalid` | signingCredential.untrusted, assertion.dataHash.mismatch | `Invalid` | algorithmicMedia |
| A03_png_one_value_changed | One colour value changed by 1; C2PA chunk kept. | True | `Invalid` | signingCredential.untrusted, assertion.dataHash.mismatch | `Invalid` | algorithmicMedia |
| A04_png_crop_8px | Cropped by 8 px; C2PA chunk kept. | True | `Invalid` | signingCredential.untrusted, assertion.dataHash.mismatch | `Invalid` | algorithmicMedia |
| A05_png_c2pa_chunk_removed | C2PA chunk removed; pixels and IDAT bytes unchanged. | False | `NO_MANIFEST` | Error: No claim found | `NO_MANIFEST` | - |
| A06_png_manifest_transplanted | C2PA chunk from the signed landscape inserted into a different synthetic image. | True | `Invalid` | signingCredential.untrusted, assertion.dataHash.mismatch | `Invalid` | algorithmicMedia |
| A07_png_sips_resave | Signed PNG re-saved as PNG by macOS sips. | False | `NO_MANIFEST` | Error: No claim found | `NO_MANIFEST` | - |
| A08_png_false_capture_claim | The same synthetic landscape signed with TEST credentials but declared digitalCapture (a false claim, made deliberately). | True | `Valid` | signingCredential.untrusted | `Trusted` | digitalCapture |
| B01_jpeg_signed_intact | Synthetic landscape JPEG signed with TEST credentials; unchanged. |  | `Valid` | signingCredential.untrusted | `Trusted` | algorithmicMedia |
| B02_jpeg_lossless_transcode_markers_kept | jpegtran -copy all -optimize (lossless; all markers copied). |  | `Invalid` | signingCredential.untrusted, assertion.dataHash.mismatch | `Invalid` | algorithmicMedia |
| B03_jpeg_lossless_transcode_markers_dropped | jpegtran -copy none (lossless; extra markers dropped). |  | `NO_MANIFEST` | Error: No claim found | `NO_MANIFEST` | - |
| B04_jpeg_reencode_q75 | Decoded and re-encoded at JPEG quality 75 (libjpeg-turbo). |  | `NO_MANIFEST` | Error: No claim found | `NO_MANIFEST` | - |
| B05_jpeg_sips_resave_q80 | Signed JPEG re-saved as JPEG (quality 80) by macOS sips. |  | `NO_MANIFEST` | Error: No claim found | `NO_MANIFEST` | - |

## 3. What each state supports

- **Trusted:** The signature is valid and chains to the configured trust anchors. Here those are C2PA TEST anchors (FOR TESTING ONLY) unless stated otherwise. The signed claims are the signer's declarations; this does not establish that the depicted scene is real.
- **Valid:** The manifest is intact and the signature is valid, but the signer does not chain to a configured trust anchor (see signingCredential.untrusted). The signer's identity is not established.
- **Invalid:** The manifest fails validation (see the failure codes). No conclusion about origin is supported.
- **NO_MANIFEST:** c2patool found no C2PA manifest. Absence is not evidence either way.
- **ERROR:** The tool reported an error. The result is unknown.

Test signing certificate used for the synthetic cases: subject=C=US, ST=CA, L=Somewhere, O=C2PA Test Signing Cert, OU=FOR TESTING_ONLY, CN=C2PA Signer; notBefore=Jun 10 18:46:40 2022 GMT; notAfter=Aug 26 18:46:40 2030 GMT.
