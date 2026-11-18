# Source ledger: Media authenticity and deepfake detection

This ledger accompanies the report "Media authenticity and deepfake detection". Every entry was accessed on 18 November 2026.

It records public sources only. It is not legal advice and not a verdict on any image or video.

## How to read this ledger

**Source ID prefixes.** IDs group sources by topic. Every ID cited in the report resolves to an entry below.

| Prefix | Topic | Entries |
|---|---|---|
| PV | Provenance and watermarking | 67 |
| DS | Detector science and failure modes | 35 |
| VE | Vendor claims versus independent evidence | 36 |
| LG | Legal and evidentiary landscape | 59 |
| MK | Users, market and verification workflow | 60 |
| NC | Non-consensual intimate imagery: needs and harms | 51 |
| RC | Uncertainty framing and misuse | 28 |

That is 336 populated entries in total. MK-36, MK-39 and MK-43 are unassigned, so 339 is the highest allocated-ID count, not the number of populated entries. About 18 sources appear under two IDs; they are listed below.

**Fields.** Each entry gives as many of these as were available:
- title
- author or publisher
- source type
- URL
- publication date
- read status
- the specific claims the source supports
- limitations
- tensions or contradictions with other sources

**Read status.**

| Label | Meaning |
|---|---|
| full text | Read in full |
| most of the text | Read except a final portion, which is noted where known |
| partial | Read in part, for example a landing page, a section, or a paywalled portion |
| abstract only | Only the abstract was read |
| secondary, snippet, extract or (2°) | Known only through a secondary account or a search-result summary |

Claims that rest only on secondary or snippet reads are unverified and should be checked before anyone relies on them. "Not accessible" means the primary page could not be read; the reason could be a paywall, a block, or the page being unavailable.

**Evidence types.** Entries label their evidence type. The types are vendor marketing, platform or vendor documentation, academic benchmarks, independent or real-world evaluations, standards text, government and regulator statements, legislation and court records, NGO positions, legal scholarship and journalism. Vendor marketing is kept separate from independent evidence.

## Sources listed under more than one ID

| Source | IDs |
|---|---|
| Deepfake-Eval-2024 (Chandra et al., arXiv 2503.02857) | DS-01 = VE-01 |
| WITNESS TRIED benchmark (arXiv 2504.21489) | VE-02 = MK-04 |
| 404 Media, "AI Images Detectors Are Being Used to Discredit the Real Horrors of War" (13 Oct 2023) | VE-06 = RC-10 |
| Groh et al., "Deepfake detection by human crowds, machines, and machine-informed crowds" (PNAS 2022) | DS-17 (arXiv version) = RC-21 (PMC version) |
| Saberi et al., "Robustness of AI-Image Detectors: Fundamental Limits and Practical Attacks" (ICLR 2024) | DS-13 = PV-12 |
| Google Gemini Help, "Verify AI-generated images, videos, and audio" | PV-09 = MK-06 |
| TAKE IT DOWN Act (P.L. 119-12; S.146 enrolled) | LG-07 = NC-19 |
| Chesney & Citron, "Deep Fakes: A Looming Challenge…" (California Law Review 2019) | LG-44 = RC-24 |
| NIST AI 100-4, "Reducing Risks Posed by Synthetic Content" (Nov 2024) | RC-20 (read in part) = PV-38 (publication page and abstract only) |
| EU AI Act Article 50 | LG-28 = PV-32 |
| EU Digital Omnibus on AI, Regulation (EU) 2026/1744 | LG-56 (EUR-Lex, full text); LG-29 = PV-31 (secondary) |
| European Commission Code of Practice on marking and labelling AI-generated content (10 Jun 2026) | LG-30 = PV-28 |
| Ofcom investigation into X over Grok (opened 12 Jan 2026) | LG-22 ≈ NC-15 |
| European Commission DSA proceedings against X over Grok (26 Jan 2026) | LG-31 ≈ NC-16 |
| Ofcom statement, "Detecting intimate image abuse" (2026) | LG-21 = NC-42 |
| NIST GenAI image-discriminator evaluation | DS-31 ≈ VE-23 |
| DARPA AI FORCE challenges | DS-29 ≈ VE-24 |
| NewsGuard detector test (8 May 2026) | RC-12 = VE-31 |
| Meta "Made with AI" to "AI info" label change (2024) | VE-30 (Meta's post) ≈ RC-13 ≈ PV-51 (coverage) |

## Contradictions and tensions across topics

Each topic section below also lists the tensions specific to its own sources.

1. **Benchmarks versus in-the-wild performance.**
   - In-distribution accuracy reached up to 99.9% (DS-03).
   - On circulating content, AUC was about 0.5 (DS-01, DS-09).
   - Vendor headline claims are 95–99.5% (VE-10, VE-15, VE-19, VE-21). The best commercial accuracy on Deepfake-Eval-2024 was 0.78–0.89 (DS-01).
   - The datasets and dates differ, so this tension is structural, not a contradiction about any one vendor.
2. **Deepfake-Eval-2024's internal inconsistencies.**
   - The best commercial image model is reported as 0.82/0.90 in Table 5 and as 0.86/0.88 in Table S10.
   - The maximum open-source AUC is 0.58 in the text but 0.63 in Table 3.
   - Image counts are 767/1,208 in DS-01 and 759/1,191 in DS-25.
3. **Hive.**
   - Hive flagged 0 of 15 authentic war photos in NewsGuard's test (RC-12).
   - A Hive result ("likely to be AI-Generated", 96.9%) was used against an authentic Netanyahu video (RC-12).
   - Hive markets "industry-leading accuracy" (VE-12).
4. **SynthID robustness.**
   - The provider reports a worst-case true-positive rate of 99.72% at a 0.1% false-positive rate (PV-10).
   - Attack papers report removal or forgery of other watermark schemes (PV-11, PV-13, PV-14, PV-15). The threat models differ.
   - No independent test of production SynthID was found. A 2026 removal claim is disputed and unverified (PV-49).
5. **What missing provenance means.**
   - C2PA says absence should not lower trust (PV-01).
   - NIST says absence could become a signal only "where it would have been expected" (RC-20).
   - Google argues that labelling only AI content creates an implied-truth effect (PV-06).
6. **The liar's dividend.**
   - Experiments using 2021–22 data found that "it's fake" claims were largely ineffective against authentic video (RC-09).
   - Field cases from 2023–26 show authentic images and video being discredited (RC-11, RC-12, VE-03, VE-06).
   - The mechanisms, periods and measures differ.
7. **Human accuracy on modern video.** One small study reports 87.5% (DS-10); others report about 58–66% (DS-09, DS-22, DS-23).
8. **Removal versus offence elements.**
   - Removal processes rest on identity and non-consent (LG-07, LG-17 to LG-19, LG-36; NC-19 to NC-21).
   - Some offences and prohibitions use realism or genuineness thresholds:
     - the US "digital forgery" definition (LG-07);
     - the EU ban on systems that generate "realistic" non-consensual intimate images (LG-56);
     - New Zealand's recording-based offences (LG-37, secondary);
     - the UK s.66E creation offence, which covers only fake or altered images (LG-17).
   - Some platform intake routes separate "fake" from "real" (Google, NC-24), or turn on "photoshop" rather than consent (Meta, NC-27).
9. **Court burden for alleged deepfakes.**
   - Some authorities put the initial burden on the party alleging fabrication: *State v. Amyda* (LG-11), *Head v John Doe* (LG-16), and the draft FRE 901(c).
   - *Matter of M.S.* (LG-13) requires a stronger foundation for "found" videos. Its vote is reported as both 4–3 and 5–2.
10. **Ofcom hash-matching for intimate image abuse.**
    - The statement is dated 18 May 2026 on its page and June 2026 in a bulletin (LG-21).
    - One extract reports the measures in force from 30 September 2026 (NC-42), but the legal sources read could not confirm this. Treat the in-force date as unverified.
11. **Is synthetic NCII "less bad" or "worse"?**
    - Adults across 10 countries rate real NCII as worse (NC-01).
    - In Thorn's survey, 16% of young people saw little or no harm, and 28% of them said it was because the images were "not real" (NC-03).
    - 55% of UK teens say a deepfake would be worse (NC-06).
    - The questions and populations differ.
12. **Gender pattern in NCII victimisation.**
    - Adult self-report surveys show more men reporting victimisation (NC-01, NC-02).
    - Regulator and school data show mostly girls depicted (NC-05, NC-08).
13. **The UK forensic regulator and validation expectations.**
    - The UK Forensic Science Regulator's Code v2 names deepfake analysis but lifts the ISO accreditation requirement for that sub-activity (RC-17).
    - PCAST holds that claims without accuracy estimates are "scientifically meaningless" (RC-18).
14. **TrueMedia.org's status.** Its free detector was sunset in January 2025 (VE-09, MK-12; partly secondary). Since 16 April 2025 it has run as a closed beta at Georgetown's McCourt School (MK-14, MK-17).
15. **Platform credential handling over time.**
    - In October 2025, no platform tested preserved credentials (PV-19).
    - Labelling improved on some platforms by March 2026 (PV-18).
    - No direct preservation test since then was found.
16. **Resolved discrepancies.**
    - Thorn's "not real" figure is 28% of the 16% who saw little or no harm, not 16% of all respondents (NC-03).
    - The EU Omnibus grace-period date of 2 December 2026 is confirmed by the Official Journal text (LG-56). This supersedes a conflicting secondary reading (PV-31).

## Sources by topic

## PV: Provenance and watermarking (sources)

Access date for all entries: 2026-11-18. "Snippet" means only a search-engine summary was seen.

- **PV-01**
  - Title: C2PA and Content Credentials Explainer, v2.3
  - Publisher: C2PA
  - Type: standards body
  - URL: https://spec.c2pa.org/specifications/specifications/2.3/explainer/Explainer.html
  - Date: undated (©2026)
  - How read: full text
  - Supports: manifest definition; assertions, actions, `digitalSourceType`, ingredients; created vs gathered assertions; hard and soft bindings; trust relationships; explicit disclaimers ("do not provide value judgments…"; "alone cannot tell you whether … true"; "not a cure-all"; removal "Yes it can"; "Provenance is not always complete"); identity not addressed; absence not meant to reduce trust; ML-DSA planned
  - Limitations: a promotional explainer by the standards body; no date
  - Tensions: with PV-06 on how to treat absence
- **PV-02**
  - Title: C2PA Technical Specification 2.3
  - Publisher: C2PA
  - Type: standards body
  - URL: https://spec.c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html
  - Date: version history "2.3 - December 2025" (PDF cover reportedly 2026-01-05)
  - How read: partial (Sections 14–15 and 18 not reached)
  - Supports: trust list definition and EKU restriction; well-formed / valid / trusted concepts; hard and soft binding definitions ("a soft binding shall not be used as a hard binding"); timestamp and revocation rationale; signer attribution limits (EXIF GPS); `c2pa.created` / `c2pa.opened` mandatory; "SHOULD NOT provide value judgments"
  - Limitations: validation definitions not read
  - Tensions: date vs PV-03; revocation design vs practice (PV-20, PV-21)
- **PV-03**
  - Title: The C2PA launches Content Credentials 2.3 and celebrates 5 years of impact
  - Publisher: C2PA
  - Type: standards body (news post)
  - URL: https://c2pa.org/the-c2pa-launches-content-credentials-2-3-and-celebrates-5-years-of-impact-across-the-digital-ecosystem/
  - Date: last updated 2026-02-23 (snippet suggests 9 February 2026)
  - How read: full
  - Supports: 2.3 features (live video, formats, edit detail, cloud, validation); "More than 6,000 members and affiliates have live applications"; conformance "late 2025"
  - Limitations: promotional; ambiguous member figure
  - Tensions: conformance date vs PV-04 and PV-05
- **PV-04**
  - Title: Content Credentials: Deployment Guidance, v1.0
  - Publisher: C2PA
  - Type: standards body
  - URL: https://c2pa.org/wp-content/uploads/sites/33/2026/07/Content-Credentials-Deployment-Guidance.pdf
  - Date: 2026-07-08
  - How read: partial (text incomplete)
  - Supports: Valid / Trusted / Tampered / No-CC states with quotes; conformance launch 4 June 2025; "54 products from 31 companies" by 14 May 2026; more than 120 companies with expressions of interest; "Durable Content Credentials" = manifest + watermark + fingerprint; avoid screenshots and re-exports; treat missing or invalid credentials with caution
  - Limitations: later sections unread
  - Tensions: launch date vs PV-03 and PV-05
- **PV-05**
  - Title: Raising the bar for trust: introducing the C2PA Conformance Program
  - Author: Andy Parsons (CAI/Adobe)
  - Type: NGO / industry initiative blog (vendor-affiliated)
  - URL: https://contentauthenticity.org/blog/raising-the-bar-for-trust-introducing-the-c2pa-conformance-program
  - Date: 2025-10-09
  - How read: full
  - Supports: soft launch June 2025; "fully up and running"; two security levels; Pixel 10 at highest level
  - Limitations: Adobe-led initiative (conflict of interest); no counts; no trust-list or revocation detail
  - Tensions: date vs PV-04
- **PV-06**
  - Title: How Pixel and Android are bringing a new level of trust to your images with C2PA Content Credentials
  - Authors: Eric Lynch, Sherif Hanna (Google)
  - Type: platform or vendor documentation / marketing
  - URL: https://blog.google/security/pixel-android-trusted-images-c2pa-content-credentials/ (also on security.googleblog.com)
  - Date: 2025-09-10
  - How read: full
  - Supports: all JPEG captures signed; Google Photos signing of edits; Assurance Level 2; StrongBox/Titan M2; one-time certificates; offline time-stamping authority; "implied truth effect" quote
  - Limitations: vendor self-description; no independent audit
  - Tensions: with PV-01 (absence), PV-26 (Apple), PV-45 and PV-46 (Samsung)
- **PV-07**
  - Title: How we're increasing transparency for gen AI content with the C2PA
  - Author: Laurie Richardson (Google)
  - Type: vendor documentation / marketing
  - URL: https://blog.google/technology/ai/google-gen-ai-content-transparency-c2pa/
  - Date: 2024-09-17
  - How read: full
  - Supports: "About this image" C2PA plan; Ads; YouTube "exploring" camera disclosure; "validate content against the forthcoming C2PA Trust list"; "no silver bullet"
  - Limitations: dated; plans, not outcomes; partially superseded by PV-06, PV-08, PV-09 and PV-41
  - Tensions: none
- **PV-08**
  - Title: AI image verification in the Gemini app
  - Authors: Pushmeet Kohli, Laurie Richardson (Google)
  - Type: vendor documentation / marketing
  - URL: https://blog.google/technology/ai/ai-image-verification-gemini-app/
  - Date: 2025-11-20
  - How read: full
  - Supports: SynthID check in Gemini; "over 20 billion AI-generated pieces of content" watermarked; Nano Banana Pro C2PA; planned video, audio and Search; future C2PA checks for non-Google models
  - Limitations: no accuracy figures; no third-party SynthID adoption documented
  - Tensions: scale figure vs PV-10
- **PV-09**
  - Title: Verify AI-generated images, videos, and audio (Gemini Apps Help)
  - Publisher: Google
  - Type: platform documentation
  - URL: https://support.google.com/gemini/answer/16722517?hl=en
  - Date: undated (live page)
  - How read: full
  - Supports: SynthID detects only Google AI; a negative result "could have been created by other AI systems"; limits (100 MB, video under 90 s, audio under 1 h, quotas); inconclusive outcomes; credentials verified only from C2PA 2.2+ Conforming Products List; remote manifests unsupported; iOS "soon"; may miss watermark "after many alterations"
  - Limitations: vendor documentation; may change
  - Tensions: none
- **PV-10**
  - Title: SynthID-Image: Image watermarking at internet scale
  - Authors: Gowal et al. (Google DeepMind)
  - Type: preprint
  - URL: https://arxiv.org/html/2510.09263v1 (abstract: https://arxiv.org/abs/2510.09263)
  - Date: 2025-10-10
  - How read: partial (limitations section not reached)
  - Supports: more than ten billion images and frames; trusted-tester verification; threat model; "Achieving perfect security is impossible"; black-box vs white-box framing; SynthID-O TPR@0.1%FPR figures (100.00 / 99.98 / 99.72 / 98.06 / 99.97 / 99.96%; WAM 83.37%)
  - Limitations: self-evaluation of the external variant, not the production SynthID; provider conflict of interest; not peer-reviewed
  - Tensions: PV-14, PV-13, PV-49; scale vs PV-08
- **PV-11**
  - Title: Invisible Image Watermarks Are Provably Removable Using Generative AI
  - Authors: Zhao, Zhang, Su, Vasan, Grishchenko, Kruegel, Vigna, Wang, Li
  - Type: peer-reviewed (NeurIPS 2024)
  - URL: https://arxiv.org/abs/2306.01953 (HTML v3 read)
  - Date: v1 2023-06-02; v3 2024-10-31
  - How read: nearly full (HTML ~95%)
  - Supports: pre-attack TPR@FPR=0.01 of 1.000 for four schemes; over 99% removal for DwtDctSvd, RivaGAN and SSL; 98% removal with PSNR above 30; StegaStamp needs strong diffusion noise; Tree-Ring resilient but less invisible; call to shift away from invisible watermarks
  - Limitations: academic schemes, not production SynthID; 2023–2024 models
  - Tensions: PV-10
- **PV-12**
  - Title: Robustness of AI-Image Detectors: Fundamental Limits and Practical Attacks
  - Authors: Saberi, Sadasivan, Rezaei, Kumar, Chegini, Wang, Feizi
  - Type: peer-reviewed (ICLR 2024 as commonly cited; venue not shown on the arXiv page)
  - URL: https://arxiv.org/abs/2310.00076
  - Date: v1 2023-09-29; v2 2024-02-14
  - How read: abstract only
  - Supports: evasion/spoofing trade-off; diffusion purification; model-substitution attack; spoofing by adding watermarked noise to real images; robustness–reliability trade-off for classifiers
  - Limitations: no numbers read; older models
  - Tensions: PV-10
- **PV-13**
  - Title: WAVES: Benchmarking the Robustness of Image Watermarks
  - Authors: An, Ding, Rabbani, Agrawal, Xu, Deng, Zhu, Mohamed, Wen, Goldstein, Huang
  - Type: peer-reviewed (ICML 2024)
  - URL: https://arxiv.org/abs/2401.08573 (HTML v3)
  - Date: v1 2024-01-16; v3 2024-06-07
  - How read: partial (~2/3 of HTML)
  - Supports: TPR@0.1%FPR metric; Stable Signature 0.001 under Regen-Diff and 0.000 under Dist-Blur; Tree-Ring vulnerable to embedding attacks (near-zero TPR in grey-box; 0.448 average for AdvEmbG-KLVAE8); StegaStamp 0.943 under Regen-Diff
  - Limitations: three schemes; 2024
  - Tensions: PV-10
- **PV-14**
  - Title: UnMarker: A Universal Attack on Defensive Image Watermarking
  - Authors: Andre Kassis, Urs Hengartner
  - Type: peer-reviewed (IEEE S&P 2025)
  - URL: https://arxiv.org/abs/2405.08363
  - Date: v1 2024-05-14; v2 2024-11-22
  - How read: abstract only
  - Supports: no detector access needed; spectral attack; semantic watermark best detection reduced to 43%; "defensive watermarking is not a viable defense against deepfakes"
  - Limitations: schemes not named in the abstract; not tested on production SynthID
  - Tensions: PV-10
- **PV-15**
  - Title: Black-Box Forgery Attacks on Semantic Watermarks for Diffusion Models
  - Authors: Müller, Lukovnikov, Thietke, Fischer, Quiring
  - Type: peer-reviewed (CVPR 2025)
  - URL: https://arxiv.org/abs/2412.03283
  - Date: v1 2024-12-04; v3 2025-06-07
  - How read: abstract only
  - Supports: imprint, remove and forge semantic watermarks (Tree-Ring, Gaussian Shading) with one reference image and an unrelated model
  - Limitations: no numbers read; semantic in-generation watermarks only
  - Tensions: PV-10
- **PV-16**
  - Title: Video Seal: Open and Efficient Video Watermarking
  - Authors: Fernandez, Elsahar, Yalniz, Mourachko (Meta FAIR, inferred from the code organisation)
  - Type: preprint
  - URL: https://arxiv.org/abs/2412.09492
  - Date: 2024-12-12
  - How read: abstract only
  - Supports: open-source video watermark; codec-aware training; robustness claim vs baselines
  - Limitations: no numbers; self-evaluation; deployment status at Meta unknown
  - Tensions: none
- **PV-17**
  - Title: Tech platforms fail to label AI content (C2PA metadata audit)
  - Authors: Alexios Mantzarlis, Nasha Dutta (Indicator)
  - Type: journalism / independent evaluation
  - URL: https://indicator.media/p/tech-platforms-fail-to-label-ai-content-c2pa-metadata
  - Date: 2025-10-23
  - How read: partial (paywalled)
  - Supports: 516 posts on 5 platforms over 3 weeks; 169 (just over 30%) labelled; Pinterest 55% on images; TikTok labelled only in-app content; Google and Meta failed on their own tools' outputs; Parsons quotes
  - Limitations: methodology and per-platform tables behind paywall; superseded in part by PV-18
  - Tensions: industry claims (PV-06, PV-08)
- **PV-18**
  - Title: AI labeling is still very much a work in progress
  - Author: Alexios Mantzarlis (Indicator)
  - Type: journalism / independent evaluation
  - URL: https://indicator.media/p/ai-labeling-is-still-very-much-a-work-in-progress
  - Date: 2026-03-18
  - How read: partial (paywalled)
  - Supports: more than 200 posts (Google, Meta, OpenAI tools); LinkedIn and Pinterest 67%, YouTube ~50%, TikTok ~1/3, Instagram 15/105; Google more consistent C2PA; meta.ai outputs apparently lack credentials
  - Limitations: partial methodology; small samples
  - Tensions: Meta labelling claims (PV-51)
- **PV-19**
  - Title: "We uploaded a fake video to 8 social apps. Only one told users it wasn't real."
  - Author: Kevin Schaul (per PV-63)
  - Publisher: The Washington Post
  - Type: journalism / independent evaluation
  - URL: https://www.washingtonpost.com/technology/2025/10/22/ai-deepfake-sora-platforms-c2pa/ (read via https://incidentdatabase.ai/reports/6301 and PV-63)
  - Date: 2025-10-22
  - How read: secondary. The original was not accessible (paywalled); read via the AI Incident Database summary and a Substack reproduction (PV-63).
  - Supports: Sora clip with credentials ("Issued by OpenAI", per AIID); 8 platforms; "No platform that The Post tested kept the Content Credentials data on the video or let users access it"; only YouTube added a warning ("Altered or synthetic content", "hidden from view inside a description attached to the clip")
  - Limitations: single clip, single test; default settings; predates 2026 platform changes; per-platform detail for most platforms not itemised in either copy
  - Tensions: industry commitments; the Substack copy names only YouTube, Facebook and TikTok and does not name the generator
- **PV-20**
  - Title: Nikon struggles with security problems in photo authentication
  - Author: Thomas Hoffmann (heise online / c't Fotografie)
  - Type: journalism
  - URL: https://heise.de/-10667707
  - Date: 2025-09-23
  - How read: full (English version)
  - Supports: multiple-exposure bypass; "falsely signs the resulting composite image with a valid C2PA certificate"; AI image verified; service suspended; non-reconnected cameras keep signing; standard validation doesn't check revocation; "Nikon itself cannot intervene here"; 2024 AFP watermark plan
  - Limitations: relies on a forum researcher's demonstration; no Nikon statement quoted
  - Tensions: spec revocation design (PV-02)
- **PV-21**
  - Title: Nikon Can't Fully Solve the Z6 III's C2PA Problems Alone
  - Publisher: PetaPixel
  - Type: journalism
  - URL: https://petapixel.com/2025/09/22/nikon-cant-fully-solve-the-z6-iiis-c2pa-problems-alone/
  - Date: 2025-09-22
  - How read: snippet (page was not accessible)
  - Supports: validators cannot be prevented from validating images from revoked cameras
  - Limitations: not read
  - Tensions: PV-02
- **PV-22**
  - Title: Nikon sent out a new notice informing users that all C2PA certificates issued will be revoked
  - Publisher: Nikon Rumors
  - Type: journalism (enthusiast site)
  - URL: https://nikonrumors.com/2025/09/21/nikon-sent-out-a-new-notice-informing-users-that-all-c2pa-certificates-issued-will-be-revoked.aspx/amp/
  - Date: 2025-09-21
  - How read: snippet
  - Supports: revocation of all issued certificates
  - Limitations: rumour site; Nikon's notice not read
  - Tensions: none
- **PV-23**
  - Title: Nikon revokes all C2PA image authenticity certificates after major vulnerability exposed
  - Publisher: Digital Camera World
  - Type: journalism
  - URL: https://www.digitalcameraworld.com/photography/photojournalism/nikon-revokes-all-c2pa-image-authenticity-certificates-after-major-vulnerability-exposed
  - Date: September 2025 (exact date not captured)
  - How read: headline only
  - Supports: revocation (headline)
  - Limitations: body not read
  - Tensions: none
- **PV-24**
  - Title: Sora 2 Watermark Removers Flood the Web
  - Author: Matthew Gault (404 Media)
  - Type: journalism
  - URL: https://www.404media.co/sora-2-watermark-removers-flood-the-web
  - Date: 2025-10-07
  - How read: partial (paywalled)
  - Supports: visible watermark on every Sora 2 video; 3 sites tested, all removed it "in a matter of seconds"; "half a dozen websites"
  - Limitations: C2PA findings and expert quotes not visible; Sora app since discontinued (PV-47, PV-48)
  - Tensions: none
- **PV-25**
  - Title: Metawatch: C2PA content credentials
  - Publisher: IPTC
  - Type: NGO / standards body measurement (independent evaluation)
  - URL: https://metawatch.iptc.org/c2pa/
  - Date: live page; crawl series about 2026-06-03 to 2026-11-01
  - How read: full
  - Supports: 6,783 images; 29 with C2PA (0.43%); validation buckets (20 valid; 1 modified; 1 expired; 7 other_invalid); issuer counts (OpenAI 9, Adobe 8, IPTC 4, Canva 3, Google 2, vivo / Automattic / self-signed 1 each)
  - Limitations: mostly news sites; small denominators; presence-based; IPTC is a C2PA-aligned body
  - Tensions: earlier snapshot 0.22% (snippet); PV-57
- **PV-26**
  - Title: Apple launches a new way to prove a photo was shot with an iPhone, not generated by AI
  - Author: Joshua Benton (Nieman Lab)
  - Type: journalism
  - URL: https://www.niemanlab.org/2026/09/apple-launches-a-new-way-to-prove-a-photo-was-shot-with-an-iphone-not-generated-by-ai/
  - Date: 2026-09-09
  - How read: full
  - Supports: Apple Reference Image on iPhone 18 Pro / Pro Max; metadata ID plus Private Cloud Compute signature; opt-in per photo; Apple "hasn't signed on to using Content Credentials"
  - Limitations: launch-day reporting; no OS version given; interoperability unknown
  - Tensions: PV-06 (C2PA approach); low-quality claims about iOS SynthID (not used)
- **PV-27**
  - Title: Preserve Content Credentials with Cloudflare Images
  - Author: Will Allen (Cloudflare)
  - Type: vendor documentation / marketing
  - URL: https://blog.cloudflare.com/preserve-content-credentials-with-cloudflare-images/
  - Date: 2025-02-03 (from page metadata)
  - How read: full
  - Supports: opt-in per-zone preservation; Cloudflare signs transformations; CDNs "frequently" stripped credentials
  - Limitations: vendor; default state unclear
  - Tensions: internal text-vs-example inconsistency
- **PV-28**
  - Title: Commission publishes Code of Practice on marking and labelling of AI-generated content
  - Publisher: European Commission (DG CNECT)
  - Type: government or regulator
  - URL: https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content
  - Date: 2026-06-10 (updated 2026-06-12)
  - How read: full (press page)
  - Supports: final, voluntary code; obligations "apply from 2 August 2026"; deepfakes and public-interest text labelling; EU icons
  - Limitations: press page lacks technical detail; no Omnibus mention
  - Tensions: Omnibus grace (PV-31)
- **PV-29**
  - Title: European Commission publishes final Code of Practice on marking and labelling AI-generated content
  - Publisher: Jones Day
  - Type: other (law-firm analysis)
  - URL: https://www.jonesday.com/en/insights/2026/06/european-commission-publishes-final-code-of-practice-on-marking-and-labelling-aigenerated-content
  - Date: June 2026
  - How read: snippet
  - Supports: "at least two layers of machine-readable marking where necessary"; detection mechanisms for many stakeholder groups
  - Limitations: secondary; Code text not read
  - Tensions: none
- **PV-30**
  - Title: Strong backing for the Code of Practice on transparency of AI-generated content
  - Publisher: European Commission
  - Type: government or regulator
  - URL: https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content
  - Date: 2026-07-31 (last updated 2026-11-17)
  - How read: full
  - Supports: "about 190 organisations" by end-July 2026, about half small or recent companies; list shows 103 (Section 1, marking and detection), 219 (Section 2, labelling), 266 unique; Section 1 includes Google, Meta, Microsoft, OpenAI (Anthropic, Aleph Alpha, Cohere, Mistral, Synthesia also named); Code "assessed as adequate both by the Commission and the AI Board"; two task forces to launch September 2026; list updated on an ongoing basis
  - Limitations: count date for 266 not stated beyond the 17 November 2026 update; Adobe and TikTok not named in the parts read; the adequacy opinion not read
  - Tensions: the earlier snippet's "more than 90 in two task forces (30 September 2026)" was not visible in this read
- **PV-31**
  - Title: Regulation (EU) 2026/1744 (Digital Omnibus on AI)
  - Type: legislation
  - URL: https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act (the Official Journal text is recorded separately as LG-56)
  - Corroborated by (snippets): https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today and https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/
  - Date: Regulation of 2026-07-08; OJ 2026-07-24; in force 2026-07-27
  - How read: law-firm alerts read as snippets; the Official Journal text is recorded as LG-56 (full text)
  - Supports (confirmed): Article 5(1)(ba) bans systems that generate "realistic" non-consensual intimate images; Article 5(1)(bb) bans systems that generate CSAM; both from 2 December 2026; systems on the market before 2 August 2026 have until 2 December 2026 for machine-readable marking
  - Supports (law-firm alerts only): new systems comply from 2 August 2026; other Article 50 duties from 2 August 2026; high-risk Annex III delayed to 2 December 2027
  - Limitations: this entry relies on law-firm alerts; see LG-56 for the Official Journal text
  - Tensions: the DLA Piper table's 2 December 2027 is superseded by the confirmed 2 December 2026
- **PV-32**
  - Title: Regulation (EU) 2024/1689 (AI Act), Article 50
  - Type: legislation
  - URL: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (wording seen via https://www.orrick.com/en/insights/2026/08/eu-ai-act-transparency-obligations-for-ai-generated-content-article-50)
  - Date: OJ 2024-07-12; Article 50 applies 2026-08-02
  - How read: secondary (snippets); article text not re-read
  - Supports: Article 50(2) machine-readable marking and detectability; "effective, interoperable, robust and reliable as far as this is technically feasible"; technology-neutral
  - Limitations: Article 50(4) exceptions not verified
  - Tensions: none
- **PV-33**
  - Title: Measures for Labeling Artificial Intelligence-Generated Synthetic Content (English translation)
  - Publisher: China Law Translate (original issued by CAC, MIIT, MPS, NRTA)
  - Type: legislation (unofficial translation)
  - URL: https://www.chinalawtranslate.com/en/ai-labeling/
  - Date: promulgated 2025-03-07 (CLT) / released 2025-03-14 (others); effective 2025-09-01
  - How read: page not accessible; the translation was read in full via AGORA's reproduction (PV-65)
  - Supports: explicit vs implicit labels; metadata contents; watermarks encouraged; platform verification (confirmed / declared / suspected); Article 10 anti-tampering; logs of at least 6 months (see PV-65 for article text)
  - Limitations: unofficial translation; China Law Translate's own page not opened
  - Tensions: PV-34; dates
- **PV-34**
  - Title: China releases new labeling requirements for AI-generated content (covers GB 45438-2025)
  - Publisher: Covington & Burling (Inside Privacy)
  - Type: other (law-firm analysis)
  - URL: https://www.covingtonblogs.com/2025/03/18/china-releases-new-labeling-requirements-for-ai-generated-content/
  - Date: 2025-03-18
  - How read: snippet
  - Supports: GB 45438-2025 is a mandatory standard effective 2025-09-01; implicit label contents; platforms add a label when an implicit label is detected
  - Limitations: secondary; standard text not read
  - Tensions: metadata field lists differ across sources
- **PV-35**
  - Title: California AB 853 (2025), amendments to the California AI Transparency Act (SB 942)
  - Type: legislation
  - URL: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853
  - Date: signed 2025-10-13
  - How read: secondary (official legislature site not accessible; content from law-firm alerts and an Assembly analysis via snippets, e.g., https://www.troutmanprivacy.com/2025/10/california-ai-transparency-act-amendments-signed-into-law/ and https://open.pluralpolicy.com/ca/bills/20252026/AB853)
  - Supports: operative date moved to 2 August 2026; large-platform detect / display / no-strip duty from 1 January 2027; capture-device latent-disclosure duty for devices first produced for sale on or after 1 January 2028
  - Limitations: not primary text; user threshold uncertain
  - Tensions: "option" vs "default" for capture devices
- **PV-36**
  - Title: Governor Newsom signs … AI bills (press release listing SB 1000)
  - Publisher: Office of the Governor of California
  - Type: government
  - URL: https://www.gov.ca.gov/2026/09/30/californias-nation-leading-ai-framework-just-got-stronger-governor-newsom-signs-more-first-in-the-nation-worker-protections-and-more/
  - Date: 2026-09-30
  - How read: snippet
  - Supports: SB 1000 (California AI Transparency Act) signed
  - Limitations: SB 1000 content only via secondary summaries; chapter number and effective dates unverified
  - Tensions: one tracker lists it as still in progress (stale)
- **PV-37**
  - Title: Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Amendment Rules, 2026 (G.S.R. 120(E))
  - Publisher: MeitY, India
  - Type: legislation (subordinate rules)
  - URL (secondary entry point): https://blog.ipleaders.in/it-rules-2026/ (also Bar & Bench, https://www.barandbench.com/news/law-policy/centre-amends-it-rules-to-regulate-ai-generated-content-takedown-timelines-reduced; Business Standard, https://business-standard.com/technology/tech-news/it-ministry-shortens-takedown-timelines-intermediaries-ai-content-rules-126021001625_1.html)
  - Date: notified 2026-02-10; in force 2026-02-20
  - How read: secondary. Gazette and PIB text not located; Khaitan & Co analysis read in full (PV-64); the Freshfields analysis was not accessible.
  - Supports: prominent labelling; permanent metadata / unique identifier where technically feasible; no removal; significant-intermediary declarations and verification; 36 h → 3 h and 24 h → 2 h (NCII) takedowns; April 2026 draft on continuous labelling (proposal)
  - Limitations: secondary; trigger wording unverified
  - Tensions: 2-hour scope differs across sources
- **PV-38**
  - Title: NIST AI 100-4, Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency
  - Authors: Bilva Chandra, Jesse Dunietz, Kathleen Roberts, Yooyoung Lee, Peter Fontana, George Awad
  - Publisher: NIST (U.S. AI Safety Institute)
  - Type: government
  - URL: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-4.pdf (publication page: https://www.nist.gov/publications/reducing-risks-posed-synthetic-content-overview-technical-approaches-digital-content; DOI https://doi.org/10.6028/NIST.AI.100-4)
  - Date: 2024-11-20 (publication page updated 2026-04-08)
  - How read: publication page and abstract read; the 81-page PDF text was not readable
  - Supports: authors; date; DOI; scope (provenance and authentication; labelling including watermarking; detection; "preventing generative AI (GAI) from producing child sexual abuse material" or NCII of real people; testing; auditing)
  - Limitations: the report's conclusions on limits were not read; it predates the 2025–2026 developments
  - Tensions: none
- **PV-39**
  - Title: More ways to spot, shape and understand AI content
  - Publisher: TikTok Newsroom
  - Type: platform documentation / marketing
  - URL: https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en
  - Date: 2025-11-19
  - How read: full
  - Supports: invisible watermarking in "testing" on 19 November 2025, to cover TikTok-tool AI content (e.g., AI Editor Pro) and C2PA uploads "over the coming weeks"; a watermark "that only we can read"; called "robust"; labels "may be removed when content is reuploaded or edited elsewhere"; continues reading C2PA on upload; over 1.3 billion videos labelled to date
  - Limitations: vendor claims; no robustness data; the phrase "difficult to remove" came from secondary coverage, not this post
  - Tensions: PV-17 and PV-18 labelling rates
- **PV-40**
  - Title: Helping people spot and understand AI-generated content on TikTok
  - Publisher: TikTok Newsroom
  - Type: platform documentation / marketing
  - URL: https://newsroom.tiktok.com/helping-people-spot-and-understand-ai-generated-content-on-tiktok?lang=en-GB
  - Date: 2026-07-10
  - How read: full
  - Supports: "over 3 billion videos" labelled AIGC via Content Credentials, creator labels and invisible watermarking; "the first video platform to implement C2PA Content Credentials" two years earlier; testing improved detection of AI-spam accounts; says nothing about attaching C2PA to downloads
  - Limitations: vendor counts; no denominator or accuracy
  - Tensions: PV-18 (about 1/3 labelled)
- **PV-41**
  - Title: YouTube will now automatically label AI-generated videos, whether creators disclose them or not
  - Publisher: The Next Web
  - Type: journalism
  - URL: https://thenextweb.com/news/youtube-will-now-automatically-label-ai-generated-videos-whether-creators-disclose-them-or-not
  - Date: late May 2026 (exact date not captured)
  - How read: snippet (not accessible)
  - Supports: automatic detection from May 2026; labels locked for Google-AI or C2PA content; placement below player
  - Limitations: secondary; YouTube's primary post not read
  - Tensions: SynthID role unclear
- **PV-42**
  - Title: Camera Authenticity Solution
  - Publisher: Sony
  - Type: vendor documentation
  - URL: https://authenticity.sony.net/camera/en-us/
  - Date: undated
  - How read: snippet
  - Supports: video limits (no 8K, no bitrates above 222 Mbps, no S&Q); 3D depth detection; signature alone cannot confirm authenticity; default certificate does not guarantee validity
  - Limitations: snippet only
  - Tensions: none
- **PV-43**
  - Title: Sony Is the First Camera Company to Verify Authenticity of Video Content
  - Publisher: PetaPixel
  - Type: journalism
  - URL: https://petapixel.com/2025/10/30/sony-is-the-first-camera-company-to-verify-authenticity-of-video-content
  - Date: 2025-10-30
  - How read: snippet
  - Supports: video C2PA on a1 II, a9 III, FX3, FX30, PXW-Z300
  - Limitations: snippet
  - Tensions: none
- **PV-44**
  - Title: Canon Introduces C2PA-Compliant Authenticity Imaging System for News Organisations
  - Publisher: Canon Europe
  - Type: vendor marketing
  - URL: https://www.canon.co.uk/press-centre/press-releases/2026/05/canon-introduces-c2pa-compliant-authenticity-imaging-system-for-news-organisations/
  - Date: May 2026 (snippet says 11 May)
  - How read: snippet (not accessible)
  - Supports: news-organisation system; paid activation
  - Limitations: model list unverified
  - Tensions: 2 vs 9 models across sources
- **PV-45**
  - Title: Samsung's Galaxy S25 will support Content Credentials to identify AI-generated images
  - Publisher: TechCrunch
  - Type: journalism
  - URL: https://techcrunch.com/2025/01/22/samsung-unpacked-samsungs-galaxy-s25-will-support-content-credentials-to-identify-ai-generated-images
  - Date: 2025-01-22
  - How read: snippet
  - Supports: credentials on Galaxy AI edits; visible "AI-generated content" mark
  - Limitations: snippet; may have changed since
  - Tensions: PV-06 approach
- **PV-46**
  - Title: Samsung's Image Authenticity Approach is Backward and It's AI's Fault
  - Publisher: PetaPixel
  - Type: journalism (opinion)
  - URL: https://petapixel.com/2025/02/13/samsungs-image-authenticity-approach-is-backward-and-its-ais-fault
  - Date: 2025-02-13
  - How read: snippet
  - Supports: unedited S25 photos carry no C2PA
  - Limitations: opinion; snippet
  - Tensions: PV-06
- **PV-47**
  - Title: OpenAI pulls the plug on Sora, the viral AI video app that sparked deepfake concerns
  - Publisher: AP (via OPB)
  - Type: journalism
  - URL: https://www.opb.org/article/2026/03/24/openai-pulls-the-plug-on-sora-the-viral-ai-video-app-that-sparked-deepfake-concerns
  - Date: 2026-03-24
  - How read: snippet
  - Supports: shutdown announcement on 24 March 2026
  - Limitations: snippet only; the OPB copy was not found
  - Tensions: none
- **PV-48**
  - Title: OpenAI sets two-stage Sora shutdown with app closing April 2026 and API following in September
  - Author: Matthias Bastian (The Decoder)
  - Type: journalism
  - URL: https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/
  - Date: 2026-03-28
  - How read: full
  - Supports: Sora web and app closed 2026-04-26; API 2026-09-24; users urged to export before the cutoffs, with data deleted afterwards; Sora continues as a research project focused on world models. It cites OpenAI's help page (https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation), which was not accessible to me.
  - Limitations: secondary to OpenAI's notice; does NOT confirm the earlier snippet claim that Sora 2 remains in ChatGPT
  - Tensions: that snippet claim (now marked unverified)
- **PV-49**
  - Title: Reverse-SynthID coverage
  - Publisher: Gigazine
  - Type: journalism
  - URL: https://www.gigazine.net/gsc_news/en/20260413-reverse-synthid
  - Date: 2026-04-13
  - How read: snippet; the underlying project was deliberately not opened
  - Supports: claimed 90% detection and 91% "watermark energy" removal in Gemini images; Google disputes
  - Limitations: unverified single-developer claim; not peer-reviewed
  - Tensions: PV-10
- **PV-50**
  - Title: Elon Musk Announces 'Manipulated Media' Label on X Images
  - Publisher: PetaPixel
  - Type: journalism
  - URL: https://petapixel.com/2026/01/29/elon-musk-announces-mainipulated-media-label-on-x-images
  - Date: 2026-01-29
  - How read: snippet
  - Supports: "Stay informed: Manipulated media" label; unclear criteria; no C2PA link established
  - Limitations: no official X policy read
  - Tensions: informal test of a "Made with AI" label
- **PV-51**
  - Title: Meta is changing its "Made with AI" tag to "AI Info"
  - Publisher: TechCrunch
  - Type: journalism
  - URL: https://techcrunch.com/?p=2803646
  - Date: 2024 (exact date not captured)
  - How read: snippet
  - Supports: label rename; same underlying C2PA/IPTC-based detection
  - Limitations: dated; snippet; 2026 Meta changes unverified
  - Tensions: PV-18 (meta.ai outputs lack credentials)
- **PV-52**
  - Title: ISO/CD 22144, Authenticity of information — Content credentials
  - Publisher: ISO
  - Type: standards body
  - URL: https://www.iso.org/standard/90726.html
  - Date: undated catalogue page
  - How read: snippet (not accessible)
  - Supports: under development
  - Limitations: stage unresolved (CD vs DIS)
  - Tensions: secondary sources describe a DIS fast-track
- **PV-53**
  - Title: IPTC NewsCodes, Digital Source Type
  - Publisher: IPTC
  - Type: standards body
  - URL: https://cv.iptc.org/newscodes/digitalsourcetype/ (concept: https://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia)
  - Date: undated (composite concept created 2023-07-26)
  - How read: snippet (not accessible)
  - Supports: definitions of `trainedAlgorithmicMedia` and `compositeWithTrainedAlgorithmicMedia`
  - Limitations: full term list not read
  - Tensions: none
- **PV-54**
  - Title: Verify Google AI videos in the Gemini app
  - Publisher: Google
  - Type: vendor documentation / marketing
  - URL: https://blog.google/technology/ai/verify-google-ai-videos-gemini-app/
  - Date: 2025-12-18
  - How read: snippet
  - Supports: video and audio SynthID checks; segment-level results; 100 MB / 90 s limits
  - Limitations: snippet; one hands-on report said checks were unreliable at launch (unverified)
  - Tensions: none
- **PV-55**
  - Title: AI disclosure on social media: a work in progress
  - Publisher: IPTC
  - Type: NGO / standards body news
  - URL: https://iptc.org/news/ai-disclosure-on-social-media-a-work-in-progress/
  - Date: 2026 (not captured)
  - How read: snippet
  - Supports: LinkedIn, Pinterest and YouTube correctly labelled all OpenAI-generated content in Indicator's audit
  - Limitations: secondary summary of PV-18
  - Tensions: none
- **PV-56**
  - Title: IPTC Photo Metadata Conference 2025, C2PA presentation
  - Publisher: IPTC
  - Type: standards body (slides)
  - URL: https://iptc.org/download/events/phmdc2025/IPTC-PHMDC-2025-Brendan_Quinn-C2PA.pdf
  - Date: 2025 (not captured)
  - How read: snippet
  - Supports: Interim Trust List frozen 2026-01-01
  - Limitations: slides; snippet
  - Tensions: none
- **PV-57**
  - Title: Is This Image AI? We Checked 1,331 Web Images for Content Credentials After the EU AI Act Deadline
  - Publisher: ProofSnap
  - Type: vendor marketing / informal evaluation
  - URL: https://getproofsnap.com/posts/c2pa-content-credentials-study-2026.html
  - Date: November 2026
  - How read: snippet
  - Supports: 3 of 1,331 images (~0.2%) had credentials; only 1 still matched
  - Limitations: vendor; internal inconsistencies; small sample
  - Tensions: PV-25
- **PV-58**
  - Title: Fujifilm to Bring C2PA Content Authenticity to X and GFX Cameras
  - Publisher: PetaPixel
  - Type: journalism
  - URL: https://petapixel.com/2024/05/15/fujifilm-to-bring-c2pa-content-authenticity-to-x-and-gfx-cameras
  - Date: 2024-05-15
  - How read: snippet
  - Supports: Fujifilm C2PA plans, no timing
  - Limitations: dated; current status unverified
  - Tensions: none
- **PV-59**
  - Title: YouTube adds label for authentic content to increase AI transparency
  - Publisher: Silicon Republic
  - Type: journalism
  - URL: https://siliconrepublic.com/?p=1097014
  - Date: October 2024 (not captured exactly)
  - How read: snippet
  - Supports: "Captured with a camera" label in "How this content was made"; requires C2PA 2.1+ capture
  - Limitations: snippet; dated
  - Tensions: none
- **PV-60**
  - Title: C2PA adoption status (tracker)
  - Publisher: imgkey (unknown operator)
  - Type: other (low-quality tracker)
  - URL: https://imgkey-com.pages.dev/c2pa-adoption-status/
  - Date: undated
  - How read: snippet
  - Supports: Leica M11-P (October 2023) as first C2PA camera
  - Limitations: low reliability; unverified
  - Tensions: none
- **PV-61**
  - Title: Nikon cameras and C2PA
  - Publisher: c2paviewer.com
  - Type: vendor-affiliated site
  - URL: https://c2paviewer.com/articles/nikon-cameras-c2pa
  - Date: updated 2026-02-27 (a related snippet says May 2026)
  - How read: snippet
  - Supports: claim that Nikon's service had not been restored as of May 2026 (unverified)
  - Limitations: vendor-affiliated; unverified
  - Tensions: none
- **PV-62**
  - Title: CDT comment on NIST AI 100-4 (draft)
  - Publisher: Center for Democracy & Technology
  - Type: NGO
  - URL: https://cdt.org/wp-content/uploads/2024/06/5.31.24-CDT-Comment-on-NIST-AI-100-4.pdf
  - Date: 2024-05-31
  - How read: snippet
  - Supports: watermarking most effective for images but removable; text watermarking far less effective; labelling "will not be a cure-all"
  - Limitations: comment on the draft, not the final report
  - Tensions: none
- **PV-63**
  - Title: Major platforms are not labeling AI-generated videos
  - Author: Fred Ritchin (Substack, Notes of a MetaPhotographer)
  - Type: other (newsletter reproducing journalism)
  - URL: https://fredritchin.substack.com/p/major-platforms-are-not-labeling
  - Date: 2025-10-28
  - How read: full
  - Supports: reproduces the Washington Post test (byline Kevin Schaul): eight platforms tested; "No platform that The Post tested kept the Content Credentials data on the video or let users access it"; only YouTube added a warning, "hidden from view inside a description attached to the clip", reading "Altered or synthetic content"
  - Limitations: partial reproduction; names only YouTube, Facebook and TikTok; does not name the generator; the commentary is the author's opinion
  - Tensions: the AIID summary (PV-19) names Sora and all eight platforms
- **PV-64**
  - Title: MeitY notifies the IT Amendment Rules 2026
  - Authors: Harsh Walia, Ishan Johri, Supratim Chakraborty, Tanu Banerjee (Khaitan & Co)
  - Type: other (law-firm analysis)
  - URL: https://www.khaitanco.com/thought-leadership/MeitY-notifies-the-IT-Amendment-Rules-2026
  - Date: 2026-02-16
  - How read: full
  - Supports:
    - In force 20 February 2026, with 10 days to implement.
    - Definition of synthetic information ("real, authentic or true"; "indistinguishable") and its exclusions.
    - Visual labels must be "prominent, easily noticeable, and adequately perceivable"; audio gets a prefixed disclosure.
    - Significant social media intermediaries must obtain declarations and "deploy appropriate technical measures, including automated tools or other suitable mechanisms".
    - Takedowns: orders 36 h → 3 h; non-consensual nudity or morphed imagery, including deepfake pornography, 24 h → 2 h.
    - Grievances: 15 days → 7 days; 72 h → 36 h; nudity and CSAM 24 h → 2 h.
    - The draft's 10% surface-area watermark rule was replaced.
  - Limitations: secondary analysis; no notification number; silent on the metadata / unique-identifier duty
  - Tensions: other summaries (PV-37) report a permanent metadata / unique-identifier duty
- **PV-65**
  - Title: Measures for Labeling of AI-Generated Synthetic Content (AGORA entry reproducing China Law Translate's unofficial translation)
  - Publisher: Emerging Technology Observatory (AGORA)
  - Type: legislation (unofficial translation, reproduced)
  - URL: https://agora.eto.tech/instrument/2096
  - Date: enacted 2025-03-07; effective 2025-09-01
  - How read: full
  - Supports:
    - Article 3 definitions of explicit and implicit labels.
    - Article 5: metadata must carry the provider "name or code, and the content reference number"; "Service providers are encouraged to add implicit labels" such as watermarks.
    - Article 6: platform checks and notices for confirmed, declared or suspected content.
    - Article 9: logs kept "for at least 6 months".
    - Article 10: users must declare; labels "must not be maliciously deleted, altered, fabricated, or concealed".
    - Article 11: mandatory national standards apply.
    - Article 14: effective 1 September 2025.
  - Limitations: unofficial translation, read via a reproduction
  - Tensions: secondary sources give 14 March 2025 as the release date
- **PV-66**
  - Title: Building trust on YouTube: 'Captured with a camera' disclosure
  - Publisher: YouTube Help (Google)
  - Type: platform documentation
  - URL: https://support.google.com/youtube/answer/15446725?hl=en
  - Date: undated (©2026)
  - How read: full
  - Supports:
    - Where the label appears.
    - Capture requires C2PA 2.1+ tools; "The content must also not have edits to sound or visuals"; edits that break provenance disqualify.
    - "If it's missing, it doesn't mean the content has modified audio or visuals".
    - "separate from our existing altered and synthetic disclosures".
    - Acknowledges "air-gapping" (filming a screen showing synthetic content), and that camera makers' detection measures may vary in sophistication.
  - Limitations: vendor documentation; no usage figures
  - Tensions: none
- **PV-67**
  - Title: Samsung US Newsroom (Galaxy S25 launch material)
  - Publisher: Samsung Electronics America
  - Type: vendor marketing
  - URL: https://news.samsung.com/us/?p=77233
  - Date: January 2025 (not captured)
  - How read: snippet (page not accessible)
  - Supports: S25 described as "the industry's first smartphone lineup to support Content Credentials"; Samsung joined the C2PA; a visible watermark is overlaid on AI-generated output when saved
  - Limitations: not read; the exact page the snippet came from is uncertain
  - Tensions: none

## DS: Detector science and failure modes (sources)

All entries accessed 2026-11-18.

**DS-01**
- **Title:** Deepfake-Eval-2024: A Multi-Modal In-the-Wild Benchmark of Deepfakes Circulated in 2024
- **Author/publisher:** N. A. Chandra, H. Lee, R. Murtfeldt, L. Qiu, A. Karmakar, E. Tanumihardja, K. Farhat, B. Caffee, C. Lee, J. Choi, S. Paik, A. Kim, O. Etzioni (TrueMedia.org-affiliated)
- **Type:** preprint
- **URL:** https://arxiv.org/html/2503.02857
- **Date:** benchmark release 4 Mar 2025; version read v5, dated 27 May 2026
- **How read:** full text (final appendix portion unread)
- **Supports:**
  - composition: video 45.1 h (1,072 real / 964 fake), audio 56.5 h (1,110 / 710), images 1,975 (767 / 1,208); 88 domains; 52 languages
  - open-source AUCs: GenConViT 0.63 / FTCN 0.50 / StyleFlow 0.51 (originally 0.96 / 0.87 / 0.95); AASIST 0.43 / RawNet2 0.53 / P3 0.58 (originally 1.00 / 0.99 / 1.00); UFD 0.56 / DistilDIRE 0.52 / NPR 0.53 (originally 0.94 / 0.99 / 0.98)
  - average AUC drops of 50% / 48% / 45%
  - best commercial: video acc 0.78 / AUC 0.79; audio 0.89 / 0.93; image 0.82 / 0.90 (precision 0.99, recall 0.71)
  - "no commercial models … 90% or above"
  - failure modes: diffusion video −21.3%; selective-face −31%; non-facial −17.4%; text overlays −9%; audio failure points
  - multimodal AVF 0.58, FGI 0.42
- **Limitations:**
  - submissions to a detection service, so a selection effect
  - labels by the authors' analysts
  - commercial vendors anonymised
  - small image set
  - internal table inconsistencies
  - authors ran a detection service (potential interest)
- **Tensions:** DS-25 (fine-tuning results); DS-05 (optimistic out-of-distribution numbers); DS-11 (human vs machine framing)

**DS-02**
- **Title:** A Sanity Check for AI-generated Image Detection (Chameleon dataset; AIDE)
- **Author/publisher:** S. Yan, O. Li, J. Cai, Y. Hao, X. Jiang, Y. Hu, W. Xie (USTC, Xiaohongshu, SJTU)
- **Type:** preprint (reported as ICLR 2025; venue not shown on the version read)
- **URL:** https://arxiv.org/html/2406.19435
- **Date:** v1 June 2024; v3 15 Feb 2025
- **How read:** full text
- **Supports:**
  - Chameleon: 11,170 AI images, each judged real by both annotators, and 14,863 real images
  - all detectors 53.8–65.8% overall accuracy; accuracy on fakes mostly 0–27%
  - AIDE: 92.77% on AIGCDetectBenchmark, 86.88% on GenImage, 58.37–65.77% on Chameleon
  - "almost all models misclassify AI-generated images as real ones"
- **Limitations:**
  - sources skew to AI-art communities (ArtStation, Civitai, Liblib) versus Unsplash photos
  - class balance (57.1% real) inflates overall accuracy
  - the scraped table's column mapping needs caution
- **Tensions:** DS-05

**DS-03**
- **Title:** GenImage: A Million-Scale Benchmark for Detecting AI-Generated Image
- **Author/publisher:** M. Zhu et al.
- **Type:** peer-reviewed (NeurIPS 2023 Datasets & Benchmarks)
- **URL:** https://ar5iv.labs.arxiv.org/html/2306.08571
- **Date:** arXiv June 2023; NeurIPS Dec 2023
- **How read:** full text (ar5iv)
- **Supports:**
  - 1,331,167 real / 1,350,000 fake images; 8 generators
  - cross-generator table (e.g., ResNet-50 99.9 → 52.0–61.9 on non-similar generators)
  - degradation table (JPEG q=65 → 51.9–55.6% for backbones; CNNSpot 97.3%)
  - "Midjourney poses the greatest challenge"
- **Limitations:**
  - generators now outdated (SD 1.4/1.5, Midjourney v5-era, BigGAN)
  - JPEG/PNG and size biases (DS-04)
  - "Avg" column includes in-distribution
- **Currency flag:** superseded as a measure of current-generator difficulty
- **Tensions:** DS-04; DS-05

**DS-04**
- **Title:** Fake or JPEG? Revealing Common Biases in Generated Image Detection Datasets
- **Author/publisher:** P. Grommelt et al.
- **Type:** preprint
- **URL:** https://arxiv.org/html/2403.17608
- **Date:** 2024 (v2)
- **How read:** full text (HTML)
- **Supports:**
  - GenImage reals are JPEG (QF ≈ 96) while fakes are PNG; fixed fake sizes
  - JPEG-compressed fakes get pushed to "natural"; a BigGAN detector called all JPEG95 fakes natural
  - real PNG called natural only 80.45% vs 100% at JPEG60
  - removing the size bias: ResNet-50 71.68 → 82.74%, Swin-T 74.09 → 85.83%
  - JPEG-96 training: +13.26 / +8.75 / +4.49 points at JPEG95 / 80 / 60
- **Limitations:** focuses on GenImage; venue not confirmed
- **Tensions:** DS-03 (CNNSpot's JPEG robustness)

**DS-05**
- **Title:** Community Forensics: Using Thousands of Generators to Train Fake Image Detectors
- **Author/publisher:** J. Park, A. Owens
- **Type:** preprint (reported as CVPR 2025; not confirmed on the page)
- **URL:** https://arxiv.org/html/2411.04125
- **Date:** v1 Nov 2024; v2 9 Jun 2025
- **How read:** full text (Table 2 not legible)
- **Supports:**
  - 4,803 generators; 2.7M generated images
  - evaluation: 26K images from 21 unseen generators (incl. DALL·E 2/3, Ideogram, Midjourney, Firefly, FLUX.1, Imagen 3)
  - 0.987 mAP / 89.2% accuracy
  - scaling plateaus beyond ~1,000 generators; 1,000 random generators beat 10 popular ones
  - authors: "not intend[ed] … to train classifiers that are directly used in the wild"; error rates "still too high for many critical applications"
- **Limitations:** no in-the-wild or re-shared evaluation; per-method numbers not extractable
- **Tensions:** DS-01, DS-02

**DS-06**
- **Title:** Real-Time Deepfake Detection in the Real-World (LaDeDa, Tiny-LaDeDa, WildRF)
- **Author/publisher:** B. Cavia, E. Horwitz, T. Reiss, Y. Hoshen
- **Type:** preprint
- **URL:** https://arxiv.org/html/2406.09398
- **Date:** 13 Jun 2024
- **How read:** full text
- **Supports:**
  - WildRF (Reddit, X, Facebook; about 5,000 images) collected via hashtags
  - LaDeDa 85.7% acc / 93.7% AP on WildRF when trained on Reddit; 68.3% / 79.9% when trained on ProGAN; 92.7% / 98.9% on academic benchmarks
  - "reliable real-world deepfake detection is still unsolved"
- **Limitations:**
  - hashtag-based labels (possible label noise)
  - small X and Facebook splits
  - table and text count mismatch
- **Tensions:** none major

**DS-07**
- **Title:** TrueFake: A Real World Case Dataset of Last Generation Fake Images also Shared on Social Networks
- **Author/publisher:** S. Dell'Anna, A. Montibeller, G. Boato (Univ. Trento; Boato also Truebees srl)
- **Type:** preprint (repo labelled IJCNN25; unconfirmed)
- **URL:** https://arxiv.org/html/2504.20658
- **Date:** 29 Apr 2025
- **How read:** full text
- **Supports:**
  - 600k images, including 180k shared via Facebook, X and Telegram
  - platform resize and JPEG parameters
  - non-shared average TPR 0.60 (NPR) to 0.93 (CLIP-D)
  - after Facebook: NPR's TPR on StyleGAN2 1.00 → 0.00; P2G's TPR → 0.11; CLIP-D's TNR on FFHQ → 0.79
  - "Facebook appears to be the most disruptive social network"
- **Limitations:**
  - faces are FFHQ/GAN-heavy
  - no training on shared images
  - TPR/TNR rather than AUC
  - one author has a company affiliation (possible conflict of interest)
- **Tensions:** DS-03 (format robustness)

**DS-08**
- **Title:** DeMamba: AI-Generated Video Detection on Million-Scale GenVideo Benchmark
- **Author/publisher:** H. Chen et al.
- **Type:** preprint
- **URL:** https://arxiv.org/html/2405.19707
- **Date:** v1 May 2024; v3 22 Aug 2024
- **How read:** most of the text (final portion not read)
- **Supports:**
  - GenVideo: about 1.08M generated / 1.22M real videos (inconsistent totals within the paper)
  - DeMamba-XCLIP-FT on unseen generators: recall 0.939 / F1 0.902 / AP 0.971
  - Sora (56 clips): AP 0.933, F1 0.647
  - degradations: CRF 28 → 0.960; JPEG → 0.763; crop → 0.672
- **Limitations:**
  - 2024-era generators
  - tiny Sora set
  - no AUC reported
- **Currency flag:** pre-dates Sora 2 / Veo 3
- **Tensions:** DS-09 (in-the-wild video collapse)

**DS-09**
- **Title:** Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systematic Evaluation of Detectors, Generators and Social Dissemination (RA-Bench)
- **Author/publisher:** S. Liang, Y. Ma, P. Zhou et al. (36 authors; last author W. Zhao)
- **Type:** preprint
- **URL:** https://arxiv.org/html/2608.14391
- **Date:** v1 14 Aug 2026; v2 17 Aug 2026
- **How read:** full text (appendix tail unread)
- **Supports:**
  - nine generators (Wan2.2, Wan2.2 Light, LTX, Omni Weaver; Happy Horse, Runway, Kling, Seedance 2.0, Hailuo)
  - traditional detectors: reference AUC 67.6–98.6% → 50.9–57.3% (open-source) and 43.9–54.0% (closed-source)
  - mean FPR at 95% TPR 83.1–91.8%
  - best zero-shot multimodal LLM (Gemini-3.1-Pro): 63.4 balanced accuracy
  - LastMile dissemination: fine-tuned models' fake recall 46.0% → 1.4%; balanced accuracy 59.5% → 47.1%; traditional mean AUC 51.4% → 47.3%; TPR at 5% FPR 5.7% → 2.8%; Spearman 0.07
  - humans: 60.3% fake recall; 22.8% of real judged generated; closed-source 52.9%; Seedance 2.0 40.7%; Kling 45.1%; 633 "HumanProof" videos
- **Limitations:**
  - preprint
  - Sora 2 / Veo 3 not included
  - simulated (not actual) platform dissemination
  - reviewer backgrounds not described
  - internal inconsistency on judgments per video
  - "snapshot of a rapidly changing field"
- **Tensions:** DS-10 (human accuracy); DS-08 (video detector optimism)

**DS-10**
- **Title:** VideoASMR-Bench: Can AI-Generated ASMR Videos Fool VLMs and Humans?
- **Author/publisher:** J. Wang, W. Wu, Y. Zhan, R. Zhao, M. Hu, J. Cheng, W. Liu, P. Torr, K. Q. Lin
- **Type:** preprint
- **URL:** https://arxiv.org/html/2512.13281
- **Date:** v1 15 Dec 2025; v4 7 May 2026
- **How read:** full text
- **Supports:**
  - generators include Veo 3.1-Fast, Sora 2, Wan2.2, Open-Sora V2, HunyuanVideo, StepVideo
  - vision-language-model accuracy: Gemini-3-Pro 76.27%, GPT-5 67.14%, GPT-4o 60.22%
  - bias to "real" (up to ~71% of fakes called real; GPT-5 called 88 of 99 Veo clips real)
  - watermark removal cuts detection ~30 points (95.4 → 53.4)
  - audio adds ~5 points
  - 10 humans: 87.5% (Veo 3.1-Fast 81.25%, Sora 2 91.25%)
- **Limitations:**
  - tiny, expert-heavy human sample
  - niche ASMR genre
  - inconsistent model counts and accuracy figures
- **Tensions:** DS-09, DS-22, DS-23 on human accuracy

**DS-11**
- **Title:** FaceForensics++: Learning to Detect Manipulated Facial Images
- **Author/publisher:** A. Rössler, D. Cozzolino, L. Verdoliva, C. Riess, J. Thies, M. Nießner
- **Type:** peer-reviewed (ICCV 2019)
- **URL:** https://ar5iv.labs.arxiv.org/html/1901.08971
- **Date:** arXiv Jan 2019; ICCV Oct 2019
- **How read:** full text (ar5iv)
- **Supports:**
  - raw / c23 / c40 accuracies (XceptionNet 99.26 / 95.73 / 81.00; steganalysis 97.63 / 70.97 / 55.98; etc.)
  - H.264 quantization 23 / 40
  - humans (n = 204, mostly CS students) 68.69 / 66.57 / 58.73%
- **Limitations:** 2019 face manipulations (Deepfakes, Face2Face, FaceSwap, NeuralTextures); in-distribution evaluation
- **Currency flag:** foundational; outdated as a measure of current difficulty
- **Tensions:** DS-01 (in-the-wild collapse); DS-17 (human vs machine)

**DS-12**
- **Title:** Evading Deepfake-Image Detectors with White- and Black-Box Attacks
- **Author/publisher:** N. Carlini, H. Farid
- **Type:** peer-reviewed (CVPR Workshops 2020)
- **URL:** https://ar5iv.labs.arxiv.org/html/2004.00622
- **Date:** arXiv Apr 2020
- **How read:** full text (ar5iv)
- **Supports:**
  - baseline AUC 0.97
  - ℓ0 attack: 2% of pixels → 71.3% misclassified; 4% → 89.7%
  - lowest-bit flip on 1% of pixels → half of fakes missed
  - patch → AUC 0.085; latent attack → 0.17; transfer attack → 0.22
  - real → fake with lowest-bit flips on ~7% of pixels for half of real images
  - "false sense of security … may be worse than if they were not deployed at all"
- **Limitations:** attacks 2020 GAN-image detectors; the abstract's 0.0005 figure is not in the body
- **Currency flag:** principle current; magnitudes dated
- **Tensions:** none

**DS-13**
- **Title:** Robustness of AI-Image Detectors: Fundamental Limits and Practical Attacks
- **Author/publisher:** M. Saberi, V. S. Sadasivan, K. Rezaei, A. Kumar, A. Chegini, W. Wang, S. Feizi
- **Type:** peer-reviewed (ICLR 2024)
- **URL:** https://arxiv.org/html/2310.00076
- **Date:** arXiv 30 Sep 2023; ICLR May 2024
- **How read:** most of the text (final portion not read)
- **Supports:**
  - evasion–spoofing trade-off theorem (Wasserstein)
  - robustness–reliability AUROC bound for classifiers
  - diffusion purification beats low-perturbation watermarks (AUROC < 0.65)
  - TreeRing AUROC 0.14 at ε = 2/255 under model substitution; StegaStamp ~12/255
  - spoofing attack works
- **Limitations:**
  - "robustness" for deepfake classifiers tested against random latent noise
  - exact evasion and spoofing rates mostly in plots
- **Tensions:** DS-32 (possibility arguments); DS-27 (defender asymmetry)

**DS-14**
- **Title:** TGIF: Text-Guided Inpainting Forgery Dataset (and Benchmark)
- **Author/publisher:** H. Mareen, D. Karageorgiou, G. Van Wallendael, P. Lambert, S. Papadopoulos
- **Type:** preprint (venue not shown; believed WIFS 2024)
- **URL:** https://arxiv.org/html/2407.11566
- **Date:** v1 Jul 2024; v2 4 Oct 2024
- **How read:** full text
- **Supports:**
  - about 75k inpainted images (SD2, SDXL, Adobe Firefly)
  - localization F1 on spliced 0.79–0.87 vs ≤ 0.19 on fully regenerated
  - synthetic-image detection AUC up to 0.94–1.00 on fully regenerated, but no localization
  - compression collapses both (e.g., CAT-Net 0.87 → 0.05–0.13; PatchCraft 0.98 → 0.59–0.66)
- **Limitations:** 2023–24 inpainting models; synthetic masks
- **Tensions:** none

**DS-15**
- **Title:** High-quality deepfakes have a heart!
- **Author/publisher:** C. Seibold, E. L. Wisotzky, A. Beckmann, B. Kossack, A. Hilsmann, P. Eisert (Fraunhofer HHI; HU Berlin)
- **Type:** peer-reviewed (Frontiers in Imaging, vol. 4)
- **URL:** https://www.frontiersin.org/journals/imaging/articles/10.3389/fimag.2025.1504551/full
- **Date:** 30 Apr 2025
- **How read:** most of the text (final portion not read)
- **Supports:**
  - heart rate in fakes correlates with the driver video (median r 0.89 DeepFaceLive; 0.55 Beckmann)
  - HR error 1.80 bpm genuine vs 1.85 / 3.24 bpm fakes
  - SNR −1.97 vs −3.35 dB
  - preliminary local-rPPG AUROC 87.4%
  - "global HR … no longer sufficient"
- **Limitations:**
  - 12 subjects, studio conditions
  - limited ground truth
  - FakeCatcher not tested directly
- **Tensions:** premise of rPPG detectors (vendor claims unverified)

**DS-16**
- **Title:** AI-synthesized faces are indistinguishable from real faces and more trustworthy
- **Author/publisher:** S. J. Nightingale, H. Farid
- **Type:** peer-reviewed (PNAS)
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8872790
- **Date:** published 14 Feb 2022
- **How read:** full text (PMC)
- **Supports:**
  - Experiment 1: 48.2% (CI 47.1–49.2), n = 315
  - Experiment 2: 59.0% with training and feedback, n = 219, no learning across the session
  - trustworthiness 4.82 vs 4.48 (+7.7%), n = 223
  - White synthetic faces hardest
- **Limitations:** StyleGAN2 faces only (2020-era); single-face crops
- **Currency flag:** foundational; generators superseded
- **Tensions:** DS-20 (higher accuracy on portraits in 2024 quiz)

**DS-17**
- **Title:** Deepfake detection by human crowds, machines, and machine-informed crowds
- **Author/publisher:** M. Groh, Z. Epstein, C. Firestone, R. Picard
- **Type:** peer-reviewed (PNAS 2022, vol. 119 no. 1); read as the arXiv preprint
- **URL:** https://ar5iv.labs.arxiv.org/html/2105.06496
- **Date:** arXiv May 2021; PNAS Jan 2022
- **How read:** full text of the preprint (published version not compared)
- **Supports:**
  - 15,016 participants
  - model 65% on the 4,000-video DFDC holdout (80% on the 50-video sample)
  - 82% of Experiment 1 participants beat the model
  - crowds 76–86%
  - model advice: 66% → 73%; harmful when wrong (Kim Jong-un 56% → 34%; Putin 70% → 55%)
  - inversion −4 to −6 points; dark skin −8.8 points
- **Limitations:** DFDC (2019–20) videos; preprint numbers may differ slightly from PNAS
- **Currency flag:** dated stimuli
- **Tensions:** DS-11 (machines beat humans)

**DS-18**
- **Title:** Fooled twice: People cannot detect deepfakes but think they can
- **Author/publisher:** N. C. Köbis, B. Doležalová, I. Soraperra
- **Type:** peer-reviewed (iScience 24(11))
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8602050
- **Date:** published 19 Nov 2021
- **How read:** full text (PMC)
- **Supports:**
  - N = 210; 57.6% accuracy; d′ 0.484
  - 67.4% "authentic" responses; bias c 0.518
  - no effect of awareness or incentives (p = 0.759)
  - confidence exceeded accuracy on 13 of 16 videos
  - overconfidence vs accuracy r = −0.475
- **Limitations:** 16 older deepfake videos; mostly UK Prolific sample
- **Currency flag:** dated stimuli
- **Tensions:** DS-20, DS-09 (bias direction)

**DS-19**
- **Title:** A Representative Study on Human Detection of Artificially Generated Media Across Countries
- **Author/publisher:** J. Frank et al.
- **Type:** peer-reviewed (IEEE S&P 2024, per background knowledge; read as the arXiv preprint)
- **URL:** https://arxiv.org/html/2312.05976
- **Date:** arXiv Dec 2023; S&P May 2024
- **How read:** most of the text (final portion not read)
- **Supports:**
  - 2,609 analysed participants (US 822, Germany 875, China 912)
  - image accuracy 48.58 / 45.90 / 49.93%; audio 50.57–59.15%; text 51.50–54.48%
  - machine images rated human more often than real ones (US, Germany)
  - "almost indistinguishable"
- **Limitations:**
  - StyleGAN2, Tacotron 2 and GPT-3 (dated)
  - representativeness quotas not fully met
  - no confidence measures
- **Currency flag:** generators superseded
- **Tensions:** DS-20 (62% in 2024 quiz)

**DS-20**
- **Title:** How good are humans at detecting AI-generated images? Learnings from an experiment
- **Author/publisher:** T. Roca, A. Cintron Roman, J. Torres Vega, M. Duarte, P. Wang, K. White, A. Misra, J. Lavista Ferres (Microsoft AI for Good Lab)
- **Type:** preprint (vendor-affiliated research)
- **URL:** https://arxiv.org/html/2507.18640v1
- **Date:** arXiv July 2025 (paper dated 12 May 2025; data 1–8 Aug 2024)
- **How read:** full text
- **Supports:**
  - about 12,500 participants; about 287,000 judgments
  - 62% overall; 63% on AI images (121,735 / 193,779)
  - hardest items real (12.6% for a real photo of US troops in Afghanistan)
  - GAN faces and inpaintings below 50%
  - in-house detector ">95%" (self-report)
- **Limitations:**
  - self-selected game players
  - not cherry-picked, but not designed for generator comparison
  - real-image accuracy not reported (my estimate)
  - Microsoft has commercial interest in detection tools
- **Tensions:** DS-16, DS-19 (higher accuracy); DS-18 (bias direction)

**DS-21**
- **Title:** Human performance in detecting deepfakes: A systematic review and meta-analysis of 56 papers
- **Author/publisher:** A. Diel et al.
- **Type:** peer-reviewed (Computers in Human Behavior Reports 16:100538)
- **URL:** https://doi.org/10.1016/j.chbr.2024.100538 (DOAJ record: https://doaj.org/article/a2803c8a1b9441458f000fd0fe82ea47)
- **Date:** Dec 2024
- **How read:** secondary — abstract excerpts via search snippets only (full text not accessible)
- **Supports:**
  - pooled 55.54% [48.87, 62.10], k = 67; 86,155 participants; 137 effects
  - audio 62.08% [38.23, 83.18]; video ~57%; images ~53%; text ~52%
  - odds-ratio analysis: 0.64 [0.52, 0.79], "39% detection accuracy"
  - interventions 65.14% [55.21, 74.46] (k = 15)
- **Limitations:**
  - not read in full
  - heterogeneous studies
  - citation discrepancy in one secondary listing
- **Tensions:** DS-10 (high human accuracy)

**DS-22**
- **Title:** Perceptual Judgments of Video Authenticity: An Examination of Viewing Duration, Confidence, Content, and Strategies
- **Author/publisher:** C. Davodi, S. Barrington, H. Farid, E. Cooper (UC Berkeley)
- **Type:** peer-reviewed workshop paper (CVPR 2026 Workshops)
- **URL:** https://farid.berkeley.edu/downloads/publications/cvprw26a.pdf (poster: https://farid.berkeley.edu/downloads/publications/cvprw26a-poster.pdf)
- **Date:** 2026 (CVPR 2026, June)
- **How read:** secondary — search-result excerpts of the poster and abstract (full text not accessible)
- **Supports:**
  - 376 US participants; 480 stimuli (Veo 3.1, Sora 2, Seedance Pro 1, plus 24 real); 48 trials each
  - AI detection 58% → 75% with duration; real ~60% flat
  - Seedance most detectable, Sora least (reported ~77.8 / 65.7 / 62.0%)
  - viewers "search for violations"
- **Limitations:** unverified details; workshop paper
- **Tensions:** DS-10

**DS-23**
- **Title:** How do people watch AI-generated videos of physical scenes?
- **Author/publisher:** D. Shi, L. Jiang, K. M. Collins, S. Wu, A. Tewari, M. Zilka (Cambridge, MIT)
- **Type:** preprint (possibly published in Scientific Reports 2026 as "Perceived authenticity drives gaze behavior…"; unconfirmed)
- **URL:** https://arxiv.org/html/2602.03374
- **Date:** v1 Feb 2026; v2 11 May 2026
- **How read:** full text
- **Supports:**
  - 40 participants; 80 videos (40 real, 40 Veo 3.1)
  - 66.4% accuracy (70.8% physics set; 62.0% professional set); 36 of 40 above chance
  - error shares 18.1% (AI judged real) / 15.5% (real judged AI)
  - gaze follows perceived, not actual, authenticity
- **Limitations:** small sample; 5-second clips; lab setting
- **Tensions:** DS-10

**DS-24**
- **Title:** The Deepfake Detection Challenge (DFDC) Preview Dataset
- **Author/publisher:** B. Dolhansky, R. Howes, B. Pflaum, N. Baram, C. Canton Ferrer (Facebook AI)
- **Type:** preprint
- **URL:** https://ar5iv.labs.arxiv.org/html/1910.08854
- **Date:** Oct 2019
- **How read:** full text (ar5iv)
- **Supports:**
  - prevalence in organic traffic is "much lower" than in datasets
  - "precision is paramount for very-rare detection problems"
  - wP = TP / (TP + α·FP); α ≈ 4·10⁷ estimated, α = 100 used
  - baseline precision and recall (e.g., XceptionNet-face 0.930 / 0.084)
- **Limitations:** 2019; preview dataset; platform (vendor) authorship
- **Currency flag:** old but still the clearest explicit base-rate source
- **Tensions:** none

**DS-25**
- **Title:** Revisiting Simple Baselines for In-The-Wild Deepfake Detection
- **Author/publisher:** O. Castaneda, K. So-Tang, K. Gurung (Georgia Tech)
- **Type:** preprint
- **URL:** https://arxiv.org/html/2509.04150v1
- **Date:** 4 Sep 2025
- **How read:** full text
- **Supports:**
  - fully fine-tuned ViT-b32 / ConvNeXt-base 0.81 accuracy; ResNet-50 0.79; ConvNeXt AUC 0.89
  - >30% of fakes caught at zero false positives
  - no-skill baseline 0.61; prior open-source best 0.69; commercial leader 0.82
- **Limitations:**
  - small dataset (validation set 116 images)
  - images only
  - "fake" includes edits
- **Tensions:** DS-01 (fine-tuning gains)

**DS-26**
- **Title:** AMMeBa: A Large-Scale Survey and Dataset of Media-Based Misinformation In-The-Wild
- **Author/publisher:** N. Dufour et al. (Google)
- **Type:** preprint
- **URL:** https://arxiv.org/html/2405.11697
- **Date:** May 2024 (data through 18 Nov 2023)
- **How read:** most of the text (final portion not read)
- **Supports:**
  - about 135.8k fact-checked claims; ~80% involve media; video >60% of media claims
  - context manipulations dominate; content manipulations least prevalent
  - AI images rare until spring 2023, then rapid rise
- **Limitations:**
  - English fact checks only (selection by fact-checkers)
  - ends Nov 2023
  - no exact AI shares in text
  - platform (vendor) authorship
- **Currency flag:** pre-dates Veo 3 / Sora 2
- **Tensions:** none

**DS-27**
- **Title:** Semantic Forensics (SemaFor) program page
- **Author/publisher:** DARPA
- **Type:** government
- **URL:** https://www.darpa.mil/research/programs/semantic-forensics
- **Date:** undated ("program is now complete")
- **How read:** full text
- **Supports:**
  - goals (detect, attribute, characterize)
  - DEF CON 32 demonstrations; analytic catalog; AI FORCE description
  - statistical detection "quickly becoming insufficient"
  - semantic-error defender asymmetry
- **Limitations:** no metrics or outcomes reported
- **Tensions:** DS-13

**DS-28**
- **Title:** Furthering deepfake defenses (news release)
- **Author/publisher:** DARPA
- **Type:** government
- **URL:** https://www.darpa.mil/news/2025/furthering-deepfake-defenses
- **Date:** 5 Mar 2025 (updated 7 Mar 2025)
- **How read:** full text
- **Supports:**
  - SemaFor ended Sep 2024; MediFor began 2016; SemaFor began 2020
  - transition to U.S. government and industry
  - DSRI (UL Research Institutes) cooperative agreement to run AI FORCE, announce results and award grants
- **Limitations:** no performance data
- **Tensions:** none

**DS-29**
- **Title:** AI FORCE challenge pages (Challenges 1–4)
- **Author/publisher:** semanticforensics.com (SemaFor public site; reported as third-party-hosted)
- **Type:** other (government-program site)
- **URL:** https://semanticforensics.com/ai-force/challenge-1 (also /challenge-2, /challenge-3, /challenge-4)
- **Date:** 2024
- **How read:** secondary — search snippets only
- **Supports:**
  - Challenge 1: authentic vs synthetic images
  - Challenge 2: image model attribution (Jun 2024)
  - Challenge 3: talking-head avatar attribution (from Jul 2024)
  - Challenge 4: synthetic audio (from Aug 2024)
- **Limitations:** not read; no results found
- **Tensions:** none

**DS-30**
- **Title:** NIST GenAI program page
- **Author/publisher:** NIST (Information Technology Laboratory)
- **Type:** government
- **URL:** https://ai-challenges.nist.gov/genai
- **Date:** undated (accessed 2026-11-18)
- **How read:** partial (mostly embedded images)
- **Supports:**
  - modalities listed; "Detectors" role
  - only "2026 GenAI Text" challenge listed (20 teams, 9 phases, 3 tracks)
  - unusual wording ("super intelligence"; "Sept. 29, 2026, Executive Order" banner), reported as observed
- **Limitations:** partial read; T2I leaderboard not retrieved
- **Tensions:** DS-31

**DS-31**
- **Title:** 2025 NIST GenAI (Pilot) Evaluation Plan for Image Discriminators; NIST GenAI T2I page
- **Author/publisher:** NIST
- **Type:** government / standards body
- **URL:** https://ai-challenges.nist.gov/pub/GenAI_Image_Discriminators_Evalplan.pdf (T2I page: https://ai-challenges.nist.gov/t2i; publication listing: https://www.nist.gov/publications/2025-nist-genai-pilot-evaluation-plan-image-discriminators)
- **Date:** 2025
- **How read:** secondary — search snippets only
- **Supports:**
  - task definition ("detect if a target image was generated using a Generative AI system or not")
  - metrics: AUC, TPR at fixed FPR, Brier-type
  - T2I discriminator task "coming soon"
- **Limitations:** not read in full; no results found
- **Tensions:** none

**DS-32**
- **Title:** On the Possibilities of AI-Generated Text Detection
- **Author/publisher:** S. Chakraborty, A. S. Bedi, S. Zhu, B. An, D. Manocha, F. Huang (Univ. of Maryland)
- **Type:** preprint (later published as an ICML 2024 position paper, per background knowledge; not confirmed on page)
- **URL:** https://ar5iv.labs.arxiv.org/html/2304.04736
- **Date:** Apr 2023
- **How read:** most of the text (ar5iv; final portion not read)
- **Supports:**
  - multi-sample detectability: n = Ω((1/δ²)·log(1/(1−ε)))
  - restates the Sadasivan et al. bound AUROC ≤ ½ + TV − TV²/2
  - "nearly always feasible, provided multiple samples are collected"
- **Limitations:** text-only framing and experiments; the extension to images is an inference
- **Tensions:** DS-13

**DS-33**
- **Title:** RobustSora: De-Watermarked Benchmark for Robust AI-Generated Video Detection
- **Author/publisher:** (authors not captured)
- **Type:** preprint
- **URL:** https://arxiv.org/abs/2512.10248
- **Date:** Dec 2025
- **How read:** secondary — search snippet only
- **Supports:**
  - 6,500 videos
  - de-watermarking costs ~11–14 points on Sora 2 vs 3–6 points for Pika / Open-Sora 2
- **Limitations:** not read
- **Tensions:** supports DS-10

**DS-34**
- **Title:** CCDF: A Benchmark Dataset for Deepfake Detection in Real-World Surveillance Footage
- **Author/publisher:** (authors not captured)
- **Type:** preprint
- **URL:** https://arxiv.org/html/2610.07939v1
- **Date:** Oct 2026
- **How read:** secondary — search snippet only
- **Supports:**
  - 1,840 videos (1,380 synthetic from Grok Imagine, Veo 3.1, Sora 2)
  - several detectors near chance on the Sora 2 / Veo 3.1 subsets (e.g., D3-Im ~0.47–0.62 AUC; C-Forensics ~0.69–0.75)
- **Limitations:** not read; surveillance-style domain
- **Tensions:** none

**DS-35**
- **Title:** Beyond benchmark accuracy: Evaluating deepfake detection tools for digital forensic admissibility through a systematic review
- **Author/publisher:** (authors not captured)
- **Type:** other (systematic review; venue unknown)
- **URL:** https://www.researchgate.net/publication/405202775_Beyond_benchmark_accuracy_Evaluating_deepfake_detection_tools_for_digital_forensic_admissibility_through_a_systematic_review
- **Date:** undated
- **How read:** secondary — search snippet only
- **Supports:**
  - ~40% of studies reported FPR/FNR; none reported confidence intervals
  - "99 false positives per true positive" at an unstated operating point
- **Limitations:** not read; unverifiable
- **Tensions:** none

## VE: Vendor claims versus independent evidence (sources)

All entries were accessed 2026-11-18. "How read" uses: full text / partial / abstract only / secondary (snippet).

**VE-01: "Deepfake-Eval-2024: A Multi-Modal In-the-Wild Benchmark of Deepfakes Circulated in 2024"**
- **Author/publisher:** N. A. Chandra, H. Lee, R. Murtfeldt, L. Qiu, A. Karmakar, E. Tanumihardja, K. Farhat, B. Caffee, C. Lee, J. Choi, S. Paik, A. Kim, O. Etzioni. Affiliations: TrueMedia.org; University of Washington; AI2; University of Maryland; Chung-Ang University; Georgetown; Miraflow AI.
- **Type:** preprint.
- **URLs:** https://arxiv.org/abs/2503.02857 ; https://arxiv.org/html/2503.02857v5
- **Date:** v1 4 Mar 2025; v5 27 May 2026 (read).
- **How read:** full text.
- **Supports:**
  - Dataset: 45 h video, 56.5 h audio, 1,975 images; 88 sites; 52 languages.
  - AUC drops of 50% / 48% / 45%.
  - Per-model AUC and accuracy.
  - Best commercial: video 0.78 / 0.79, audio 0.89 / 0.93, image 0.82 / 0.90 (S10 0.86).
  - Anonymization quote; ≥90% bar; failure-mode deltas; class counts; labelling rules; access gated until May 2027.
- **Limitations:**
  - Suspicion-selected sample.
  - Commercial results anonymized.
  - 2024 content only.
  - Labels partly use fact-checks, Community Notes and (for audio) detector outputs.
  - Internal table discrepancies.
  - Conflict of interest: TrueMedia.org relied on partner vendors' models.
- **Tensions:** VE-15, VE-19, VE-21, VE-10, VE-33 (headline claims); VE-12/VE-28 (human-expert framing).

**VE-02: "TRIED: Truly Innovative and Effective AI Detection Benchmark, developed by WITNESS"**
- **Author/publisher:** shirin anlen, Zuzanna Wojciak (WITNESS), via arXiv 2504.21489.
- **Type:** NGO report (preprint).
- **URL:** https://arxiv.org/html/2504.21489v2
- **Date:** v2 1 May 2025 (v1 30 Apr 2025).
- **How read:** full text.
- **Supports:**
  - Six pillars.
  - DRRF casework: Myanmar and Ghana false positives; Mexico original photo flagged; crop/resize false negative; inconclusive Philippines, Sudan, Georgia, India, Nigeria, Uganda and Venezuela cases.
  - Rubric items ("performance metrics are accurate and not exaggerated"; communicate uncertainty; document metrics); retirement protocol.
- **Limitations:**
  - Qualitative; no case count; tools unnamed.
  - Advocacy organization.
  - The witness.org launch post was not read: https://www.witness.org/ai-detection-global-benchmark-witness-2/
- **Tensions:** binary high-accuracy vendor framing (VE-15, VE-19, VE-21); launch-date discrepancy.

**VE-03: "Five Real-World Failures Expose Need for Effective Detection of AI-Generated Media"**
- **Author/publisher:** shirin anlen (WITNESS), Tech Policy Press.
- **Type:** NGO perspective in a journalism outlet.
- **URL:** https://techpolicy.press/five-real-world-failures-expose-need-for-effective-detection-of-ai-generated-media
- **Date:** June 26, 2025.
- **How read:** full text.
- **Supports:** Cambodia/Ghana, Sudan, Mexico, Ukraine and Ghana liar's-dividend cases.
- **Limitations:** no statistics; tools unnamed; promotes the author organization's framework.
- **Tensions:** real-time and accuracy marketing (VE-19, VE-20).

**VE-04: "FTC Order Requires Workado to Back Up Artificial Intelligence Detection Claims"**
- **Author/publisher:** US Federal Trade Commission.
- **Type:** government / regulator.
- **URL:** https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-order-requires-workado-back-artificial-intelligence-detection-claims
- **Date:** April 28, 2025.
- **How read:** full text (press release; PDFs not read).
- **Supports:** "98 percent" vs. "just 53 percent" on general-purpose content; academic-only training; order terms; 3-0 vote.
- **Limitations:** text detector; the testing method is not described in the release.
- **Tensions:** unconditioned vendor claims (VE-15, VE-19, VE-21).

**VE-05: "FTC Approves Final Order against Workado, LLC, Which Misrepresented the Accuracy of its Artificial Intelligence Content Detection Product"**
- **Author/publisher:** US Federal Trade Commission.
- **Type:** government / regulator.
- **URL:** https://www.ftc.gov/node/297697
- **Secondary (snippets):**
  - https://advertisinglaw.fkks.com/post/102l358/ftcs-ai-crackdown-continues-workado-ordered-to-drop-unsupported-accuracy-claims
  - https://www.mychesco.com/a/news/national/ftc-finalizes-order-restricting-workados-ai-content-detection-claims/
- **Date:** August 28, 2025.
- **How read:** full text of the FTC page. The secondary sources were snippets only.
- **Supports:**
  - Final approval 3-0 after public comment; two comments answered.
  - No accuracy or efficacy claims without competent and reliable evidence; evidence retention; consumer email; compliance reports.
  - Complaint quote: "trained or fine-tuned to effectively classify only academic content".
- **Limitations:**
  - The page omits the 98% figure, which is in VE-04.
  - "Formerly Content at Scale AI" comes from secondary sources only.
- **Tensions:** none.

**VE-06: "AI Images Detectors Are Being Used to Discredit the Real Horrors of War"**
- **Author/publisher:** Emanuel Maiberg, 404 Media.
- **Type:** journalism.
- **URL:** https://www.404media.co/ai-images-detectors-are-being-used-to-discredit-the-real-horrors-of-war/
- **Date:** Oct 13, 2023.
- **How read:** full text as available (possibly incomplete because of a paywall).
- **Supports:** an authentic photo posted by Israeli official accounts was flagged AI by a free detector; Farid: "the image does not show any signs it was created by AI"; "second level of disinformation".
- **Limitations:** the tool is not named in the article text read; 2023.
- **Tensions:** VE-35 (tool attribution and statements).

**VE-07: Washington Post, "Fooled by AI? These firms sell deepfake detection that's 'REAL 100%.'" (via summaries)**
- **Author/publisher:** Washington Post, summarized by UC Berkeley School of Information and bestofai.com.
- **Type:** journalism (secondary).
- **URLs:**
  - https://www.ischool.berkeley.edu/news/2024/prof-hany-farid-evaluates-new-deepfake-detection-firms-claiming-near-perfect-detection
  - https://bestofai.com/article/fooled-by-ai-these-firms-sell-deepfake-detection-thats-real-100
- **Date:** May 2024 (Berkeley item dated May 12, 2024).
- **How read:** secondary (snippet).
- **Supports:** Farid on four developers claiming near-perfect detection, and start-ups that "grade themselves on a curve"; Deep Media "99%"; "at least five military contracts worth nearly $2 million".
- **Limitations:** original not read.
- **Tensions:** VE-18, VE-25.

**VE-08: Berkeley iSchool item on Farid's comments to the Washington Post about why AI detection tools fail**
- **Author/publisher:** UC Berkeley School of Information.
- **Type:** journalism (secondary).
- **URL:** https://www.ischool.berkeley.edu/news/2024/professor-hany-farid-speaks-washington-post-about-why-ai-detection-tools-can-fail-catch
- **Date:** Aug 15, 2024.
- **How read:** secondary (snippet).
- **Supports:** training data is largely lab-made deepfakes unlike social media.
- **Limitations:** original not read.
- **Tensions:** consistent with VE-01.

**VE-09: TrueMedia.org shutdown and open-source release**
- **Author/publisher:** TrueMedia.org; GeekWire; TrueMedia GitHub organization.
- **Type:** NGO / journalism (secondary).
- **URLs:**
  - https://truemedia.org/post/shutting-down-truemedia (page not found)
  - https://www.truemedia.org/post/open-source-release
  - https://www.geekwire.com/2025/truemedia-org-plans-to-shutter-and-open-source-its-ai-deepfake-detector-etzioni-hints-at-new-startup/
  - https://www.geekwire.com/2025/truemedia-is-back-deepfake-detection-tool-revived-now-managed-by-georgetown-university/
- **Date:** Jan 7, 2025; Jan 14, 2025 (GitHub closed); Jan 27, 2025 (open-source post); revival date unknown.
- **How read:** secondary (snippet).
- **Supports:** sunset of the free detector; unmaintained repositories; mission quote; reported Georgetown revival.
- **Limitations:** primary posts not read.
- **Tensions:** VE-02 durability pillar.

**VE-10: "Intel Introduces Real-Time Deepfake Detector"**
- **Author/publisher:** Intel Newsroom.
- **Type:** vendor marketing.
- **URL:** https://www.intel.com/content/www/us/en/newsroom/news/intel-introduces-real-time-deepfake-detector.html
- **Date:** Nov 14, 2022.
- **How read:** full text.
- **Supports:** "96% accuracy rate"; blood-flow method; milliseconds; 72 streams.
- **Limitations:** no dataset; dated.
- **Tensions:** VE-11.

**VE-11: BBC test of Intel FakeCatcher (via secondary coverage)**
- **Author/publisher:** BBC, via Advanced Television and PetaPixel.
- **Type:** journalism (secondary).
- **URLs:**
  - https://www.advanced-television.com/2023/07/24/bbc-tests-intel-deepfake-detector
  - https://petapixel.com/2023/08/02/deepfake-detection-software-analyzes-a-persons-blood-flow
- **Date:** July 2023 (Advanced Television, July 24, 2023).
- **How read:** secondary (snippet).
- **Supports:** about 12 clips; fakes caught "bar one"; several real videos flagged; "overly cautious"; no audio analysis; pixelation.
- **Limitations:** tiny sample; BBC original not read.
- **Tensions:** VE-10.

**VE-12: Hive, AI-generated content detection page**
- **Author/publisher:** Hive.
- **Type:** vendor marketing.
- **URL:** https://thehive.ai/apis/ai-generated-content-classification
- **Date:** undated (footer © 2026).
- **How read:** full text.
- **Supports:** "industry-leading accuracy"; 2024-study claim citing arXiv 2402.03214; generator updates; DoD partnership mention.
- **Limitations:** no metrics.
- **Tensions:** VE-28 (perturbation weakness, human-plus-machine conclusion); VE-31; VE-01.

**VE-13: Reality Defender homepage**
- **Author/publisher:** Reality Defender.
- **Type:** vendor marketing.
- **URL:** https://www.realitydefender.com/
- **Date:** undated (references Jun 25, 2026 and Apr 2, 2025).
- **How read:** partial.
- **Supports:** no numeric accuracy; Gartner "Market Shaper"; RSA award; "2.4M+" calls; "Keep the final say."
- **Limitations:** marketing.
- **Tensions:** VE-01 (anonymized partner).

**VE-14: Sensity homepage**
- **Author/publisher:** Sensity.
- **Type:** vendor marketing.
- **URL:** https://sensity.ai/
- **Date:** undated.
- **How read:** full text.
- **Supports:** "The Most Accurate Deepfake Detection Solution"; "lower false positives"; "court-ready".
- **Limitations:** no metrics.
- **Tensions:** VE-01.

**VE-15: AI or Not homepage**
- **Author/publisher:** AI or Not (Optic).
- **Type:** vendor marketing.
- **URL:** https://www.aiornot.com/
- **Date:** undated.
- **How read:** full text.
- **Supports:** "98.9% accuracy"; 7M+ checks; 500K+ users; no disclaimers.
- **Limitations:** no conditions.
- **Tensions:** VE-27, VE-28, VE-31, VE-35, VE-01.

**VE-16: Sightengine, "Detect AI-generated images"**
- **Author/publisher:** Sightengine.
- **Type:** vendor marketing.
- **URL:** https://sightengine.com/detect-ai-generated-images
- **Date:** undated.
- **How read:** full text (chart images not readable).
- **Supports:** "highest accuracy" claim citing the 80,000-image study; "covers all major current generators"; caveats on false positives and negatives, new-generator lag, and "no detector is 100% reliable".
- **Limitations:** no metrics in text.
- **Tensions:** VE-29 (dataset size; IT2I collapse); VE-31.

**VE-17: GetReal Security homepage**
- **Author/publisher:** GetReal Security.
- **Type:** vendor marketing.
- **URL:** https://www.getrealsecurity.com/
- **Date:** undated.
- **How read:** full text.
- **Supports:** no figure; "forensic-grade precision and explainability"; method categories (C2PA, provenance, biometrics, and others).
- **Limitations:** nothing measurable.
- **Tensions:** none.

**VE-18: Deep Media homepage**
- **Author/publisher:** Deep Media.
- **Type:** vendor marketing.
- **URL:** https://deepmedia.ai/
- **Date:** undated.
- **How read:** full text.
- **Supports:** no detection-accuracy claim; "Sub-200ms latency"; "80% Lower total cost of ownership …".
- **Limitations:** entity continuity unverified.
- **Tensions:** VE-07, VE-25.

**VE-19: Resemble AI, Detect**
- **Author/publisher:** Resemble AI.
- **Type:** vendor marketing.
- **URL:** https://www.resemble.ai/detect/
- **Date:** undated (references 2026 generators).
- **How read:** full text.
- **Supports:** "Up to 99.5% accuracy"; per-generator 94–>99%; unnamed "#1" benchmark; 54 languages (MLAADv10); "Zero day coverage".
- **Limitations:** no test conditions.
- **Tensions:** VE-01, VE-02.

**VE-20: Pindrop homepage**
- **Author/publisher:** Pindrop.
- **Type:** vendor marketing.
- **URL:** https://www.pindrop.com/
- **Date:** undated (references 2026).
- **How read:** full text.
- **Supports:** no numeric deepfake accuracy; real-time claim; "about two seconds"; "5000+ AI voices"; TIME 2026.
- **Limitations:** audio and meetings focus.
- **Tensions:** VE-33 (earlier "99%"); VE-01.

**VE-21: DuckDuckGoose homepage**
- **Author/publisher:** DuckDuckGoose.
- **Type:** vendor marketing.
- **URL:** https://www.duckduckgoose.ai/
- **Date:** undated (benchmarks labelled Q2 2026).
- **How read:** full text.
- **Supports:** "≈96%"; "95% to 99%"; DFDC 96.5%, FF++ 98.1%, Celeb-DF v2 97.3%; "0.01% FPR … live production traffic".
- **Limitations:**
  - Self-reported; inconsistencies.
  - Background (not re-verified): the cited benchmarks are 2019–2020-era face-swap datasets.
- **Tensions:** VE-01.

**VE-22: Clarity homepage**
- **Author/publisher:** Clarity.
- **Type:** vendor marketing.
- **URL:** https://www.getclarity.ai/
- **Date:** undated.
- **How read:** full text (solution subpage not read).
- **Supports:** no numeric claims; ensemble AI for video interviews.
- **Limitations:** marketing.
- **Tensions:** none.

**VE-23: NIST GenAI Image Discriminators pilot (program pages and evaluation plan)**
- **Author/publisher:** NIST.
- **Type:** standards body / government.
- **URLs:**
  - https://ai-challenges.nist.gov/t2i
  - https://ai-challenges.nist.gov/pub/GenAI_Image_Discriminators_Evalplan.pdf
- **Date:** plan 2025; leaderboard scheduled Apr 10, 2026; workshop May 2026.
- **How read:** secondary (snippet).
- **Supports:** task definition; rules restricting public cross-team comparison; AUC and Brier metrics (text track).
- **Limitations:** no results found.
- **Tensions:** none.

**VE-24: DARPA SemaFor / AI FORCE**
- **Author/publisher:** DARPA; semanticforensics.com.
- **Type:** government.
- **URLs:**
  - https://www.darpa.mil/news/2024/deepfake-defense
  - https://semanticforensics.com/ai-force/challenge-1
- **Date:** 2024.
- **How read:** secondary (snippet).
- **Supports:** AI FORCE open challenges; the third-party site says it is "not a DoD or DARPA website".
- **Limitations:** no results.
- **Tensions:** none.

**VE-25: Deep Media trade profiles**
- **Author/publisher:** TechBrew; Decrypt.
- **Type:** journalism (trade).
- **URLs:**
  - https://www.techbrew.com/stories/2022/08/22/meet-the-company-working-with-the-air-force-to-detect-deepfakes
  - https://decrypt.co/202181/deepfake-detection-deepmedia-ai-government
- **Date:** Aug 22, 2022; Decrypt 2023 (exact date unverified).
- **How read:** secondary (snippet).
- **Supports:** about 95% "across most deepfake modalities"; "won't release until 99%".
- **Limitations:** unverified.
- **Tensions:** VE-07, VE-18.

**VE-26: "FTC Announces Crackdown on Deceptive AI Claims and Schemes" (Operation AI Comply)**
- **Author/publisher:** US Federal Trade Commission.
- **Type:** government / regulator.
- **URL:** https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
- **Date:** Sept 25, 2024.
- **How read:** full text.
- **Supports:** five actions (DoNotPay $193,000, 5-0; Ascend Ecom ≥$25M; Ecommerce Empire Builders; Rytr, 3-2; FBA Machine >$15.9M); Khan quote; **no detector cases**.
- **Limitations:** sweep predates Workado.
- **Tensions:** none.

**VE-27: "Testing AI or Not: How Well Does an AI Image Detector Do Its Job?"**
- **Author/publisher:** Dennis Kovtun, Bellingcat.
- **Type:** journalism / independent test.
- **URL:** https://www.bellingcat.com/resources/how-tos/2023/09/11/testing-ai-or-not-how-well-does-an-ai-image-detector-do-its-job/
- **Date:** Sept 11, 2023.
- **How read:** full text.
- **Supports:**
  - 100/100 uncompressed Midjourney detected.
  - Real images 89/90; contest photos 13/20 (6 false positives).
  - Compressed Midjourney 3/10.
  - Watermarked 10/10.
  - Quotes on compression.
- **Limitations:** 2023 version; Midjourney only; small sample; counts inconsistent; single tool.
- **Tensions:** VE-15.

**VE-28: "Organic or Diffused: Can We Distinguish Human Art from AI-generated Images?"**
- **Author/publisher:** A. Y. J. Ha, J. Passananti, R. Bhaskar, S. Shan, R. Southen, H. Zheng, B. Y. Zhao (University of Chicago; one artist co-author).
- **Type:** peer-reviewed (ACM CCS 2024).
- **URLs:** https://arxiv.org/abs/2402.03214 ; https://arxiv.org/html/2402.03214v3
- **Date:** v1 Feb 5, 2024; v3 Jul 2, 2024; CCS Oct 14–18, 2024.
- **How read:** full text (appendix tail unread).
- **Supports:**
  - Clean ACC/FPR/FNR: Hive 98.03 / 0.00 / 3.17; Optic 90.67 / 24.47 / 1.15; Illuminarty 72.65 / 67.40 / 4.69; ensemble 98.75 / 0.48 / 1.71.
  - Perturbation rates (Hive FNR 32.44% under high Glaze).
  - Human groups: 59.23 / 75.32 / 83.00 accuracy.
  - Hive re-tests in April and June 2024.
  - Human-plus-machine conclusion.
- **Limitations:**
  - Art images, not social-media photos or video.
  - 630 core images.
  - Main query dates not stated.
- **Tensions:** VE-12 (selective citation); VE-15 (AI or Not FPR).

**VE-29: "The Adversarial AI-Art: Understanding, Generation, Detection, and Benchmarking" (ARIA)**
- **Author/publisher:** Y. Li, Z. Liu, J. Zhao, L. Ren, F. Li, J. Luo, B. Luo (University of Kansas; University of Rochester).
- **Type:** preprint.
- **URLs:** https://arxiv.org/abs/2404.14581 ; https://arxiv.org/html/2404.14581v1
- **Date:** Apr 22, 2024 (v1).
- **How read:** full text.
- **Supports:**
  - About 144K images (127,046 AI / 17,129 real; counts inconsistent); 5 categories; 4 generators; T2I and IT2I modes.
  - Commercial accuracies: Sightengine 98.72 real; 95.84–100 T2I; 25.12 and 43.76 on two IT2I subsets; Illuminarty, Is it AI?, Content at Scale and Fake Image Detector figures.
  - User study 65.24% / 68.00%.
- **Limitations:**
  - Accuracy only (no FPR/TPR split).
  - No query dates; default thresholds.
  - Internal count inconsistencies.
- **Tensions:** VE-16 ("80,000 images"; "highest accuracy").

**VE-30: "Our Approach to Labeling AI-Generated Content and Manipulated Media"**
- **Author/publisher:** Meta.
- **Type:** platform documentation.
- **URL:** https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
- **Date:** Apr 5, 2024; updated May 10, Jul 1 and Sept 12, 2024 (header also shows Oct 23, 2025).
- **How read:** full text.
- **Supports:** "Made with AI" → "AI info" (Jul 1, 2024); labels "weren't always aligned with people's expectations"; minor AI retouching example; detection via industry signals and self-disclosure.
- **Limitations:** no error rates; label-effect research is covered in the RC entries.
- **Tensions:** VE-31.

**VE-31: "Leading AI Image Detection Tools Mislead Online Users, Often Declaring Authentic Content Fake"**
- **Author/publisher:** Isis Blachez, Sofia Rubinson, Ines Chomnalez (NewsGuard).
- **Type:** journalism / independent evaluation.
- **URL:** https://www.newsguardtech.com/?p=33448
- **Date:** May 8, 2026.
- **How read:** full text.
- **Supports:**
  - Per-tool results for Hive, AI or Not, ZeroGPT, Sightengine and ScamAI on 15 authentic, 15 lightly retouched and 15 significantly edited images (≥50% threshold; free tiers).
  - 13.33% of authentic images flagged overall.
  - Quotes on consensus and thresholds.
- **Limitations:**
  - n=15 per set.
  - Free tiers only.
  - The light-edit tool is unnamed.
  - NewsGuard is a commercial ratings company, though not a detector vendor.
- **Tensions:** VE-15, VE-12, VE-16.

**VE-32: "AI's blind spot: Tools fail to detect their own fakes"**
- **Author/publisher:** AFP (Ara Eugenio, Purple Romero, Anuj Chopra), republished by RNZ.
- **Type:** journalism.
- **URL:** https://www.rnz.co.nz/news/business/579586/ai-s-blind-spot-tools-fail-to-detect-their-own-fakes
- **Date:** Nov 21, 2025.
- **How read:** full text.
- **Supports:** Google AI mode, Gemini and Copilot called AI images genuine; Tow Center 7/7 chatbots failed on 10 real photos (as reported).
- **Limitations:**
  - Anecdotal cases.
  - Tow Center study seen only as reported.
  - The Copyleaks CEO quoted is a detection vendor (conflict of interest).
- **Tensions:** none.

**VE-33: "Pindrop says it can detect deepfake audio with 99% accuracy"**
- **Author/publisher:** Paul Gillin, SiliconANGLE.
- **Type:** journalism repeating a vendor claim.
- **URL:** https://siliconangle.com/2024/08/15/pindrop-says-can-detect-deepfake-audio-99-accuracy
- **Secondary (snippets):**
  - https://venturebeat.com/ai/pindrop-claims-to-detect-ai-audio-deepfakes-with-99-accuracy
  - https://www.biometricupdate.com/202405/pindrop-claims-up-to-99-accuracy-detecting-synthetic-voice-fraud-plaguing-call-centers
- **Date:** Aug 15, 2024 (Biometric Update, May 2024).
- **How read:** SiliconANGLE full text; others snippet only.
- **Supports:**
  - "99% accuracy"; training on 350+ tools, 20M utterances, 40+ languages; preview launch; no independent evaluation.
  - Snippets: "<1%" FPR; about 200,000-sample internal analysis; "previously unseen deepfakes with 90% accuracy"; warranty.
- **Limitations:** audio; vendor-sourced figures.
- **Tensions:** VE-20 (no figure now); VE-01 (best audio 0.89).

**VE-34: McAfee deepfake-detection accuracy claims**
- **Author/publisher:** McAfee press releases, via search results; Decrypt; AFP via The Star.
- **Type:** vendor marketing (snippets).
- **URLs:**
  - https://www.mcafee.com/en-us/newsroom/press-releases/2024/mcafee-unveils-advanced-deepfake-audio-detection-technology-at-ces-2024-to-defend-against-rise-in-ai-generated-scams-and-disinformation.html
  - https://www.businesswire.com/news/home/20240820483013/en (not accessible)
  - https://decrypt.co/212396/mcafee-claims-its-audio-deepfake-detection-tool-is-90-accurate
  - https://www.mcafee.com/en-us/deepfake-detector.html (not accessible)
- **Date:** Jan 2024; Aug 20, 2024.
- **How read:** secondary (snippet).
- **Supports:** ">90%" (Mockingbird); "96%" (Deepfake Detector on Lenovo AI PCs; analyses audio in videos on device).
- **Limitations:** primary text not read.
- **Tensions:** none found.

**VE-35: Follow-up coverage of the October 2023 war-photo detector verdict**
- **Author/publisher:**
  - The Conversation (via inkl).
  - NYT, syndicated by Deccan Herald ("AI muddies Israel-Hamas war in unexpected way").
  - Check Your Fact ("Post Falsely Claim Image Of Burned Israeli Child Are AI Generated").
  - PetaPixel ("App That Claims to Identify AI Images Embroiled in Israel Hamas Argument").
- **Type:** journalism (secondary).
- **URLs:**
  - https://inkl.com/news/was-this-photo-of-a-dead-israeli-baby-ai-generated-when-ai-detection-errors-muddle-public-debate (not accessible)
  - https://www.deccanherald.com/world/ai-muddies-israel-hamas-war-in-unexpected-way-2746434 (not accessible)
  - https://checkyourfact.com/2023/10/16/fact-check-post-falsely-claim-image-of-burned-israeli-child-are-ai-generated
  - https://petapixel.com/2023/10/17/app-that-claims-to-identify-ai-images-embroiled-in-israel-hamas-argument (not accessible)
- **Date:** Oct 2023 (Check Your Fact Oct 16; PetaPixel Oct 17).
- **How read:** secondary (snippet).
- **Supports:** the tool was AI or Not; the screenshot had more than 21M views; Oct 14 company statement on false positives with "low quality" images; later "inconclusive" due to compression and alteration, with the detector "refined".
- **Limitations:** none read in full.
- **Tensions:** VE-06 (tool unnamed in the text read).

**VE-36: UK ASA guidance on AI and deepfakes in advertising**
- **Author/publisher:** Advertising Standards Authority (UK), plus law-firm summaries.
- **Type:** regulator (snippets).
- **URLs:**
  - https://www.asa.org.uk/news/ai-and-deepfakes-four-things-advertisers-need-to-know-before-they-hit-run.html
  - https://www.lewissilkin.com/insights/2026/06/18/asa-warns-on-ai-generated-content-and-deepfakes-102n4o1
- **Date:** 2026 (law-firm note June 18, 2026; ASA page undated in snippet).
- **How read:** secondary (snippet).
- **Supports:** existing CAP codes apply to AI content and deepfakes; AI-product efficacy and comparative claims need evidence; no detector-accuracy ruling found.
- **Limitations:** not read in full; ASA rulings database not searched.
- **Tensions:** none.

## LG: Legal and evidentiary landscape (sources)

*About 20 entries were read in full or near-full (marked "full text" or "partial"). The rest are labelled "secondary/search summary"; claims resting on them are marked as such.*

**LG-01**
- **Title:** Machine-Generated Evidence: Rules Advisory Committee Hits Pause to Consider Significant Revisions to Proposed Federal Rule of Evidence 707 Addressing Evidence Generated by Artificial Intelligence
- **Publisher:** Redgrave LLP (no named author)
- **Type:** other (law-firm practitioner commentary)
- **URL:** https://www.redgravellp.com/publication/machine-generated-evidence--rules-advisory-committee-hits-pause-to-consider-significant-revisions-to-proposed-federal-rule-of-evidence-707-addressing-evidence-generated-by-artificial-intelligence
- **Date:** July 2026
- **How read:** full text
- **Claims supported:**
  - Rule 707 text as published August 2025, quoted above, including "simple scientific instruments"; hearings 15 and 29 Jan 2026; April 2026 Reporter's memo with seven critiques and three redrafts.
  - 7 May 2026 vote not to advance; Redraft 2 the leading option; fall 2026 mini-conference at the 15 Oct 2026 Boston meeting.
  - 901(c) postponed; two-step structure; FJC survey (more than 930 responding, 15 with deepfake challenges, about one-third and 55% support).
  - Statements by DOJ ("not ready for publication"), Caproni and Sullivan; earliest publication August 2027.
- **Limitations:** secondary account of the agenda book and meeting; no vote counts.
- **Tensions:** "simple" vs "basic"; DOJ remark timing (LG-02).

**LG-02**
- **Title:** Is That Video Real? Federal Judges Weigh a Deepfake Evidence Rule as AI Improves
- **Publisher:** Ron Frey (The Frey Law Firm), InternetCrime.com
- **Type:** journalism / law-firm blog
- **URL:** https://www.internetcrime.com/news/deepfake-evidence-rule-901c/
- **Date:** 15 Oct 2026
- **How read:** full text
- **Claims supported:**
  - OpenAI (Shira Anderson) and Meta (Devin Norder) addressed the committee in Boston on 15 Oct 2026; quote "no universal method exists to reliably detect every watermark or verify every image or video".
  - Chair Furman said deepfakes have been infrequent in cases; draft 901(c) structure, including pretrial notice; carve-out for conceded fabricated images in child-exploitation cases; FJC "15 of 931".
- **Limitations:** relies on Investing.com and an unlinked agenda book; statements paraphrased; no C2PA discussion.
- **Tensions:** DOJ remark timing vs LG-01.

**LG-03**
- **Title:** FTC Begins Enforcing the TAKE IT DOWN Act
- **Publisher:** Federal Trade Commission
- **Type:** government or regulator
- **URL:** https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act
- **Date:** 19 May 2026
- **How read:** full text
- **Claims supported:** "today began enforcing"; §3 deadline 19 May 2026; removal of the image "and known identical copies, within 48 hours of a valid request"; TakeItDown.ftc.gov; Ferguson quote "In the age of AI, anyone can be targeted."
- **Limitations:** press release; no penalties figure.
- **Tensions:** none.

**LG-04**
- **Title:** Complying With the Take It Down Act
- **Publisher:** Federal Trade Commission (business guidance)
- **Type:** government or regulator
- **URL:** https://www.ftc.gov/business-guidance/resources/complying-take-it-down-act
- **Date:** May 2026
- **How read:** full text
- **Claims supported:** covered platforms include "social media, messaging, image or video sharing, and gaming platforms"; digital forgeries described as "images that were digitally created or altered using software, an app, or artificial intelligence"; "reasonable efforts to find and remove known identical copies"; "civil penalties of $53,088 per violation"; people "do not need to report duplicate images".
- **Limitations:** silent on the elements of a valid request, the good-faith safe harbour and false requests.
- **Tensions:** the inclusion of messaging vs the critiques in LG-46 and LG-47.

**LG-05**
- **Title:** FTC Sends Warning Letters to Companies About Compliance with the TAKE IT DOWN Act
- **Publisher:** Federal Trade Commission
- **Type:** government or regulator
- **URL:** https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-sends-warning-letters-companies-about-compliance-take-it-down-act
- **Date:** 20 May 2026
- **How read:** full text
- **Claims supported:** 12 "nudify" companies; "appear to be in violation of TIDA" (no removal process); "immediately come into compliance"; penalties up to $53,088 per violation.
- **Limitations:** company names not given in the summary; letters only, not enforcement actions.
- **Tensions:** none.

**LG-06**
- **Title:** FTC Chairman Ferguson Advises Companies to Comply with the Take It Down Act
- **Publisher:** Federal Trade Commission
- **Type:** government or regulator
- **URL:** https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-chairman-ferguson-advises-companies-comply-take-it-down-act
- **Date:** May 2026
- **How read:** secondary/search summary only
- **Claims supported:** compliance letters to 15 major platforms, including Alphabet, Meta, Apple, Reddit, Snapchat, TikTok and X.
- **Limitations:** not read; exact date unknown.
- **Tensions:** none.

**LG-07**
- **Title:** Public Law 119-12 (TAKE IT DOWN Act)
- **Publisher:** US Congress, via GovInfo
- **Type:** legislation
- **URL:** https://www.govinfo.gov/content/pkg/PLAW-119publ12/html/PLAW-119publ12.htm
- **Date:** enacted 19 May 2025
- **How read:** full text (key provisions extracted; with a targeted re-read of §3/§4 scope and penalties)
- **Claims supported:**
  - Definitions of "digital forgery" and "identifiable individual"; adult offence elements for authentic and forged depictions; 2-year maximum; consent-to-creation rule; exceptions, including legal-proceedings filings.
  - Elements of a §3 request (quoted); 48-hour removal; identical copies; one-year deadline; good-faith immunity "regardless of whether…"; FTC Act §18 enforcement; covered-platform definition and exclusions.
- **Limitations:** the 15 U.S.C. 6851 definition of "intimate visual depiction" was not read; absence of counter-notice inferred from the extracted provisions.
- **Additional provisions read:** §3 covers "an intimate visual depiction published on the covered platform" that "was published without the consent of the identifiable individual"; the definition cross-references §223(h)(1)(E) to 15 U.S.C. 6851; minors up to 3 years (§223(h)(4)(B)); forgery threats up to 18 months for adults and 30 months for minors (§223(h)(6)(B)).
- **Tensions:** LG-46 and LG-47 (over-removal).

**LG-08**
- **Title:** Durbin Successfully Passes Bill To Combat Nonconsensual, Sexually-Explicit Deepfake Images
- **Publisher:** Senate Judiciary Committee (Democrats) / Sen. Durbin
- **Type:** government
- **URL:** https://www.judiciary.senate.gov/press/dem/releases/durbin-successfully-passes-bill-to-combat-nonconsensual-sexually-explicit-deepfake-images
- **Date:** 13 Jan 2026
- **How read:** secondary/search summary
- **Claims supported:** the DEFIANCE Act (S.1837) passed the Senate by unanimous consent on 13 Jan 2026; held at the desk in the House.
- **Limitations:** not read in full; the bill text (congress.gov) was not accessible.
- **Tensions:** none.

**LG-09**
- **Title:** Paris Hilton returns to Capitol to push for House vote on deepfake porn bill
- **Publisher:** CBS News
- **Type:** journalism
- **URL:** https://www.cbsnews.com/news/paris-hilton-alexandria-ocasio-cortez-defiance-act-deepfake-bill/
- **Date:** 17 Nov 2026
- **How read:** secondary/search summary
- **Claims supported:** DEFIANCE stalled in the House; the Speaker's office did not respond; H.R. 3562 led by Reps. Ocasio-Cortez and Laurel Lee.
- **Limitations:** snippet-level.
- **Tensions:** none.

**LG-10**
- **Title:** Court Throws Out Case After Finding Plaintiffs Submitted Deepfake Videos and Altered Images
- **Publisher:** Eugene Volokh, Reason / Volokh Conspiracy
- **Type:** legal scholarship (blog) quoting a court record
- **URL:** https://reason.com/volokh/2025/09/25/court-throws-out-case-after-finding-plaintiffs-submitted-deepfake-videos-and-altered-images/
- **Date:** 25 Sep 2025
- **How read:** full text (order excerpts)
- **Claims supported:** *Mendones* (9 Sep 2025): exhibits 6A and 6C "products of GenAI"; the comparison indicators quoted above; CCP §128.7(b); terminating sanction; criminal referral declined as "too severe"; "Use GenAI in court with great caution."
- **Limitations:** excerpts only; attribution of "zero tolerance" wording uncertain.
- **Tensions:** none.

**LG-11**
- **Title:** Claiming Video Was "Deepfake" Not Enough to Require Excluding It, Even Absent Evidence of Who Recorded It
- **Publisher:** Eugene Volokh, Reason / Volokh Conspiracy
- **Type:** legal scholarship (blog) quoting a court record
- **URL:** https://reason.com/volokh/2026/10/13/claiming-video-was-deepfake-not-enough-to-require-excluding-it-even-absent-evidence-of-who-recorded-it/
- **Date:** 13 Oct 2026
- **How read:** full text
- **Claims supported:** *State v. Amyda* (Iowa Sup. Ct., unanimous, Mansfield J.): "mere speculation…"; "no identifiable circumstances…"; "only conjecture"; Rule 5.901 standard; citations to *Christian Church* (Del. 2025), *Perry* (D.C. 2026) and *M.S.*
- **Limitations:** excerpts; some quoted phrases may be Volokh's paraphrase.
- **Tensions:** *M.S.* (LG-13).

**LG-12**
- **Title:** AI Deepfakes in Court (database)
- **Publisher:** Damien Charlotin
- **Type:** other (research database, CC BY 4.0)
- **URL:** https://www.damiencharlotin.com/deepfakes/
- **Date:** undated; latest entry 15 Oct 2026
- **How read:** full page
- **Claims supported:**
  - 29 cases; country and outcome counts; no UK, Australian or NZ cases.
  - *Mendones* methods (metadata, judicial inspection, admissions).
  - *Burnley*, *Kirkham*, *Demissie*, *Bryan*, *Amyda* (9 Oct 2026), *M.S.* (17 Feb 2026), *Modena*, *Poznań*, *CA Paris*, *CPH Lyon*.
  - *Head v John Doe* "Deepfake Detected" printout given no weight.
- **Limitations:** curator's summaries, not judgments; coverage incomplete.
- **Tensions:** *Head* basis vs LG-16.

**LG-13**
- **Title:** Matter of M.S. (M.H.), 2026 NY Slip Op 00825
- **Publisher:** N.Y. Court of Appeals (opinion); commentary by Pryor Cashman, NYSBA and others
- **Type:** court record (secondary)
- **URL:** https://nycourts.gov/reporter/3dseries/2026/2026_00825.htm; https://www.pryorcashman.com/publications/new-york-court-of-appeals-gives-lawyers-powerful-arguments-to-challenge-admission-of-video-evidence; https://nysba.org/web-post-new-york-state-law-digest-march-2026/
- **Date:** 17 Feb 2026
- **How read:** secondary/search summary (the opinion was not accessible)
- **Claims supported:** *Patterson* standard; videos not authenticated; majority quote "increasing prevalence of 'deepfake' videos … more suspect form of authentication"; Troutman dissent "new and perhaps insurmountable hurdles"; "superficial and simplistic analysis of deepfake technology"; reported 4–3.
- **Limitations:** quotes via secondary sources; vote count disputed.
- **Tensions:** *Amyda*; amNY's "five of seven".

**LG-14**
- **Title:** State v. Puloka, No. 21-1-04851-2 (Wash. Super. Ct. King County), Findings of Fact and Conclusions of Law (Frye)
- **Publisher:** reported by Greenberg Traurig and NBC News
- **Type:** court record (secondary)
- **URL:** https://gtlaw.com/en/insights/2024/5/washington-court-rejects-novel-use-of-ai-enhanced-video-in-trial; https://www.nbcnews.com/news/us-news/washington-state-judge-blocks-use-ai-enhanced-video-evidence-rcna141932
- **Date:** 29 Mar 2024 (ruling); April–May 2024 (reports)
- **How read:** secondary/search summary
- **Claims supported:** AI-enhanced (Topaz) video excluded under Frye; the relevant community is forensic video analysts; about 16x pixel increase; SWGDE caution; commercial adoption not persuasive.
- **Limitations:** judgment not read.
- **Tensions:** none.

**LG-15**
- **Title:** Huang v. Tesla (Santa Clara Super. Ct., 19CV346663), tentative ruling
- **Publisher:** reported by Fortune and Bloomberg Law
- **Type:** court record (secondary) / journalism
- **URL:** https://fortune.com/2023/04/27/elon-musk-lawyers-argue-recordings-of-him-touting-tesla-autopilot-safety-could-be-deepfakes/; https://news.bloomberglaw.com/esg/musk-likely-must-give-deposition-in-fatal-autopilot-crash-suit
- **Date:** 26–27 Apr 2023
- **How read:** secondary/search summary
- **Claims supported:** "deeply troubling"; limited deposition of up to three hours; famous people should not "avoid taking ownership of what they did actually say and do".
- **Limitations:** tentative ruling; the order not read; later history not traced.
- **Tensions:** none.

**LG-16**
- **Title:** Head v John Doe, 2026 BCSC 184 (Canada), as reported
- **Publisher:** IBA, "Authenticating evidence in the age of AI"; Courthouse Libraries BC guide
- **Type:** court record (secondary) / practitioner guidance
- **URL:** https://www.ibanet.org/authenticating-evidence-in-the-age-of-AI; https://www.courthouselibrary.ca/sites/default/files/inline-files/Assessing%20Weight%20of%20Video%20Recording%20Evidence%20in%20the%20Age%20of%20Generative%20AI.pdf
- **Date:** judgment 4 Feb 2026; IBA April 2026
- **How read:** secondary/search summary
- **Claims supported:** deepfake allegation over GoPro footage rejected; online AI tool printout ("Deepfake Detected") given no weight; video admitted; authentication via camera and SD-card custody.
- **Limitations:** outside the five jurisdictions; judgment not read (not accessible).
- **Tensions:** the basis for authentication differs from LG-12.

**LG-17**
- **Title:** Sexual Offences Act 2003, section 66E (Creating purported intimate image of adult)
- **Publisher:** legislation.gov.uk (The National Archives)
- **Type:** legislation
- **URL:** https://www.legislation.gov.uk/ukpga/2003/42/section/66E
- **Date:** in force 6 Feb 2026; page current to 18 Nov 2026
- **How read:** full text
- **Claims supported:**
  - s.66E(1), (2), (4), (5), (6) and (7), quoted above.
  - Annotation: "Ss. 66E-66H inserted (6.2.2026) by Data (Use and Access) Act 2025 … s. 138 … S.I. 2026/31, reg. 2"; no Crime and Policing Act amendments to s.66E itself.
- **Limitations:** maximum summary term depends on other commencement provisions.
- **Tensions:** none.

**LG-18**
- **Title:** Sexual Offences Act 2003, sections 66A, 66B, 66D
- **Publisher:** legislation.gov.uk
- **Type:** legislation
- **URL:** https://www.legislation.gov.uk/ukpga/2003/42/section/66B (also /section/66A and /section/66D)
- **Date:** in force 31 Jan 2024
- **How read:** full text
- **Claims supported:** s.66B(1)–(4) "shows, or appears to show"; s.66B(7) "not necessary for the prosecution to prove" that the image exists for threats; penalties; s.66A(5)(a) "made or altered by computer graphics…"; inserted by OSA 2023 ss.187–188 (SI 2024/31); prospective Crime and Policing Act 2026 amendments.
- **Limitations:** prospective amendment text not shown.
- **Tensions:** contrast with s.66E.

**LG-19**
- **Title:** Crime and Policing Act 2026, Part 5, Chapter 4
- **Publisher:** legislation.gov.uk
- **Type:** legislation
- **URL:** https://www.legislation.gov.uk/ukpga/2026/20/part/5/chapter/4
- **Date:** Royal Assent 29 Apr 2026 (see LG-55)
- **How read:** partial
- **Claims supported:** s.99 (new SOA s.66I–66K) wording and 3-year maximum; s.100 48-hour takedown with declaration-based reports and provider exceptions; commencement 29 Jun 2026 (SI 2026/689); s.102 prospective; s.104 and s.106 6 Nov 2026 (SI 2026/1090).
- **Limitations:** Schedule 13 (taking and recording offences) not read.
- **Tensions:** none.

**LG-20**
- **Title:** Crime and Policing Act 2026: overarching factsheet; Intimate Image Abuse and AI Chatbots: Crime and Policing Act becomes law
- **Publisher:** Home Office / GOV.UK; Wiggin LLP
- **Type:** government; other (law-firm commentary)
- **URL:** https://www.gov.uk/government/publications/crime-and-policing-act-2026-factsheets/crime-and-policing-act-overarching-factsheet; https://www.wiggin.co.uk/insight/intimate-image-abuse-and-ai-chatbots-crime-and-policing-act-becomes-law/
- **Date:** 2026
- **How read:** secondary/search summary (GOV.UK page not accessible)
- **Claims supported:** Royal Assent 29 Apr 2026 (now confirmed by LG-55); description of the nudification-tool offence.
- **Limitations:** snippet-level.
- **Tensions:** none.

**LG-21**
- **Title:** Statement: Detecting intimate image abuse
- **Publisher:** Ofcom
- **Type:** government or regulator
- **URL:** https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/statement-detecting-intimate-image-abuse
- **Date:** 18 May 2026 (per page snippet)
- **How read:** secondary/search summary (not accessible)
- **Claims supported:** hash-matching recommendation; StopNCII-equivalent database; covered services; expected in force "Autumn 2026"; human-review guidance 9 Sep 2026 (via Digital Policy Alert snippet).
- **Limitations:** not read; in-force status unknown.
- **Tensions:** June 2026 date in an Ofcom bulletin.

**LG-22**
- **Title:** Ofcom launches investigation into X over Grok sexualised imagery; Ofcom update: Investigation into X, and scope of the Online Safety Act
- **Publisher:** Ofcom
- **Type:** government or regulator
- **URL:** https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery; https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/investigation-into-x-and-scope-of-the-online-safety-act
- **Date:** 12 Jan 2026 (opening); update undated
- **How read:** secondary/search summary (not accessible)
- **Claims supported:** investigation opened 12 Jan 2026; X measures; "remains ongoing"; inability to investigate standalone Grok image creation; maximum fine £18m or 10%.
- **Limitations:** not read; no outcome found.
- **Tensions:** none.

**LG-23**
- **Title:** Ofcom fines nudification site £50,000 for failing to introduce age-checks
- **Publisher:** Ofcom
- **Type:** government or regulator
- **URL:** https://www.ofcom.org.uk/online-safety/protecting-children/ofcom-fines-nudification-site-50000-for-failing-to-introduce-age-checks
- **Date:** November 2025
- **How read:** secondary/search summary
- **Claims supported:** Itai Tech Ltd (Undress.cc) fined £50,000 for age-assurance failure; information notice issued 24 Jun 2025.
- **Limitations:** age-check enforcement, not intimate image abuse.
- **Tensions:** £55,000 in some outlets.

**LG-24**
- **Title:** Ofcom issues final guidance on protecting women and girls online (A Safer Life Online for Women and Girls)
- **Publisher:** SCL; Mishcon de Reya (reporting Ofcom)
- **Type:** other (practitioner commentary) reporting a regulator
- **URL:** https://www.scl.org/ofcom-issues-final-guidance-on-protecting-women-and-girls-online/; https://www.mishcon.com/news/online-safety-ofcom-publishes-guidance-to-tech-firms-to-tackle-online-harms-against-women-and-girls
- **Date:** 25 Nov 2025
- **How read:** secondary/search summary
- **Claims supported:** non-binding VAWG guidance; hash matching recommended; nudification-app de-listing; plan to consult on mandatory hash matching.
- **Limitations:** Ofcom document not read.
- **Tensions:** Refuge wants it made a binding Code.

**LG-25**
- **Title:** AI and the Judiciary: Updated guidance issued on responsible use of AI by judicial office holders; Deepfakes and the Legal Sector
- **Publisher:** Wiggin LLP; Chronicle Law
- **Type:** other (practitioner commentary) reporting judicial guidance
- **URL:** https://www.wiggin.co.uk/insight/ai-and-the-judiciary-updated-guidance-issued-on-responsible-use-of-artificial-intelligence-by-judicial-office-holders/; https://chroniclelaw.co.uk/blogs/2026/04/09/deepfakes-and-the-legal-sector/
- **Date:** April and October 2025 (guidance); 9 Apr 2026 (Chronicle)
- **How read:** secondary/search summary
- **Claims supported:** the guidance warns "AI tools are now being used to produce fake material, including text, images and video"; judges to watch for litigant AI use.
- **Limitations:** the judiciary.uk text was not read; date of the October update uncertain (1 vs 31 Oct).
- **Tensions:** scope of permitted judicial AI use differs across commentaries.

**LG-26**
- **Title:** Government considers ending "computer is right" rule following Horizon scandal; Victims and Courts Bill, Lords debate
- **Publisher:** Legal Cheek; Parallel Parliament (Hansard mirror)
- **Type:** journalism; government (parliamentary record)
- **URL:** https://www.legalcheek.com/2025/01/government-considers-ending-computer-is-right-rule-following-horizon-scandal; https://www.parallelparliament.co.uk/lord/kevan-jones/debate/2026-03-10/lords/lords-chamber/victims-and-courts-bill
- **Date:** January 2025; 10 Mar 2026
- **How read:** secondary/search summary
- **Claims supported:** MoJ call for evidence on the presumption of computer reliability; the presumption still in place in March 2026; Chakrabarti amendment.
- **Limitations:** no government response found.
- **Tensions:** none.

**LG-27**
- **Title:** Directive (EU) 2024/1385 on combating violence against women and domestic violence (Art. 5)
- **Publisher:** EUR-Lex; EU Monitor; commentary (Oxford ORA, TechPolicy.press)
- **Type:** legislation (secondary read) plus legal scholarship
- **URL:** https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202401385; https://eumonitor.eu/9353000/1/j9vvik7m1c3gyxp/vmdjatjnwez4; https://ora.ox.ac.uk/objects/uuid:2eac4c02-3e4c-4553-bb43-e3584a72ff1c/files/sjd472z87f; https://www.techpolicy.press/eu-moves-to-regulate-ai-nudification-but-key-challenges-remain/
- **Date:** adopted 14 May 2024; OJ 24 May 2024; in force 13 Jun 2024; transposition deadline 14 Jun 2027
- **How read:** full text on EUR-Lex (https://eur-lex.europa.eu/eli/dir/2024/1385/oj/eng), read in full; the commentary pieces are search summaries
- **Claims supported:** Art. 5(1)(a)–(c) and 5(2) wording; recital 19 ("fabrication of 'deepfakes'"); Art. 23 removal and disabling orders; Art. 49 transposition by 14 Jun 2027; Art. 50 entry into force on the twentieth day after publication; adoption and OJ dates; scope critiques (commentary).
- **Limitations:** some Art. 23 wording was read as a paraphrase.
- **Tensions:** nudification-scope gap vs the AI Act ban.

**LG-28**
- **Title:** Regulation (EU) 2024/1689 (AI Act), Art. 50 and Art. 3(60)
- **Publisher:** artificialintelligenceact.eu; Orrick
- **Type:** legislation (secondary read); other (law-firm commentary)
- **URL:** https://artificialintelligenceact.eu/transparency-rules-article-50/; https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50
- **Date:** Act 2024; Art. 50 applies from 2 Aug 2026; Orrick August 2026
- **How read:** full text of Art. 50 and Art. 3(60) via the AI Act Explorer reproduction (https://artificialintelligenceact.eu/article/50/), read; the guide and the Orrick piece are search summaries
- **Claims supported:** Art. 50(2) ("effective, interoperable, robust and reliable as far as this is technically feasible"; "marked in a machine-readable format and detectable as artificially generated or manipulated"); the Art. 50(4) disclosure duty with its law-enforcement and artistic exceptions; Art. 3(60) definition (quoted); application from 2 Aug 2026; the page marks Art. 50(7) as amended; perceivable without tools and no retroactive labelling (commentary).
- **Limitations:** an unofficial reproduction, not the Official Journal.
- **Tensions:** none.

**LG-29**
- **Title:** Digital Omnibus on AI (reported as Regulation (EU) 2026/1744)
- **Publisher:** Bird & Bird; regulation-ai.eu; technology.org; Cooley
- **Type:** other (law-firm and compliance commentary)
- **URL:** https://www.twobirds.com/en/insights/2026/digital-omnibus-on-ai-provisional-agreement-reached-at-the-may-trilogue; https://www.regulation-ai.eu/en/omnibus/; https://www.technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus-what-applies-from-december-2026-to-august-2028/; https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/
- **Date:** May to Oct 2026
- **How read:** secondary/search summary
- **Claims supported:** timeline (7 May, 16 Jun, 29 Jun, OJ 24 Jul, in force 27 Jul 2026); Art. 50 not delayed except the Art. 50(2) grace period to 2 Dec 2026; new Art. 5 NCII and CSAM bans from 2 Dec 2026; three ways the ban can be breached.
- **Limitations:** commentary only. Superseded for text and dates by the EUR-Lex primary text (LG-56), which confirms the number, the 2 Dec 2026 dates and the Art. 50(2) transition.
- **Tensions:** guidance dates (8 May vs 20 Jul) vary across sources.

**LG-30**
- **Title:** Commission publishes Code of Practice on marking and labelling AI-generated content
- **Publisher:** European Commission (DG CONNECT)
- **Type:** government or regulator
- **URL:** https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content
- **Date:** 10 Jun 2026 (updated 12 Jun 2026)
- **How read:** full text (short press page)
- **Claims supported:** voluntary Code; "sets out practical steps"; obligations "will apply from 2 August 2026"; labelling of deepfakes and public-interest text; EU icon.
- **Limitations:** the Code itself not read; no mention of C2PA or reliability limits on the page.
- **Tensions:** none.

**LG-31**
- **Title:** Elon Musk's X probed by EU over sexually explicit images on Grok; EU launches investigation into X over Grok-generated sexual images
- **Publisher:** CNBC; BleepingComputer
- **Type:** journalism
- **URL:** https://www.cnbc.com/2026/01/26/elon-musk-grok-eu-explicit-images-investigation.html; https://www.bleepingcomputer.com/news/artificial-intelligence/eu-launches-investigation-into-x-over-grok-generated-sexual-images/
- **Date:** 26 Jan 2026
- **How read:** secondary/search summary
- **Claims supported:** DSA formal proceedings vs X over Grok risk assessment; retention order; no decision found; separate €120m fine (5 Dec 2025).
- **Limitations:** the Commission release not read.
- **Tensions:** 6 Jan vs 26 Jan opening date.

**LG-32**
- **Title:** Criminal Code Amendment (Deepfake Sexual Material) Act 2024 (No. 78, 2024), Sch. 1; Bills Digest
- **Publisher:** AustLII; Parliamentary Library (APH)
- **Type:** legislation (secondary read); government
- **URL:** https://classic.austlii.edu.au/au/legis/cth/num_act/ccasma2024387/sch1.html; https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/bd/bd2324a/24bd081
- **Date:** assent 2 Sep 2024; commenced 3 Sep 2024
- **How read:** secondary/search summary
- **Claims supported:** s.474.17A substituted; "depicting, or appearing to depict"; irrelevant whether "created, or altered in any way, using technology"; 6 years, aggravated 7 years (s.474.17AA); exceptions; carriage-service scope; minors excluded.
- **Limitations:** exact subsection numbers not verified (official text not accessible; see LG-57).
- **Tensions:** none.

**LG-33**
- **Title:** Court orders $343,500 penalty for posting deepfakes of Australian women
- **Publisher:** eSafety Commissioner
- **Type:** government or regulator
- **URL:** https://www.esafety.gov.au/newsroom/media-releases/court-orders-343500-penalty-for-posting-deepfakes-of-australian-women
- **Date:** 26 Sep 2025
- **How read:** secondary/search summary
- **Claims supported:** *eSafety Commissioner v Rotondo (No 4)* [2025] FCA 1191; A$343,500 plus costs; s.75 breaches and non-compliance with removal notices; first civil penalty under the Online Safety Act.
- **Limitations:** judgment not read.
- **Tensions:** ABC "almost $350,000".

**LG-34**
- **Title:** eSafety takes action against another major 'nudify' service…; Another three 'nudifying' services go dark in Australia
- **Publisher:** eSafety Commissioner; Medianet
- **Type:** government or regulator
- **URL:** https://www.esafety.gov.au/newsroom/media-releases/esafety-takes-action-against-another-major-nudify-service-for-failing-to-protect-australian-children; https://newshub.medianet.com.au/2026/06/another-three-nudifying-services-go-dark-in-australia-as-regulatory-pressure-mounts-over-child-safety-concerns/159353/
- **Date:** May 2026; June 2026
- **How read:** secondary/search summary
- **Claims supported:** enforcement against nudify services; services withdrawing; the seven most-used services withdrawn or complied (reported).
- **Limitations:** the legal basis for each action not extracted.
- **Tensions:** none.

**LG-35**
- **Title:** Online Safety Amendment (Digital Duty of Care) Bill 2026
- **Publisher:** Parliament of Australia; Lexology
- **Type:** legislation (bill); other (law-firm commentary)
- **URL:** https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7553; https://www.lexology.com/library/detail.aspx?g=f0234b27-125f-48ce-b825-56bef48905ad
- **Date:** October–November 2026
- **How read:** secondary/search summary
- **Claims supported:** Part 6A (s.86B) nudify takedown via app stores and search; House passed with amendments 28 Oct 2026 (Lexology); Senate committee report due 20 Nov 2026.
- **Limitations:** status as of 18 Nov 2026 unconfirmed.
- **Tensions:** conflicting introduction dates.

**LG-36**
- **Title:** Image-Based Abuse Scheme Regulatory Guidance (Jan 2025); Sharing school imagery in the age of AI
- **Publisher:** eSafety Commissioner
- **Type:** government or regulator
- **URL:** https://esafety.gov.au/sites/default/files/2025-01/IBA-Scheme-Regulatory-Guidance-Jan2025_2.pdf; https://www.esafety.gov.au/newsroom/blogs/sharing-school-imagery-in-the-age-of-ai-risks-deepfakes-and-how-to-protect-students-and-staff
- **Date:** January 2025; 2026
- **How read:** secondary/search summary
- **Claims supported:** intimate image = image or video that "shows, or appears to show" (s.15); image-based abuse includes "fake or altered" images; 24-hour removal notices (secondary).
- **Limitations:** the s.15 text itself not read.
- **Tensions:** section-number conflicts in secondary sources.

**LG-37**
- **Title:** Deepfake bill passes first reading in Parliament; ACT release; ACT MP says deepfake bill a 'first step'
- **Publisher:** RNZ; ACT Party via Scoop
- **Type:** journalism; government/political
- **URL:** https://www.rnz.co.nz/news/politics/595813/deepfake-bill-passes-first-reading-in-parliament; https://www.scoop.co.nz/stories/PA2605/S00169/deepfake-bill-passes-first-reading-now-its-time-for-kiwis-to-have-their-say.htm; https://www.rnz.co.nz/news/politics/768470/act-mp-says-deepfake-bill-a-first-step-in-ai-regulation
- **Date:** 20 May 2026; 22 Jul 2026
- **How read:** secondary/search summary
- **Claims supported:** unanimous first reading on 20 May 2026; Social Services and Community Committee; "created, synthesised or altered" expansion of s.216G and the HDCA; McClure before the committee on 22 Jul 2026.
- **Limitations:** the bill text not read (not accessible; see LG-58).
- **Tensions:** ballot date; WhereTheyStand out of date.

**LG-38**
- **Title:** Submissions on the Deepfake Digital Harm and Exploitation Bill (Privacy Commissioner; InternetNZ); TLANZ commentary
- **Publisher:** Office of the Privacy Commissioner; InternetNZ; LawNews
- **Type:** government; NGO; journalism
- **URL:** https://www.privacy.org.nz/assets/DOCUMENTS/Submissions/2026-06-19-OPC-Submission-on-Deepfake-Digital-Harm-and-Exploitation-Bill-A1196216-A1199351.pdf; https://internetnz.nz/assets/Archives/Submissions/InternetNZs-Deepfake-Digital-Harm-and-Exploitation-Bill-Submission.pdf; https://lawnews.nz/criminal/deepfake-bill-wont-hold-nudify-platforms-to-account-says-tlanz-committee/
- **Date:** 19 Jun 2026; 17 Jun 2026; 2026
- **How read:** secondary/search summary
- **Claims supported:** the bill at select committee in June 2026; the Privacy Commissioner supports passage; the criticism that nudify platforms are not covered.
- **Limitations:** submissions not read.
- **Tensions:** none.

**LG-39**
- **Title:** Understanding Deep Fakes; The Harmful Digital Communications Act
- **Publisher:** Netsafe
- **Type:** NGO (approved agency under statute)
- **URL:** https://netsafe.org.nz/online-abuse-and-harassment/understanding-deep-fakes; https://netsafe.org.nz/our-work/helpline-services/the-harmful-digital-communications-act
- **Date:** undated
- **How read:** secondary/search summary
- **Claims supported:** Netsafe is the approved agency; the HDCA covers AI images "if they cause or are likely to cause harm"; Netsafe advocates amending s.22A.
- **Limitations:** pages not read in full.
- **Tensions:** commentators (Spinoff, Newsroom) say "intimate visual recording" excludes synthetic images.

**LG-40**
- **Title:** Guidelines for use of generative artificial intelligence in Courts and Tribunals
- **Publisher:** Courts of New Zealand (Office of the Chief Justice)
- **Type:** government (judiciary)
- **URL:** https://courtsofnz.govt.nz/going-to-court/practice-directions/practice-guidelines/all-benches/guidelines-for-use-of-generative-artificial-intelligence-in-courts-and-tribunals
- **Date:** 7 Dec 2023
- **How read:** secondary/search summary
- **Claims supported:** three sets of guidelines; deepfake-awareness wording for judges and lawyers; RNZ (19 Feb 2026) report on a committee discussing notice periods for AI-origin challenges.
- **Limitations:** guidelines not read; any update after 2023 unknown.
- **Tensions:** none.

**LG-41**
- **Title:** Court Protocols on AI (NSW Supreme Court Practice Note SC Gen 23)
- **Publisher:** Law Society of NSW
- **Type:** other (professional body) reporting a court practice note
- **URL:** https://lawsociety.com.au/court-protocols-ai
- **Date:** PN issued 21 Nov 2024, revised 28 Jan 2025
- **How read:** secondary/search summary
- **Claims supported:** generative AI prohibited in evidence and expert reports absent leave in "exceptional circumstances"; no deepfake-specific provisions found.
- **Limitations:** practice note not read.
- **Tensions:** none.

**LG-42**
- **Title:** Judicial Approaches to Acknowledged and Unacknowledged AI-Generated Evidence
- **Authors:** Maura R. Grossman & Paul W. Grimm, Columbia Science & Technology Law Review, vol. 26(2)
- **Type:** legal scholarship
- **URL:** https://journals.library.columbia.edu/index.php/stlr/article/view/13890
- **Date:** 2025
- **How read:** abstract only (via search summaries)
- **Claims supported:** acknowledged vs unacknowledged distinction; existing rules can cope if applied flexibly; proposes new rules.
- **Limitations:** full text not read.
- **Tensions:** the committee's caution (LG-01).

**LG-43**
- **Title:** Deepfakes in Court: How Judges Can Proactively Manage Alleged AI-Generated Material in National Security Cases
- **Authors:** Daniel W. Linna Jr., Abhishek Dalal, Chongyang Gao, Paul W. Grimm, Maura R. Grossman, Chiara Pulice, V.S. Subrahmanian, Hon. John Tunheim (U. Chi. Legal Forum)
- **Type:** legal scholarship
- **URL:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4943841
- **Date:** 2024 (SSRN); published 2025
- **How read:** abstract only
- **Claims supported:** detection tools "have proven unreliable and biased"; humans are poor at distinguishing real from fake.
- **Limitations:** abstract-level.
- **Tensions:** practitioner reliance on detectors (LG-52).

**LG-44**
- **Title:** Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security
- **Authors:** Robert Chesney & Danielle K. Citron, 107 Calif. L. Rev. 1753
- **Type:** legal scholarship
- **URL:** https://law.utexas.edu/faculty/publications/2019-deep-fakes-a-looming-challenge-for-privacy-democracy-and-national-security/
- **Date:** 2019 (SSRN 2018)
- **How read:** secondary (table of contents and summaries)
- **Claims supported:** the "Liar's Dividend" concept and section title; growing awareness of deepfakes lets liars dismiss authentic evidence.
- **Limitations:** the authors' exact definition not quoted.
- **Tensions:** none.

**LG-45**
- **Title:** 86% fake – 100% admissible? Rethinking evidence in the AI era
- **Publisher:** Kennedys
- **Type:** other (law-firm commentary)
- **URL:** https://www.kennedyslaw.com/en/thought-leadership/article/2026/86-fake-100-admissible-rethinking-evidence-in-the-ai-era/
- **Date:** 2026
- **How read:** secondary/search summary (not accessible)
- **Claims supported:** detector probability scores can be mistaken for proof; a proprietary detector with a confidence score and no audit trail is challengeable under Rule 702; reinforce FRE 901 and 104 gatekeeping.
- **Limitations:** not read; authors unknown.
- **Tensions:** none.

**LG-46**
- **Title:** Concerns Regarding the TAKE IT DOWN Act (coalition sign-on letter)
- **Publisher:** Center for Democracy & Technology et al.
- **Type:** NGO
- **URL:** https://cdt.org/wp-content/uploads/2025/02/TAKE-IT-DOWN-Sign-On-Letter_21225.pdf
- **Date:** 12 Feb 2025
- **How read:** secondary/search summary
- **Claims supported:** over-breadth ("speech that is neither illegal nor actually NDII"); encryption quote; request to exclude encrypted services.
- **Limitations:** pre-enactment; not read in full.
- **Tensions:** the statute and FTC guidance (LG-04, LG-07).

**LG-47**
- **Title:** A Takedown of the Take It Down Act
- **Author:** Eric Goldman, Technology & Marketing Law Blog
- **Type:** legal scholarship (blog)
- **URL:** https://blog.ericgoldman.org/archives/2025/06/a-takedown-of-the-take-it-down-act.htm
- **Date:** June 2025
- **How read:** secondary/search summary
- **Claims supported:** over-removal incentive; "many erroneous removals"; no exemption for messaging or encrypted services.
- **Limitations:** not read in full.
- **Tensions:** FTC guidance silent on errors.

**LG-48**
- **Title:** C2PA in a Court of Law
- **Publisher:** Hacker Factor Blog (Neal Krawetz)
- **Type:** other (technical blog)
- **URL:** https://hackerfactor.com/blog/index.php?/archives/1080-C2PA-in-a-Court-of-Law.html
- **Date:** undated
- **How read:** secondary/search summary
- **Claims supported:** C2PA does not protect EXIF/XMP, so may not qualify for FRE 902(13)/(14) self-authentication; falls back to Rule 901.
- **Limitations:** opinion, not law; not read in full.
- **Tensions:** other commentary suggests a FRE 901(b)(9) route.

**LG-49**
- **Title:** California Revamps AI Transparency Requirements; California AI Transparency Act amendments signed into law
- **Publisher:** Morrison & Foerster; Troutman Pepper Locke
- **Type:** other (law-firm commentary) on legislation
- **URL:** https://www.mofo.com/resources/insights/261001-california-revamps-ai-transparency-requirements; https://www.troutmanprivacy.com/2025/10/california-ai-transparency-act-amendments-signed-into-law/
- **Date:** 1 Oct 2026; October 2025
- **How read:** secondary/search summary
- **Claims supported:** operative 2 Aug 2026; latent provenance disclosures; AB 853 platform and capture-device duties phased through 2028; SB 1000 (2026) reported.
- **Limitations:** statute not read; SB 1000 from a single source.
- **Tensions:** none.

**LG-50**
- **Title:** State deepfake-law trackers (aggregators citing Ballotpedia)
- **Publisher:** e.g., lawsignals.com, ailawsbystate.com, stackcyber.com, recordinglaw.com
- **Type:** other (aggregators)
- **URL:** https://lawsignals.com/ai-legislation/deepfake-laws; https://www.ailawsbystate.com/blog/deepfake-laws-by-state-2026
- **Date:** 2026
- **How read:** secondary/search summary
- **Claims supported:** about 46–48 states with sexual-deepfake laws ("all except Ohio and New Mexico" as of 5 Aug 2026, per Ballotpedia); some states minors-only.
- **Limitations:** the specific page for the "48" figure could not be pinned; low reliability.
- **Tensions:** counts of 46, 48 and 49.

**LG-51**
- **Title:** Formal Comment – Machine-Generated Evidence (FRE 707)
- **Publisher:** American Association for Justice
- **Type:** NGO (professional association)
- **URL:** https://www.justice.org/advocacy/legal-affairs/federal-rules/fc---fre-707
- **Date:** comment period August 2025 to 16 Feb 2026
- **How read:** secondary/search summary
- **Claims supported:** AAJ urged a pause and redraft; the rule is overbroad; suggested narrowing to ML/AI systems.
- **Limitations:** not read.
- **Tensions:** none.

**LG-52**
- **Title:** When the Image Is Fake but the Harm Is Real: Children's Rights in the Age of AI-Generated Sexual Exploitation
- **Publisher:** American Bar Association, Litigation Section (Children's Rights newsletter)
- **Type:** NGO / professional body
- **URL:** https://www.americanbar.org/groups/litigation/resources/newsletters/childrens-rights/when-image-is-fake-harm-real/
- **Date:** undated (2025–26)
- **How read:** secondary/search summary
- **Claims supported:** synthetic-CSAM prosecutions rely on expert testimony involving metadata, AI detection tools, provenance and forensics.
- **Limitations:** not read.
- **Tensions:** LG-02 and LG-43 on detector reliability.

**LG-53**
- **Title:** Advisory Committee on Evidence Rules — Agenda Book, May 7, 2026
- **Publisher:** Administrative Office of the US Courts
- **Type:** government (court rule-making record)
- **URL:** https://www.uscourts.gov/sites/default/files/document/2026-05-evidence-rules-agenda-book.pdf
- **Date:** May 2026
- **How read:** not read (file not accessible)
- **Claims supported:** none directly; it is the primary record behind LG-01 and LG-02.
- **Limitations:** listed so the report writer knows where the primary text is.
- **Tensions:** none.

**LG-54**
- **Title:** Sexual Offences Act 2003, section 66I (purported intimate image generators)
- **Publisher:** legislation.gov.uk (The National Archives)
- **Type:** legislation
- **URL:** https://www.legislation.gov.uk/ukpga/2003/42/section/66I
- **Date:** in force 29 Jun 2026; page current to November 2026
- **How read:** full text (quoted in short excerpts)
- **Claims supported:**
  - Offence of making, adapting, supplying or offering to supply a thing "for use as a generator of purported intimate images".
  - The reasonable-person test ("a reasonable person (having regard to all the circumstances) would consider that they do so") and the all-reasonable-steps defence.
  - Summary conviction up to the general limit; up to 3 years on indictment.
  - s.66I(6): reach to acts outside England and Wales by UK nationals and bodies. s.66I(7): "thing" includes "a program, information in electronic form and a service", and "purported intimate image" has the s.66E meaning.
  - Annotation: ss.66I–66L inserted 29.6.2026 by Crime and Policing Act 2026 ss.99(2) and 255(1); SI 2026/689 reg. 2(1)(i).
- **Limitations:** ss.66J–66L not read separately.
- **Tensions:** none.

**LG-55**
- **Title:** Crime and Policing Act 2026 (c. 20), introductory text
- **Publisher:** legislation.gov.uk
- **Type:** legislation
- **URL:** https://www.legislation.gov.uk/ukpga/2026/20/introduction
- **Date:** 29 Apr 2026
- **How read:** full text (short page)
- **Claims supported:** Royal Assent "[29th April 2026]".
- **Limitations:** none.
- **Tensions:** resolves the earlier reliance on secondary sources (LG-20). The Act's contents page (https://www.legislation.gov.uk/ukpga/2026/20/contents) lists ss.98–103 under "Intimate images etc".

**LG-56**
- **Title:** Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards simplifying the implementation of harmonised AI rules (Digital Omnibus on AI) — title as rendered by the page tool
- **Publisher:** EUR-Lex (Official Journal of the European Union)
- **Type:** legislation
- **URL:** https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng
- **Date:** 8 Jul 2026; OJ L 24 Jul 2026; in force 27 Jul 2026
- **How read:** full text
- **Claims supported:**
  - New Art. 5(1)(ba): "an AI system that generates or manipulates realistic images, videos, audio or similar material" … "without that person's freely-given, specific, informed, unambiguous and explicit consent".
  - New Art. 5(1)(bb): CSAM, "except where a 'without right' defence applies under national law".
  - Scope: providers where generation is intended, or reasonably foreseeable and reproducible without adequate safeguards; deployers using the system for that purpose.
  - Art. 113(a): "shall apply from 2 December 2026". Art. 111(4): "comply with Article 50(2) by 2 December 2026".
  - Amended Art. 50(7) (codes of practice; implementing act if a code is inadequate). Entry into force on the third day after publication (Art. 4). Recital 38 (four-month transition).
- **Limitations:** parts of the scope wording were read as summaries; check the full title against the Official Journal.
- **Tensions:** confirms the secondary reports in LG-29.

**LG-57**
- **Title:** Criminal Code Amendment (Deepfake Sexual Material) Act 2024 (No. 78, 2024), as made
- **Publisher:** Federal Register of Legislation (legislation.gov.au)
- **Type:** legislation
- **URL:** https://www.legislation.gov.au/C2024A00078/asmade/text
- **Date:** 2 Sep 2024 (date shown next to the document ID)
- **How read:** partial (only the title, table of contents and status were available)
- **Claims supported:** title; Act No. 78, 2024 (C2024A00078); status "In force"; Schedule 1 amends the Criminal Code Act 1995.
- **Limitations:** the operative text of s.474.17A was not available.
- **Tensions:** none.

**LG-58**
- **Title:** Deepfake Digital Harm and Exploitation Bill 213-1 (2025), Members Bill
- **Publisher:** New Zealand Legislation (legislation.govt.nz)
- **Type:** legislation (bill)
- **URL:** https://www.legislation.govt.nz/bill/member/2025/0213/latest/whole.html
- **Date:** 2025 (introduction version)
- **How read:** secondary/search summary (official page not accessible)
- **Claims supported:**
  - Bill number 213-1. The explanatory note says it expands "intimate visual recording" in the Crimes Act 1961 and the HDCA 2015 to images "created, synthesised, or altered".
  - Crimes Act ss.216H–216N and HDCA s.22A would apply to created images.
  - Commencement the day after Royal Assent.
  - The "latest" version in search results is 213-1, suggesting no reported-back version yet.
- **Limitations:** not read. A "latest" version in search results does not prove the parliamentary stage.
- **Tensions:** none.

**LG-59**
- **Title:** Iowa appellate blog summary of State v. Amyda
- **Publisher:** Nyemaster Goode (via LexBlog)
- **Type:** other (law-firm commentary)
- **URL:** https://www.lexblog.com/organization/nyemaster-goode/
- **Date:** October 2026 (year inferred)
- **How read:** secondary/search summary
- **Claims supported:** the Iowa Supreme Court affirmed admission of the video over a deepfake claim; oral argument 9 Sep; opinion 9 Oct; Mansfield J. for a unanimous court.
- **Limitations:** the snippet omits the year. 2026 is inferred from the chronology: Court of Appeals decision on 28 Jan 2026 (LG-12) and Volokh's post on 13 Oct 2026 (LG-11).
- **Tensions:** a search summary suggested 2025; resolved as 2026.

## MK: Users, market and workflow (sources)

Access date for all entries: 2026-11-18.

### A. Read in full or in part

**MK-01. "How Americans View AI and Its Impact on People and Society"**
- Publisher and type: Pew Research Center; other (survey research).
- URL: https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/
- Published: 2025-09-17.
- How read: full landing report (methodology not read).
- Claims supported:
  - 76% say telling AI from human content is very important; 53% are not confident they can.
  - About six in ten want more control over AI in their lives.
  - 50% more concerned than excited (37% in 2021).
  - 57% rate risks high versus 25% for benefits.
  - n=5,023, fieldwork 9–15 June 2025.
- Limitations: US only; self-reported confidence; margin of error not captured.
- Tensions: MK-03 (importance versus behaviour).

**MK-02. Digital News Report 2026, Executive Summary**
- Publisher and type: Reuters Institute (byline not confirmed); other (survey).
- URL: https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary
- Published: 2026-06-16.
- How read: partial (~95%).
- Claims supported:
  - Concern about fake news online 62% (+4pp); rises above 5pp in 11 markets; Brazil −3pp.
  - Western Europe rise linked to "deepfakes, AI slop…".
  - Trust in chatbot answers 20% (UK 6%); news overall 37%; news on social media 22%.
  - Weekly chatbot news use 7%→10% (16% of under-35s); 42% click through.
  - 48 markets, about 2,000 respondents per market.
- Limitations: online panel; fieldwork dates not extracted.
- Tensions: question wording versus MK-03; MK-38.

**MK-03. Digital News Report 2025, Executive Summary**
- Author/publisher and type: Nic Newman, Reuters Institute; other (survey).
- URL: https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary
- Published: 2025-06-17.
- How read: full.
- Claims supported:
  - Where people check first: trusted news 38%, official sources 35%, search 33%, fact-checkers 25%, social media 14%.
  - 58% concerned about what is real or fake (US 73%).
  - Facebook and TikTok seen as biggest threats; influencers and politicians 47% each.
  - Chatbot news use 7%.
- Limitations: online panel; the search item's wording is ambiguous; regional figures inconsistent.
- Tensions: MK-01.

**MK-04. "TRIED: Truly Innovative and Effective AI Detection Benchmark"**
- Authors/publisher and type: Shirin Anlen and Zuzanna Wojciak, WITNESS; NGO (arXiv preprint).
- URLs: https://arxiv.org/html/2504.21489v2 (abstract: https://arxiv.org/abs/2504.21489)
- Published: v2 2025-05-01.
- How read: partial (~79%).
- Claims supported:
  - Six pillars; Deepfakes Rapid Response Force since Mar 2023 with "over forty experts".
  - Case failures (Philippines, Georgia, Sudan, Ghana, Venezuela, Myanmar, Mexico).
  - Crops flipping a verdict; difficulty interpreting confidence scores.
  - Python tool "exclusionary"; paywalls; tool abandonment; "can also easily be tricked".
  - Calls for retention policies and offline use; tools as one input; proving authenticity is harder.
- Limitations: advocacy casework; no case counts or quantitative scores.
- Tensions: transparency versus adversarial risk; consistent with MK-05 and MK-54.

**MK-05. "What Journalists Should Know About Deepfake Detection in 2025"**
- Author/publisher and type: Kaylee Williams, CJR/Tow Center; journalism.
- URL: https://www.cjr.org/tow_center/what-journalists-should-know-about-deepfake-detection-technology-in-2025-a-non-technical-guide.php
- Published: 2025-03-11.
- How read: full.
- Claims supported:
  - Detectors are "one tool among many".
  - Check training data and update date; over-reliance risk.
  - Generalisation drops; evasion; outputs hard to interpret.
  - WITNESS Feb 2024 tool comparison; Pikesville escalation.
- Limitations: no original tests or accuracy figures.
- Tensions: none.

**MK-06. "Verify AI-generated images, videos, and audio"**
- Publisher and type: Google (Gemini Help); platform documentation.
- URL: https://support.google.com/gemini/answer/16722517?hl=en
- Published: undated.
- How read: partial (page incomplete).
- Claims supported:
  - SynthID (Google AI only) plus C2PA; absence ≠ authentic.
  - Quotas and file limits; web and Android, iOS "soon"; sign-in required; no data terms on the page.
- Limitations: vendor self-description.
- Tensions: MK-33 (inconsistent behaviour reported in a hands-on test).

**MK-07. Privacy Policy, Is It AI?**
- Publisher and type: IsItAI.com; vendor documentation.
- URL: https://isitai.com/privacy
- Published: "Last updated: October 2026".
- How read: full.
- Claims supported: retention windows; anonymised training use; third-party detection, explanation and search providers; no mention of human review.
- Limitations: practice not audited; processors unnamed.
- Tensions: contrasts with MK-46.

**MK-08. Privacy Policy, AI or Not**
- Publisher and type: AI or Not Inc.; vendor documentation.
- URL: https://www.aiornot.com/privacy-policy
- Published: undated (©2023–2026).
- How read: full.
- Claims supported: no upload-specific terms; account-duration retention; Zoom audio in volatile memory, not used for training; sharing with hosting, Stripe and analytics providers; AWS.
- Limitations: none beyond the policy text.
- Tensions: contrasts with MK-07 and MK-46.

**MK-09. FAQ: Security & Compliance (GDPR)**
- Publisher and type: Sightengine; vendor documentation.
- URL: https://sightengine.com/faq/gdpr-content-moderation
- Published: undated (©2026).
- How read: partial.
- Claims supported: GDPR compliance; DPA with SCCs; enterprise data routing.
- Limitations: retention not on the page (see MK-46).
- Tensions: none.

**MK-10. Hive AI Detector, Chrome Web Store listing**
- Publisher and type: Castle Global Inc. / Chrome Web Store; vendor documentation.
- URL: https://chromewebstore.google.com/detail/hive-ai-detector/cmeikcgfecnhojcbfapbmpbjgllklcbi
- Published: last updated 2025-01-12 (v0.0.10).
- How read: full.
- Claims supported: free, no login; image, video, text and audio detection plus generator prediction; 50k users; 3.1/5 (414); handles "website content".
- Limitations: self-declared disclosures.
- Tensions: snippet rating of 4.6–4.7; MK-48 redirect.

**MK-11. "Norton Unveils Advanced Deepfake Protection Powered by Intel Core Ultra Processors"**
- Publisher and type: Gen Digital; vendor marketing.
- URL: https://newsroom.gendigital.com/2025-09-16-Norton-Unveils-Advanced-Deepfake-Protection-Powered-by-Intel-R-Core-TM-Ultra-Processors
- Published: 2025-09-16.
- How read: full.
- Claims supported: on-device NPU; YouTube and Facebook; Norton 360 Genie Scam Protection tiers; US, UK, AU, NZ; mobile Genie July 2025.
- Limitations: no accuracy data or prices.
- Tensions: MK-32.

**MK-14. "How it works", TrueMedia.org**
- Publisher and type: TrueMedia.org / Georgetown University; NGO/academic documentation.
- URL: https://www.truemedia.org/how-it-works
- Published: undated (© 2026 Georgetown University).
- How read: full.
- Claims supported:
  - "relaunching the TrueMedia Platform as a closed beta at Georgetown"; waitlist; "Non-partisan, open source, free"; hosted at Georgetown.
  - Authenticity Check (image and audio, URL or upload) and Veracity Check (text).
  - Outputs: aggregated scores, individual detector outputs, uncertainty levels, contextual notes; human verification by an in-house forensics team.
  - "No detector achieves 100% accuracy…".
- Limitations: no data-handling terms; no eligibility criteria.
- Tensions: scope versus MK-13.

**MK-17. "TrueMedia finds new home at Georgetown's McCourt School"**
- Publisher and type: Georgetown University McCourt School; other (university news).
- URL: https://mccourt.georgetown.edu/news/truemedia-finds-new-home-at-georgetowns-mccourt-school/
- Published: 2025-04-16.
- How read: full.
- Claims supported:
  - McCourt School is the new base; work carried by the Massive Data Institute (MDI) and Tech & Public Policy (TPP).
  - Leads: Lisa Singh, Michelle De Mooy, Sejin Paik, Julie Kanzler Dang.
  - Etzioni: "AI can help restore trust in what we see and hear online by detecting deepfakes".
- Limitations: no shutdown reasons, access terms or funding.
- Tensions: none.

**MK-18. "State of the Fact-Checkers: Audiences grow as finances worsen"**
- Publisher and type: IFCN at Poynter; NGO (survey report coverage by the publisher).
- URL: https://www.poynter.org/ifcn/2026/state-fact-checkers-2025/
- Published: 2026-04-06.
- How read: full article. The report PDF (https://www.poynter.org/wp-content/uploads/2026/03/2026-State-of-Fact-Checkers-4.pdf) could not be read.
- Claims supported:
  - 141 organisations in 71 countries.
  - 76% vulnerable or in crisis; 22.6% sustainable.
  - Meta revenue share 45.5%→34.3%; grants 46.2%; 56.9% single-funder dependent.
  - Staff cuts 38.3% (from 14.9%).
  - 53.3% integrated AI tools; 50% have AI guidelines (from 32%); 73% expect AI in a supporting role.
  - 49.6% say deepfakes and synthetic media are a major challenge.
- Limitations: self-reported; IFCN signatories only; definitions not in the article.

**MK-22. "Reality Defender Banks $33M to Tackle AI-Generated Deepfakes"**
- Publisher and type: SecurityWeek; journalism.
- URL: https://www.securityweek.com/reality-defender-banks-33m-to-tackle-ai-generated-deepfakes/
- Published: 2024-10-23.
- How read: full.
- Claims supported:
  - $33M expanded Series A; investors listed above.
  - Founded 2021; multimodal detection; financial-sector expansion.
  - Vendor-sourced figures: deepfake video prices up to $20,000 per minute; dark-web deepfake tool trading +223% (Q1 2023 to Q1 2024).
- Limitations: those statistics are vendor/Accenture-sourced.
- Tensions: none.

**MK-23. "Has GetReal cracked the code on AI deepfakes? $18M and an impressive client list says yes"**
- Publisher and type: TechCrunch; journalism.
- URL: https://techcrunch.com/2025/03/26/has-getreal-cracked-the-code-on-ai-deepfakes-18m-and-an-impressive-client-list-says-yes
- Published: 2025-03-26.
- How read: full.
- Claims supported:
  - $17.5M Series A led by Forgepoint; In-Q-Tel, Cisco and Capital One among strategic backers; prior $7M seed.
  - Founders Farid and Schlein.
  - Platform with web interface and API; Inspect, Protect and Respond modules (human analysts).
  - Customers John Deere and Visa; no self-serve tier; pricing undisclosed.
- Limitations: company-sourced claims.
- Tensions: headline "$18M" versus $17.5M.

**MK-45. Gemini Apps Privacy Hub**
- Publisher and type: Google; platform documentation.
- URL: https://support.google.com/gemini/answer/13594961?hl=en
- Published: updated 2026-11-16/17.
- How read: full (as extracted).
- Claims supported:
  - "A subset of chats are reviewed by human reviewers."
  - Reviewed chats kept up to 3 years, "even if you delete them".
  - Training on future chats when the setting is on; the hub says this covers attachments.
  - History-off chats saved "around 2 months".
  - "Please don't enter confidential information…".
- Limitations: does not single out verification uploads specifically.
- Tensions: older 72-hour figure (unverified).

**MK-46. Privacy Policy, Sightengine**
- Publisher and type: Sightengine; vendor documentation.
- URL: https://sightengine.com/policies/privacy
- Published: "Last updated: November 6, 2026".
- How read: full.
- Claims supported:
  - Deleted after processing by default; API content only used to return results (except the Feedback API).
  - Demo logs deleted after a limited period.
  - EU processing; hosting providers listed; processor under the DPA for API customers.
- Limitations: DPA and sub-processor list not read.
- Tensions: resolves MK-44.

**MK-47. Terms of Service, AI or Not**
- Publisher and type: AI or Not Inc.; vendor documentation.
- URL: https://www.aiornot.com/terms-of-service
- Published: undated (©2023–2026).
- How read: full.
- Claims supported:
  - No licence or training clause.
  - User responsible for content; termination may destroy content.
  - "AS-IS"; liability for "ACCURACY OF RESULTS" excluded.
  - Free or fee; Business plan; $5,000 per month resale cap.
  - Only "obscene" content is barred; no explicit intimate-image clause.
- Limitations: prices not shown.
- Tensions: none.

**MK-48. Privacy Policy, Castle Global, Inc. ("Deploy")**
- Publisher and type: Castle Global, Inc.; vendor documentation.
- URL: https://deploy.com/privacy (reached by 301 redirect from https://thehive.ai/privacy)
- Published: "last updated on October 23, 2026".
- How read: full.
- Claims supported:
  - Silent on detector uploads.
  - Retention "for as long as we have a relationship with you".
  - Product-development use; not selling data; deletion requests.
  - Links to thehive.ai and hivemoderation.com.
- Limitations: Hive's relationship to Deploy is unstated.
- Tensions: MK-10 branding.

**MK-49. "At GlobalFact 2026, fact-checkers report challenges, resilience"**
- Author/publisher and type: Louis Jacobson, Poynter; journalism.
- URL: https://www.poynter.org/fact-checking/2026/globalfact-2026-fact-checking-ai-misinformation/
- Published: 2026-06-23.
- How read: full.
- Claims supported:
  - GlobalFact held in Vilnius, 17–19 June 2026.
  - "Good enough" fakes quote.
  - Hibrid.info chatbot study (answers "reflect the ideological structures and data sources"; location effects).
  - Three-fourths of 100+ fact-checkers financially vulnerable.
  - 30 closed versus 10 opened in 2025; 437 active by mid-2026.
  - "meet people where they are".
- Limitations: conference reportage; no detector discussion.
- Tensions: consistent with MK-18.

**MK-50. Illuminarty homepage and plans**
- Publisher and type: Illuminarty; vendor documentation and marketing.
- URL: https://illuminarty.ai/en/
- Published: undated.
- How read: full.
- Claims supported:
  - Plans: Free $0, Basic $10/mo (10,000 API requests/day), Pro $30/mo (40,000/day), Enterprise on request.
  - "AI detection will always be free…"; extension "working on".
- Limitations: no accuracy data.
- Tensions: directory snippets claim an extension exists.

**MK-51. Privacy Policy, Illuminarty**
- Publisher and type: Illuminarty; vendor documentation.
- URL: https://illuminarty.ai/en/privacy.html
- Published: "Last updated: November 16, 2022".
- How read: full.
- Claims supported: images kept "only for the duration necessary"; training, sharing and human review not addressed; feedback goes to Typeform; entity and country not stated.
- Limitations: four years old.
- Tensions: none.

**MK-52. "SIFT (The Four Moves)"**
- Author/publisher and type: Mike Caulfield, Hapgood blog; other (educator method).
- URL: https://hapgood.us/2019/06/19/sift-the-four-moves/
- Published: 2019-06-19.
- How read: partial (the post itself; comments not read).
- Claims supported: the four moves; media-context guidance (cuts, captions, setting).
- Limitations: predates generative AI; does not mention reverse image search.
- Tensions: none.

**MK-53. "How to Spot AI-Generated Scam Products"**
- Author/publisher and type: Kolina Koltai, Bellingcat; journalism (OSINT guide).
- URL: https://www.bellingcat.com/resources/2025/03/25/detecting-ai-products/
- Published: 2025-03-25.
- How read: full.
- Claims supported: the seven checks listed in Key question 4; inconsistency quote; no detectors named.
- Limitations: e-commerce focus.
- Tensions: visual-cue optimism versus MK-54.

**MK-54. Verification Handbook 3, ch. 6, "How to think about deepfakes and emerging manipulation technologies"**
- Author/publisher and type: Sam Gregory (WITNESS); European Journalism Centre / DataJournalism.com; NGO/journalism guidance.
- URL: https://datajournalism.com/read/handbook/verification-3/investigating-actors-content/6-how-to-think-about-deepfakes-and-emerging-manipulation-technologie
- Published: undated (c. early 2020).
- How read: full.
- Claims supported:
  - Three-step approach; corroborate any sign of synthesis.
  - "A perfect deepfake detection system will never exist"; "Trusting the human eye is not a robust strategy!"
  - Compression degrades free tools; absence of evidence is not proof.
- Limitations: **partly outdated** (pre-diffusion visual tells such as blinking).
- Tensions: MK-53.

**MK-56. "InVID-WeVerify verification plugin"**
- Publisher and type: WeVerify project / AFP Medialab; NGO/journalism documentation.
- URL: https://weverify.eu/verification-plugin/
- Published: undated (references the Sept 2021 relaunch; page appears dated).
- How read: full.
- Claims supported: free extension; >57k weekly active users (as stated); maintained by AFP Medialab; feature list; advanced tools "reserved for journalists, fact-checkers and researchers…"; partner "web services".
- Limitations: likely outdated; no synthetic-detector information.
- Tensions: none.

**MK-57. Content Credentials Verify**
- Publisher and type: Content Authenticity Initiative; standards body / vendor documentation.
- URL: https://verify.contentauthenticity.org/ (contentcredentials.org/verify 301-redirects here)
- Published: undated.
- How read: page content not readable (title "Content Credentials").
- Claims supported: the redirect location as of the access date.
- Limitations: no data-handling text retrievable.
- Tensions: none.

**MK-58. DeepFake-o-meter**
- Publisher and type: University at Buffalo; academic tool.
- URL: https://zinc.cse.buffalo.edu/ubmdfl/deep-o-meter/
- Published: undated.
- How read: page content not readable (title "DFOM Frontend").
- Claims supported: the front end is live.
- Limitations: no access, output or privacy details retrievable.
- Tensions: none.

### B. Seen only as search-result summaries (unverified; re-check before citing)

**TrueMedia (MK-12, MK-13, MK-15, MK-16)**
- MK-12. TrueMedia shutdown post. TrueMedia.org; NGO. URL: https://truemedia.org/post/shutting-down-truemedia. Dated 2025-01-07 per search summary; page not found. Claim: service "sunset".
- MK-13. TrueMedia open-source release post. TrueMedia.org; NGO. URL: https://www.truemedia.org/post/open-source-release. Published 2025-01-27. Snippet only. Claim: image, video and audio models open-sourced; repositories described elsewhere as unmaintained.
- MK-15. GeekWire on the TrueMedia shutdown. Journalism. URL: https://www.geekwire.com/2025/truemedia-org-plans-to-shutter-and-open-source-its-ai-deepfake-detector-etzioni-hints-at-new-startup/. Published Jan 2025. Snippet only. Claim: closure after 13 Jan 2025.
- MK-16. GeekWire on the TrueMedia revival. Journalism. URL: https://www.geekwire.com/2025/truemedia-is-back-deepfake-detection-tool-revived-now-managed-by-georgetown-university/. Published 2025. Not accessible. Claim: Etzioni cited high maintenance cost.

**User-needs research (MK-19, MK-20)**
- MK-19. "Researchers Study How Deepfake Detection Tools Influence Journalists". University of Mississippi news release about a CHI 2024 peer-reviewed paper (DOI 10.1145/3613904.3641973). URL: https://olemiss.edu/news/2024/07/dungeons-and-deepfakes/. Published July 2024. Secondary and abstract-level. Claims: n=24 journalists; over-reliance; traditional checks first.
- MK-20. "Cutting through the Hype". University of Vienna note on a 2023 peer-reviewed Digital Journalism article (DOI 10.1080/21670811.2023.2194665). URL: https://polcom.univie.ac.at/news-events/detailansicht/news/new-publication-cutting-through-the-hype/. Snippet only; authors unconfirmed.

**Vendors and funding (MK-21, MK-24 to MK-29)**
- MK-21. McAfee Deepfake Detector coverage. Help Net Security and McAfee; journalism and vendor marketing.
  - URLs: https://www.helpnetsecurity.com/2024/08/21/mcafee-deepfake-detector/ and https://www.mcafee.com/en-us/newsroom/press-releases/2025/mcafee-brings-mcafee-deepfake-detector-to-select-hp-copilot-pcs.html
  - Published 2024-08-21 and Jan 2025. Search summaries only; the 2024 McAfee release was not accessible.
  - Claims: on-device NPU; opt-in; audio-only; English; Lenovo then HP.
- MK-24. Resemble AI $13M. SecurityWeek and AI News; journalism. URLs: https://www.securityweek.com/resemble-ai-raises-13-million-for-ai-threat-prevention/amp/ and https://www.artificialintelligence-news.com/news/google-sony-and-okta-back-resemble-ai-push-into-deepfake-detection/. Published Dec 2025. Snippet only.
- MK-25. Neuramancer €1.7M pre-seed. tech.eu; journalism. URL: https://tech.eu/2026/03/12/neuramancer-lands-eur17m-pre-seed-to-scale-deepfake-detection-tools/. Published 2026-03-12. Snippet only.
- MK-26. Modulate $25M. Crypto Briefing; journalism (low quality). URL: https://cryptobriefing.com/modulate-raises-25m-deepfake-detection/. Date unclear. Snippet only.
- MK-27. Voxmind pre-seed. Biometric Update; journalism. URL: https://www.biometricupdate.com/202605/voxmind-secures-funding-as-firms-seek-defenses-against-voice-deepfakes. Published May 2026. Snippet only. Claim: £546,491 pre-seed.
- MK-28. Clarity $16M seed. FF News; journalism. URL: https://ffnews.com/newsarticle/funding/clarity-raises-16m-in-seed-funding-led-by-walden-catalyst-and-bessemer-venture-partners. Undated. Snippet only.
- MK-29. "BNY, Samsung Next and Fusion Fund invest in Reality Defender". Reality Defender; vendor marketing. URL: https://www.realitydefender.com/insights/bny-samsung-next-and-fusion-fund-invest-in-reality-defender. Undated. Title only.

**Provenance tools, Norton and Gemini (MK-30 to MK-34)**
- MK-30. Adobe HelpX, Inspect Content Credentials. Adobe; vendor documentation. URL: https://helpx.adobe.com/creative-cloud/help/cai/adobe-content-authenticitiy-inspect.html. Not accessible. Snippet claim: uploads "isn't stored anywhere".
- MK-31. "Using the Verify tool". CAI open-source docs; standards body documentation. URL: https://opensource.contentauthenticity.org/docs/verify. Page not found. Snippet claim: verify by upload or public URL.
- MK-32. Norton support, community and mobile pages. Gen Digital; vendor documentation and marketing. Published 2025–2026. Snippets only.
  - URLs:
    - https://support.norton.com/sp/en/us/home/current/solutions/v2025051222180272
    - https://community.norton.com/t/introducing-deepfake-protection-feature/405536
    - https://newsroom.gendigital.com/2025-07-31-Norton-Adds-Audio-and-Visual-Deepfake-Protection-on-Mobile
    - https://www.gendigital.com/blog/news/family-of-brands/fight-deepfake-norton-media-shield
  - Claims: conflicting language and platform lists; "Media Shield" and "Video Analyzer" branding.
- MK-33. Gigazine hands-on test of Gemini's SynthID check. Journalism. URL: https://gigazine.net/gsc_news/en/20251121-gemini-check-synthid. Published 2025-11-21. Snippet only. Claims: renaming a file changed the answer; "SynthID is not currently functioning" error.
- MK-34. Google blog posts on content verification. Platform marketing. Not opened.
  - URLs: https://blog.google/technology/ai/ai-image-verification-gemini-app/ and https://blog.google/innovation-and-ai/products/making-it-easier-to-understand-how-content-was-created-and-edited/

**Other leads (MK-35, MK-37, MK-38)**
- MK-35. WITNESS TRIED press release and Tech Policy Press essay. NGO and journalism. Published 2025. Snippets only.
  - URLs: https://www.witness.org/ai-detection-global-benchmark-witness-2/ and https://techpolicy.press/five-real-world-failures-expose-need-for-effective-detection-of-ai-generated-media
- MK-37. imagewhisperer.org fact-check aggregator. Other (low reliability). URL: https://imagewhisperer.org/weekly-report/2026-02-18. Snippet claim: ~35% of fact-checked claims involve AI. Do not use.
- MK-38. Edelman and eMarketer summaries of DNR 2026. Other. Published June 2026. Snippets only.
  - URLs: https://www.edelman.com/newsroom/richard-edelmans-6am-blog/reuters-institute-digital-news-report-2026 and https://www.emarketer.com/content/social-platforms-news-sites-digital-media-reach
  - Claims: deepfake worry above 75% in several markets; 85% of US adults concerned (YouGov). Not found in MK-02.

**Further academic and vendor leads (MK-40 to MK-44)**
- MK-40. ICIS 2025 action-design study. AIS eLibrary; peer-reviewed conference paper. URL: https://aisel.aisnet.org/icis2025/hti/hti/20/. Snippet only. Claim: design requirements across journalism, security and finance.
- MK-41. Sohrawardi dissertation. RIT Repository; academic thesis. URL: https://repository.rit.edu/theses/12387. Published 2025. Snippet only. Claim: role-play method with journalists in the US and Bangladesh.
- MK-42. "DeFaking Deepfakes: Understanding Journalists' Needs for Deepfake Detection". Computation + Journalism 2020; academic paper. URL: https://cj2021.northeastern.edu/files/2019/11/CJ_2020_paper_64.pdf. Published 2020 (older). Snippet only.
- MK-44. Sightengine "Security & Compliance" page. Vendor documentation. URL: https://sightengine.com/security. Snippet only. Claim: immediate-deletion option. Superseded by MK-46.

**Ofcom, YouTube and IFCN detail (MK-55, MK-59 to MK-63)**
- MK-55. "Deepfake Defences 2: The Attribution Toolkit". Ofcom; government/regulator.
  - URLs: https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/deepfake-defences-2--the-attribution-toolkit (PDF: https://www.ofcom.org.uk/siteassets/resources/documents/online-safety/information-for-industry/deepfake-defences-2/deepfake-defences-2---the-attribution-toolkit.pdf)
  - Published 2025-07-11 (updated 2025-08-22).
  - Snippet only. The companion page https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/how-can-tech-firms-help-users-spot-deepfakes was not accessible.
  - Claims: four attribution measures; watermarks "often" stripped by basic edits; combine with classifiers and reporting; guidance, not rules.
- MK-59. "YouTube's likeness detection technology has officially launched". TechCrunch; journalism. URL: https://techcrunch.com/2025/10/21/youtubes-likeness-detection-technology-has-officially-launched. Published 2025-10-21. Snippet only. Claim: YPP creator rollout after pilot.
- MK-60. TechRadar on YouTube's likeness-detection expansion. Journalism. URL: https://techradar.com/computing/software/youtube-is-rolling-out-its-industry-first-likeness-detection-tool-to-all-channel-owners-and-not-just-big-content-creators-but-youll-need-to-share-your-government-issued-id-if-you-want-the-added-layer-of-protection. Date not shown. Snippet only. Claim: all channel owners; government ID required.
- MK-61. PhotographyTalk on YouTube likeness detection. Journalism. URL: https://www.photographytalk.com/youtube-opens-ai-likeness-detection-to-every-creator-18-and-older/. Snippet only. Claims: 16 May 2026 expansion to adult creators; voice detection planned. Date conflicts with MK-60.
- MK-62. Poynter IFCN detail. Other (secondary). Published 2026. Search summary only.
  - URL: https://www.poynter.org/ifcn/2026/fact-checkers-financial-losses-strain/ (plus the report PDF)
  - Claims: 67.2% vulnerable plus 8.8% in crisis among 137 respondents; legal action 20.4% (up from 16.4%); government pressure 29.2%; harassment 78%→65%; 92% adaptable.
- MK-63. "Ofcom's strategic approach to AI, 2026/27". Ofcom; government/regulator. URL: https://www.ofcom.org.uk/siteassets/resources/documents/about-ofcom/annual-reports/ofcoms-strategic-approach-to-ai-2026-2027.pdf. Snippet only. Claim: plans to stress-test interventions such as deepfake detection tools.

(MK-36, MK-39 and MK-43 are unassigned.)

### C. Sources not accessible (no claims drawn)

- https://www.realitydefender.com/pricing: page not found.
- factcheck.afp.com: not accessible.
- https://www.esafety.gov.au/industry/tech-trends-and-challenges/deepfakes: not accessible.
- https://www.mcafee.com/en-us/newsroom/press-releases/2024/mcafee-launches-worlds-first-automatic-and-ai-powered-deepfake-detector-on-select-new-lenovo-ai-pcs.html: not accessible.

## NC: NCII needs and harms (sources)

Access date for all entries: 2026-11-18. "Extract" means search-engine extracts or summaries only.

**NC-01**
- **Title:** Non-Consensual Synthetic Intimate Imagery: Prevalence, Attitudes, and Knowledge in 10 Countries
- **Author/publisher:** Umbach, Henry, Beard, Berryessa (CHI 2024; DOI 10.1145/3613904.3642382)
- **Source type:** peer-reviewed
- **URL:** https://arxiv.org/html/2402.01721v2 (abstract https://arxiv.org/abs/2402.01721)
- **Published:** arXiv 26 Jan / 13 Feb 2024; CHI May 2024
- **How read:** full text (HTML, about 86%)
- **Supports:**
  - N=16,693; 10 countries; YouGov; May–June 2023.
  - 2.2% victimisation and 1.8% perpetration, with behaviour, gender and country breakdowns.
  - Real NCII rated worse than synthetic (0.27; 0.56); viewing rated least bad.
  - About 4% victim-blaming; 28.1% familiar with the concept.
  - Recommendations: provenance, classifiers, own-face search; "laws are not a panacea".
- **Limitations:** 2023 data; self-report; unsure respondents excluded; victims may be unaware; weighting needed; low inter-rater reliability; text vs table mismatch on threat ratios.
- **Tensions:** gender pattern vs NC-05/NC-08; harm ranking vs NC-06.

**NC-02**
- **Title:** "That Experience Still Haunts Me to This Day": A Multi-Region Survey on AI-Generated Image-Based Sexual Abuse Victimization
- **Author/publisher:** Nicola Henry, Rebecca Umbach (Google), Renee Shelby, Kwynn Gonzalez-Pons (*International Journal of Human–Computer Interaction*); RMIT release
- **Source type:** peer-reviewed
- **URL:** https://www.rmit.edu.au/news/all-news/2026/nov/image-based-abuse ; https://research.google/pubs/that-experience-still-haunts-me-to-this-day-a-multi-region-survey-on-ai-generated-image-based-sexual-abuse-victimization/ ; https://www.news-medical.net/news/20261103/Study-reveals-widespread-abuse-involving-non-consensual-AI-generated-intimate-images.aspx
- **Published:** 2026 (RMIT release 4 Nov 2026; one source gives 8 Sept 2026 online)
- **How read:** abstract page and RMIT release in full; paper not read
- **Supports:**
  - More than 7,200 adults in AU/UK/US.
  - 15% digitally altered; 6.9% (about 7%) AI-generated; AU 7.7%; men 10.2% vs women 3.8%.
  - Higher-risk groups; women report worse impacts; about 87% reported at least one impact.
  - Blocking 69%; platform reporting 58%.
  - Related: 3.2% perpetration; "for fun or as a joke"; about 1 in 5 deliberately viewed.
  - Henry: "some people may never know…".
  - Secondary only: n=7,230; fieldwork Jul–Aug 2024; gender-impact percentages; perpetrator relationships.
- **Limitations:** Google-funded with a Google co-author; full text not read.
- **Tensions:** gender vs NC-05/NC-08; scale vs NC-44; 58% vs 56.8%.

**NC-03**
- **Title:** Deepfake Nudes & Young People (report); blog "Deepfake nudes are a harmful reality for youth"; press release "1 in 8 teens know someone targeted…"
- **Author/publisher:** Thorn
- **Source type:** NGO
- **URL:** https://www.thorn.org/blog/deepfake-nudes-are-a-harmful-reality-for-youth-new-research-from-thorn/ ; https://www.thorn.org/press-releases/1-in-8-teens-know-someone-targeted-by-deepfake-nudes-new-report-finds/ ; https://info.thorn.org/hubfs/Research/Thorn_DeepfakeNudes&YoungPeople_Mar2025.pdf
- **Published:** 3 Mar 2025
- **How read:** blog and press release in full; report PDF not readable
- **Supports:**
  - n=1,200, ages 13–20.
  - 31% familiar; 1 in 8 know a victim; 1 in 17 targeted (blog); 2% created; 20% think it is legal.
  - 41% "cause harm to the person in them"; harms named 30/29/26%.
  - 16% no or conditional harm, of whom 28% cited "not real".
  - 62% would tell a parent vs 34% of victims did.
- **Limitations:** country and fieldwork dates not stated; NGO advocacy role.
- **Tensions:** blog wording overstates the "not real" share (see Contradiction 3).

**NC-04**
- **Title:** Will I be believed? How deepfakes are adding fears to youth experiencing sextortion
- **Author/publisher:** Thorn
- **Source type:** NGO
- **URL:** https://www.thorn.org/blog/will-i-be-believed-how-deepfakes-are-adding-fears-to-youth-experiencing-sextortion/
- **Published:** 26 Sept 2024
- **How read:** full text
- **Supports:**
  - About 10% of financial-sextortion reports in 2023 involved inauthentic images.
  - The "fear of not being believed" quote.
  - 1 in 6 minors never disclose; disclosure via tools is twice as likely as to a parent.
  - Recommends proactive detection.
- **Limitations:** no sample size or years given; the vignette is fictional.
- **Tensions:** complements NC-03.

**NC-05**
- **Title:** In Deep Trouble: Surfacing Tech-Powered Sexual Harassment in K-12 Schools (report page and press release)
- **Author/publisher:** Center for Democracy & Technology
- **Source type:** NGO
- **URL:** https://cdt.org/insights/report-in-deep-trouble-surfacing-tech-powered-sexual-harassment-in-k-12-schools/ ; https://cdt.org/insights/cdt-research-reveals-widespread-tech-powered-sexual-harassment-in-k-12-public-schools/
- **Published:** 26 Sept 2024
- **How read:** both pages in full; PDF not read; some figures from extracts
- **Supports:**
  - US; Jul–Aug 2024 fieldwork; 2023–24 school year.
  - 39% heard of NCII at school; 15% knew of deepfake NCII; 51% vs 14% depiction by gender.
  - 71% of teachers report severe sanctions; 5% say the school helped with removal.
  - From extracts: 60%, 36%, 43%, 68/61%.
- **Limitations:** awareness, not victimisation, measures; sample sizes not obtained.
- **Tensions:** gender vs NC-01/NC-02.

**NC-06**
- **Title:** The new face of digital abuse: Children's experiences of nude deepfakes
- **Author/publisher:** Internet Matters (Opinium)
- **Source type:** NGO
- **URL:** https://www.internetmatters.org/hub/press-release/new-report-uk-teenagers-encountered-ai-generated-nude-deepfakes/ ; https://www.internetmatters.org/hub/research/children-experiences-nude-deepfakes-research/
- **Published:** Oct 2024 (fieldwork June 2024)
- **How read:** extract (site not accessible)
- **Supports:**
  - 2,000 parents and 1,000 children aged 9–17 (UK).
  - 13% "experience"; boys 2x; vulnerable 25% vs 11%.
  - 55% think a deepfake would be worse than a real image; 11% and 6% taught about it at school.
- **Limitations:** broad "experience" measure; the "99%" estimate is likely vendor-derived; primary not read.
- **Tensions:** gender; harm ranking.

**NC-07**
- **Title:** Common Sense Media Releases New Research on Teens and AI-Generated Explicit Material
- **Author/publisher:** Common Sense Media (with Burson)
- **Source type:** NGO
- **URL:** https://about.commonsensemedia.org/press-room/press-releases/common-sense-media-releases-new-research-on-teens-and-ai-generated-explicit-material
- **Published:** 21 Jul 2026
- **How read:** full text
- **Supports:**
  - n=1,314 US teens aged 13–17.
  - Nearly half have seen AI explicit material; almost a quarter saw it depicting themselves or someone they know.
  - 18% made it or know someone who did (63% of those depicted people they know); boys 11% vs girls 4% made it; 25% shared.
  - 67% fear being deepfaked (girls 71%, boys 62%); 30/23/9% behaviour changes.
  - 82% say it should be illegal; 23% say AI nudes are less harmful "because no one gets hurt".
- **Limitations:** fieldwork dates not given; "know someone who" measures; press-release level.
- **Tensions:** with NC-06 on harm ranking.

**NC-08**
- **Title:** eSafety urges schools to report deepfakes as numbers double; Deepfake damage in schools (advisory); Toolkit for Schools Respond 3B guide
- **Author/publisher:** eSafety Commissioner (Australia)
- **Source type:** government or regulator
- **URL:** https://www.esafety.gov.au/newsroom/media-releases/esafety-urges-schools-to-report-deepfakes-as-numbers-double ; https://www.esafety.gov.au/newsroom/blogs/deepfake-damage-in-schools-how-ai-generated-abuse-is-disrupting-students-families-and-school-communities ; https://www.esafety.gov.au/sites/default/files/2026-03/Respond-Guide-to-responding-to-image-based-abuse-involving-AI-deepfakes.pdf
- **Published:** June 2025 (guide file dated 2026-03)
- **How read:** extract (site not accessible)
- **Supports:**
  - Under-18 reports doubled in 18 months vs the prior 7 years; 4 in 5 female; almost weekly school incidents.
  - Advice to report to police; victims may be unaware the material exists.
- **Limitations:** based on reports to eSafety; primary not read.
- **Tensions:** gender vs NC-01/NC-02.

**NC-09**
- **Title:** eSafety action prevents services 'nudifying' Australian school children; Another three 'nudifying' services go dark…
- **Author/publisher:** eSafety Commissioner
- **Source type:** government or regulator
- **URL:** https://www.esafety.gov.au/newsroom/media-releases/esafety-action-prevents-services-nudifying-australian-school-children ; https://www.esafety.gov.au/newsroom/media-releases/another-three-nudifying-services-go-dark-in-australia-as-regulatory-pressure-mounts-over-child-safety-concerns
- **Published:** Sept–Nov 2025; about June 2026
- **How read:** extract
- **Supports:**
  - Warning to a UK provider (about 100k Australian visits a month), which withdrew.
  - 2026 Direction to Comply; 3 more services withdrew.
  - The 7 most-used services have withdrawn or are complying.
- **Limitations:** 2026 dates vary across sources.
- **Tensions:** none.

**NC-10**
- **Title:** eSafety image-based abuse FAQ; IBA Scheme Regulatory Guidance (Feb 2024); How to collect evidence; Addressing deepfake image-based abuse (blog)
- **Author/publisher:** eSafety Commissioner
- **Source type:** government or regulator
- **URL:** https://www.esafety.gov.au/key-topics/image-based-abuse/faq-about-image-based-abuse ; https://www.esafety.gov.au/sites/default/files/2024-02/Image-Based-Abuse-Scheme-Regulatory-Guidance-Feb2024.pdf ; https://www.esafety.gov.au/report/how-to-collect-evidence ; https://www.esafety.gov.au/newsroom/blogs/addressing-deepfake-image-based-abuse
- **Published:** Feb 2024 and others undated
- **How read:** extract
- **Supports:**
  - Altered and synthetic images are included; all complaints schemes cover synthetic material.
  - Evidence guidance: don't save images of minors; record URLs; involve a trusted person; mute rather than block.
- **Limitations:** primary not read.
- **Tensions:** possession requirement for hashing (NC-21/NC-22).

**NC-11**
- **Title:** A Revealing Picture: AI-Generated 'Undressing' Images Move from Niche Pornography Discussion Forums to a Scaled and Monetized Online Business
- **Author/publisher:** Graphika (Santiago Lakatos)
- **Source type:** other (research firm)
- **URL:** https://graphika.com/reports/a-revealing-picture
- **Published:** 8 Dec 2023
- **How read:** partial (landing page; full report gated)
- **Supports:** 34 providers; over 24M unique visitors in Sept 2023; spam up more than 2,000%; 52 Telegram groups with at least 1M users.
- **Limitations:** 2023 and superseded; Similarweb data.
- **Tensions:** scale vs NC-12.

**NC-12**
- **Title:** Indicator nudifier investigation ("AI nudifiers continue to reach millions and make millions")
- **Author/publisher:** Alexios Mantzarlis and Santiago Lakatos, Indicator (with WIRED coverage)
- **Source type:** journalism
- **URL:** https://indicator.media/p/ai-nudifiers-continue-to-reach-millions-and-make-millions
- **Published:** 14 Jul 2025
- **How read:** partial (visible portion; rest paywalled)
- **Supports:**
  - 85 sites (7 offline); "may be worth up to $36 million a year".
  - 62 of 85 on major cloud/CDN; 53 of 85 with major sign-on; mainstream payment providers.
  - From extract: about 18.5M visitors (WIRED); Google cut sign-on for 23 sites.
- **Limitations:** estimation method not visible; paywall.
- **Tensions:** 53 vs 54 sign-on count; Google funding of NC-02.

**NC-13**
- **Title:** City Attorney shuts down 10 websites that create nonconsensual deepfake pornography
- **Author/publisher:** San Francisco City Attorney
- **Source type:** court record / government
- **URL:** https://sfcityattorney.org/city-attorney-shuts-down-10-websites-that-create-nonconsensual-deepfake-pornography/
- **Published:** suit Aug 2024; update about June 2025
- **How read:** extract
- **Supports:** 16 sites sued; 200M+ visits in H1 2024; $100k settlement; 10 sites offline in California.
- **Limitations:** visits are not victims.
- **Tensions:** none.

**NC-14**
- **Title:** Meta sues AI 'nudify' app Crush AI…
- **Author/publisher:** TechCrunch; CBS News
- **Source type:** journalism
- **URL:** https://techcrunch.com/2025/06/12/meta-sues-ai-nudify-app-crush-ai-for-advertising-on-its-platforms ; https://www.cbsnews.com/news/meta-nudify-app-lawsuit-crushai
- **Published:** 12 Jun 2025
- **How read:** extract
- **Supports:** Hong Kong suit over ad evasion; Lantern signal-sharing.
- **Limitations:** ad counts conflict; outcome unknown.
- **Tensions:** with NC-12.

**NC-15**
- **Title:** Ofcom launches investigation into X over Grok sexualised imagery; later updates
- **Author/publisher:** Ofcom
- **Source type:** government or regulator
- **URL:** https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery ; https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-update-monitoring-xs-response-to-hate-and-terror-content-and-grok-investigation-latest
- **Published:** 12 Jan 2026; updates to 14 Oct 2026
- **How read:** extract (not accessible)
- **Supports:** timeline; standalone-Grok limitation; still open at 14 Oct 2026; maximum penalties.
- **Limitations:** primary not read.
- **Tensions:** with NC-16.

**NC-16**
- **Title:** Commission investigates Grok and X's recommender systems under the Digital Services Act
- **Author/publisher:** European Commission
- **Source type:** government or regulator
- **URL:** https://digital-strategy.ec.europa.eu/en/news/commission-investigates-grok-and-xs-recommender-systems-under-digital-services-act
- **Published:** 26 Jan 2026
- **How read:** full text
- **Supports:** risk quote; risk-assessment duties, including before deployment.
- **Limitations:** no penalty information on the page.
- **Tensions:** with NC-15.

**NC-17**
- **Title:** Attorney General Bonta Sends Cease and Desist Letter to xAI…; Reuters via MarketScreener
- **Author/publisher:** California Attorney General; Reuters
- **Source type:** government / journalism
- **URL:** https://www.oag.ca.gov/news/press-releases/attorney-general-bonta-sends-cease-and-desist-letter-xai-demands-it-halt-illegal ; https://hk.marketscreener.com/news/california-ag-sends-cease-and-desist-letter-to-xai-on-deepfake-images-ce7e58dfd88ef22d
- **Published:** 16 Jan 2026
- **How read:** extract
- **Supports:** cease-and-desist; imagery still generated after restrictions; Indonesia and Malaysia blocks.
- **Limitations:** primary not read.
- **Tensions:** none.

**NC-18**
- **Title:** CCDH Grok research, as reported
- **Author/publisher:** Center for Countering Digital Hate, via AFP/The Star and Decrypt
- **Source type:** NGO (via journalism)
- **URL:** https://www.thestar.com.my/tech/tech-news/2026/01/23/musk039s-grok-created-three-million-sexualised-images-research-says ; https://decrypt.co/355543/grok-generated-23k-sexualized-images-children-watchdog-reports
- **Published:** 22–23 Jan 2026
- **How read:** extract
- **Supports:** about 3M images in about 11 days; sample method; about 23,338 appearing to depict minors; LLM classifier; X restrictions on 9 and 14 Jan.
- **Limitations:** LLM classification; consent not assessed; primary not read.
- **Tensions:** NYT's separate estimate seen only secondhand.

**NC-19**
- **Title:** TAKE IT DOWN Act (S.146, enrolled)
- **Author/publisher:** US Congress via GovInfo
- **Source type:** legislation
- **URL:** https://www.govinfo.gov/content/pkg/BILLS-119s146enr/html/BILLS-119s146enr.htm
- **Published:** signed 19 May 2025
- **How read:** full text
- **Supports:** digital-forgery definition; offences; request contents; 48 hours; identical copies; FTC enforcement; good-faith liability shield; exemptions.
- **Limitations:** whether removal covers forgeries not confirmed verbatim.
- **Tensions:** with NC-27.

**NC-20**
- **Title:** FTC Begins Enforcing Take It Down Act
- **Author/publisher:** US Federal Trade Commission
- **Source type:** government or regulator
- **URL:** https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act
- **Published:** 19 May 2026
- **How read:** full text
- **Supports:** start of enforcement; TakeItDown.ftc.gov; letters to 15 companies; quote.
- **Limitations:** no enforcement outcomes found.
- **Tensions:** none.

**NC-21**
- **Title:** StopNCII.org FAQ
- **Author/publisher:** StopNCII.org (SWGfL; developed with Meta)
- **Source type:** NGO
- **URL:** https://stopncii.org/faq/
- **Published:** undated (©2026)
- **How read:** full text
- **Supports:** synthetic images included; eligibility; on-device hashing; algorithms; limits.
- **Limitations:** no partner list on the page; internal inconsistency.
- **Tensions:** possession requirement vs NC-08/NC-10.

**NC-22**
- **Title:** Take It Down FAQ
- **Author/publisher:** NCMEC
- **Source type:** NGO
- **URL:** https://takeitdown.ncmec.org/faq/
- **Published:** undated (©2026)
- **How read:** full text
- **Supports:** eligibility; must have the image on the device; anonymous; "Do not download…"; limits.
- **Limitations:** silent on AI-generated images.
- **Tensions:** possession vs unawareness of the material.

**NC-23**
- **Title:** How we're addressing explicit fake content in Search
- **Author/publisher:** Google (Emma Higham)
- **Source type:** platform documentation
- **URL:** https://blog.google/products/search/google-search-explicit-deep-fake-content-update/
- **Published:** 31 Jul 2024
- **How read:** full text
- **Supports:** filtering and duplicate removal; demotion; over 70% reduction in exposure; "technical challenge".
- **Limitations:** self-reported metric.
- **Tensions:** with NC-24 intake.

**NC-24**
- **Title:** Remove involuntary fake pornography / sexual content from Google (Search Help)
- **Author/publisher:** Google
- **Source type:** platform documentation
- **URL:** https://support.google.com/websearch/answer/9116649?hl=en
- **Published:** undated
- **How read:** full text
- **Supports:** three criteria, including "The content is fake…"; separate category for real images; URLs and screenshots requested (can be cropped to the face); duplicate removal (opt-out available); search results only.
- **Limitations:** effect of choosing the wrong category unknown.
- **Tensions:** with authenticity-agnostic regimes.

**NC-25**
- **Title:** Developing a new partnership to combat non-consensual intimate imagery on Search
- **Author/publisher:** Google
- **Source type:** platform documentation
- **URL:** https://blog.google/products/search/stopncii-program-partnership/
- **Published:** 17 Sept 2025
- **How read:** extract
- **Supports:** StopNCII hashes coming to Search.
- **Limitations:** rollout status unknown.
- **Tensions:** none.

**NC-26**
- **Title:** Strengthening our approach to tackling non-consensual intimate imagery
- **Author/publisher:** Microsoft (Jenny Lay-Flurrie); also the Sept 2024 announcement as relayed in Microsoft's letter to Sen. Shaheen
- **Source type:** platform documentation
- **URL:** https://blogs.microsoft.com/on-the-issues/?p=67603 ; https://www.shaheen.senate.gov/download/niimicrosoftresponse?download=1
- **Published:** 27 May 2026 (blog); Sept 2024 (pilot)
- **How read:** blog full text; letter via extract
- **Supports:** "applied consistently across real and synthetic content"; form has options for real and AI images; Bing since Sept 2024; expanded to Teams Free, OneDrive, Xbox; human review and appeals; 268,899 images by Aug 2024 (extract).
- **Limitations:** company-reported.
- **Tensions:** none.

**NC-27**
- **Title:** Explicit AI Images of Female Public Figures (Oversight Board release); Meta transparency page for the case
- **Author/publisher:** Oversight Board; Meta
- **Source type:** platform documentation (quasi-judicial)
- **URL:** https://www.oversightboard.com/news/new-decision-addresses-metas-rules-on-non-consensual-deepfake-intimate-images/ ; https://transparency.meta.com/oversight/oversight-board-cases/explicit-ai-images/
- **Published:** 25 Jul 2024; Meta page updated 26 Sept 2024
- **How read:** both in full
- **Supports:**
  - Case facts: 48-hour auto-closure; Media Matching Service (MMS) bank; source-image observation.
  - Four recommendations verbatim; non-consent signal reasoning.
  - Quotes: "search for and report every instance"; "Even waiting 48 hours…".
  - Meta's statuses: Recs 1, 2 and 4 "Assessing feasibility"; Rec 3 "Implementing in full"; AI nudity removed "regardless of photorealism".
- **Limitations:** statuses as of Sept 2024; later changes unknown.
- **Tensions:** with NC-19 realism threshold.

**NC-28**
- **Title:** Non-consensual nudity policy
- **Author/publisher:** X Help Center
- **Source type:** platform documentation
- **URL:** https://help.x.com/en/rules-and-policies/intimate-media
- **Published:** undated
- **How read:** extract (not accessible)
- **Supports:** covers AI prompting and generation "even if unsuccessful".
- **Limitations:** primary not read.
- **Tensions:** policy vs practice (NC-31, NC-18).

**NC-29**
- **Title:** Reddit bans 'involuntary porn' communities…
- **Author/publisher:** TechCrunch
- **Source type:** journalism
- **URL:** https://techcrunch.com/2018/02/07/deepfakes-fake-porn-reddit-twitter-ban/
- **Published:** 7 Feb 2018
- **How read:** extract
- **Supports:** "depictions that have been faked"; 2022 rename (secondary).
- **Limitations:** out of date.
- **Tensions:** none.

**NC-30**
- **Title:** TikTok Community Guidelines: Integrity & Authenticity
- **Author/publisher:** TikTok (and press coverage)
- **Source type:** platform documentation
- **URL:** https://www.tiktok.com/community-guidelines/en/integrity-authenticity
- **Published:** 2023; 13 Sept 2025
- **How read:** extract
- **Supports:** no synthetic media of private individuals or minors.
- **Limitations:** image-based sexual abuse wording unverified.
- **Tensions:** none.

**NC-31**
- **Title:** Reporting Non-Consensual Intimate Media: An Audit Study of Deepfakes
- **Author/publisher:** Li Qiwei, Zhang, Kasper, Ashkinaze, Eaton, Schoenebeck, Gilbert
- **Source type:** preprint
- **URL:** https://arxiv.org/html/2409.12138v1
- **Published:** 18 Sept 2024
- **How read:** full text
- **Supports:** DMCA 25/25 removed (20.30 h) vs non-consensual-nudity route 0/25 in 21 days; consequences for posters.
- **Limitations:** one platform; small sample; synthetic personas; predates the TAKE IT DOWN Act and Grok.
- **Tensions:** with NC-28.

**NC-32**
- **Title:** Platforms as Crime Scene, Judge, and Jury: How Victim-Survivors of Non-Consensual Intimate Imagery Report Abuse Online
- **Author/publisher:** Li Qiwei, Kennon, Bedera, Eaton, Gilbert, Schoenebeck
- **Source type:** preprint
- **URL:** https://arxiv.org/html/2512.13500
- **Published:** 15 Dec 2025
- **How read:** partial (about 59%)
- **Supports:** n=13; needs and burdens; P5, P7 and P11 quotes; recommendations.
- **Limitations:** small US sample; deepfakes only briefly covered; not peer-reviewed.
- **Tensions:** none.

**NC-33**
- **Title:** Mapping the Burden: Toward Survivor-Centered Reporting Systems and Policies for Non-Consensual Intimate Images
- **Author/publisher:** Alice Jo, Grace Harlan; advisor Cailin Crockett (Berkman Klein Center, Applied Social Media Lab)
- **Source type:** other (white paper)
- **URL:** https://asml.cyber.harvard.edu/2026/06/04/mapping-the-burden/ ; https://cyber.harvard.edu/publication/2026/mapping-burden-survivor-centered-reporting-systems-policies-ncii
- **Published:** 4 Jun 2026
- **How read:** landing page in full; PDF not read
- **Supports:** 7 platforms; "structurally burdensome"; "entirely reactive"; content visible during review; recommendations.
- **Limitations:** platforms and methods not named on the page.
- **Tensions:** none.

**NC-34**
- **Title:** Sexualized Deepfake Abuse: Perpetrator and Victim Perspectives…
- **Author/publisher:** Flynn, Powell, Eaton, Scott (*Journal of Interpersonal Violence*); Monash press release and Lens article
- **Source type:** peer-reviewed
- **URL:** https://journals.sagepub.com/doi/10.1177/08862605251368834 ; https://www.monash.edu/news/articles/new-report-uncovers-perpetrator-and-victim-perspectives-on-sexualised-deepfake-abuse ; https://lens.monash.edu/2025/12/04/1387953/inside-the-minds-of-deepfake-abusers-what-drives-ai-fuelled-sexual-abuse
- **Published:** 9 Sept 2025; Lens 4 Dec 2025
- **How read:** abstract and press only
- **Supports:** 25 interviews; minimisation as justification vs coping; "just a joke"; little recourse.
- **Limitations:** small sample; full text not read.
- **Tensions:** none.

**NC-35**
- **Title:** 'It's Torture for the Soul': The Harms of Image-Based Sexual Abuse
- **Author/publisher:** McGlynn, Johnson, Rackley, Henry, Gavey, Flynn, Powell (*Social & Legal Studies* 30(4))
- **Source type:** peer-reviewed
- **URL:** https://durham-repository.worktribe.com/output/1297667
- **Published:** 2021
- **How read:** abstract only
- **Supports:** 75 victim-survivors; five harms.
- **Limitations:** pre-generative-AI.
- **Tensions:** none.

**NC-36**
- **Title:** Seeking Justice and Redress for Victim-Survivors of Image-Based Sexual Abuse
- **Author/publisher:** Rackley, McGlynn, Johnson, Henry, Gavey, Flynn, Powell (*Feminist Legal Studies* 29(3))
- **Source type:** peer-reviewed
- **URL:** https://durham-repository.worktribe.com/output/1276954
- **Published:** 2021
- **How read:** abstract only (full text requires login)
- **Supports:** "ad hoc, piecemeal and inconsistent"; reclaiming control; multi-agency response.
- **Limitations:** pre-generative-AI.
- **Tensions:** none.

**NC-37**
- **Title:** "Violation of my body:" Perceptions of AI-generated non-consensual (intimate) imagery
- **Author/publisher:** Brigham, Wei, Kohno, Redmiles (SOUPS 2024)
- **Source type:** peer-reviewed
- **URL:** https://www.usenix.org/conference/soups2024/presentation/brigham
- **Published:** Aug 2024
- **How read:** abstract-level (extract)
- **Supports:** n=315; AI-generated NCII judged far less acceptable; seeking it out more acceptable to some.
- **Limitations:** vignette study.
- **Tensions:** none.

**NC-38**
- **Title:** Examining public attitudes to deepfakes (Crest Advisory); Police warn of rising threat from sexual deepfakes (NPCC)
- **Author/publisher:** Crest Advisory for the Office of the Police Chief Scientific Adviser; National Police Chiefs' Council
- **Source type:** government or regulator
- **URL:** https://www.crestadvisory.com/post/examining-public-attitudes-to-deepfakes ; https://prgloo-prod-newsroom-npcc-01.azurewebsites.net/releases/police-warn-of-rising-threat-from-sexual-deepfakes
- **Published:** 24 Nov 2025 (Crest updated 12 Dec 2025)
- **How read:** both in full
- **Supports:**
  - n=1,700, aged 16+, England and Wales; 67% seen a deepfake; 21% and 14% viewed sexual deepfakes.
  - About 25% accept or are neutral about non-consensual sexual deepfakes; most rate them less harmful than phone theft.
  - 13% (+9% neutral) accept sharing after an argument; 92% say harmful; 3 in 5 worried; 14% aware of the law.
  - 5% created any deepfake (34%/14% of those sexual); about 1 in 6 created or would create.
  - 4% of Revenge Porn Helpline contacts reported to police.
  - Hammond quotes; police exploring image hashing for evidence.
- **Limitations:** pollster and fieldwork dates not given; secondary "7%/51%" figures not found.
- **Tensions:** with NC-06 on harm ranking.

**NC-39**
- **Title:** Malicious Actors Manipulating Photos and Videos to Create Explicit Content and Sextortion Schemes (I-060523-PSA)
- **Author/publisher:** FBI / IC3
- **Source type:** government or regulator
- **URL:** https://www.ic3.gov/PSA/2023/PSA230605
- **Published:** 5 Jun 2023
- **How read:** extract
- **Supports:** uptick in cases; victims unaware; advice.
- **Limitations:** 2023; no numbers.
- **Tensions:** none.

**NC-40**
- **Title:** The deepfake dilemma: new challenges protecting students' confidentiality (blog); Generative AI issue page; NCMEC/ICAC fact sheet; Stanford CIS letter
- **Author/publisher:** NCMEC; ICAC Task Force; Stanford CIS
- **Source type:** NGO
- **URL:** https://www.missingkids.org/blog/2025/the-deepfake-dilemma-new-challenges-protecting-students-confidentiality ; https://www.missingkids.org/theissues/generative-ai ; https://icactaskforce.org/assets/genai%20fact%20sheet%20-%20color.pdf ; https://cyberlaw.stanford.edu/letter-to-ncmec-about-ai-csam-report-statistics
- **Published:** 20 Nov 2025 (blog); others 2025–2026
- **How read:** blog in full; others via extract
- **Supports:**
  - Iowa case: 44 girls; four classmates charged as juveniles; victims silenced; no counselling.
  - Generative-AI report counts: 4,700 / 67,000 / 440,000 (H1 2025); over 1.5M in 2025, of which 1.1M were non-actionable Amazon reports (extract).
  - Images "nearly impossible to tell apart" (fact sheet); Stanford: at least 78% not AI CSAM.
- **Limitations:** counts reflect reporting artefacts.
- **Tensions:** 440k vs 485k.

**NC-41**
- **Title:** Sharing nudes and semi-nudes: advice for education settings working with children and young people
- **Author/publisher:** UK Council for Internet Safety / Department for Education
- **Source type:** government or regulator
- **URL:** https://www.gov.uk/government/publications/sharing-nudes-and-semi-nudes-advice-for-education-settings-working-with-children-and-young-people/sharing-nudes-and-semi-nudes-advice-for-education-settings-working-with-children-and-young-people
- **Published:** updated 11 Mar 2024 (disclaimer says Feb 2024)
- **How read:** full text (about 76%)
- **Supports:**
  - "deep fakes" / "deep nudes" terminology; "pseudo-images"; law applies to AI imagery.
  - "must not intentionally view…"; "never copy, print, share, store or save them; this is illegal".
  - No victim-blaming; viewing with a second staff member if unavoidable.
- **Limitations:** England only; tail of the page not read.
- **Tensions:** none.

**NC-42**
- **Title:** Statement: Detecting intimate image abuse; related Ofcom pages
- **Author/publisher:** Ofcom
- **Source type:** government or regulator
- **URL:** https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/statement-detecting-intimate-image-abuse
- **Published:** 18 May 2026; guidance 9 Sept 2026
- **How read:** extract (not accessible)
- **Supports:** hash-matching duty covering explicit deepfakes; reported in force 30 Sept 2026; enforcement programme; 48-hour consultation planned.
- **Limitations:** dates partly secondary.
- **Tensions:** hash limits.

**NC-43**
- **Title:** Tackling non-consensual intimate image abuse (Women and Equalities Committee), via summaries
- **Author/publisher:** UK Parliament; SCL; EVAW; SWGfL
- **Source type:** government or regulator
- **URL:** https://www.scl.org/tackling-non-consensual-intimate-image-abuse/ ; https://www.endviolenceagainstwomen.org.uk/governments-refusal-to-act-on-image-based-sexual-abuse-a-devastating-letdown/
- **Published:** 5 Mar 2025
- **How read:** extract
- **Supports:** possession-offence recommendation; helpline takedown over 90%; overseas hosting.
- **Limitations:** report text not read.
- **Tensions:** none.

**NC-44**
- **Title:** Revenge Porn Helpline report: insights from 2025; 2025 report PDF; related news
- **Author/publisher:** SWGfL / Revenge Porn Helpline; Jersey Evening Post
- **Source type:** NGO (plus journalism)
- **URL:** https://swgfl.org.uk/research/revenge-porn-helpline-report-insights-from-2025/ ; https://swgfl.org.uk/assets/documents/revenge-porn-helpline-2025.pdf ; https://jerseyeveningpost.com/news/2025/11/10/government-urged-to-fund-support-for-sextortion-victims-as-ai-deepens-abuse/
- **Published:** 2026; news 10 Nov 2025
- **How read:** SWGfL page in full; PDF not readable; news via extract
- **Supports:** about 25k reports (+11%); more than 20.8k images (+34%); over 94% removal; "63 synthetic" (unverified).
- **Limitations:** no verified synthetic breakdown.
- **Tensions:** vs survey prevalence.

**NC-45**
- **Title:** How we practice trauma-informed design at Chayn; Chayn Principles
- **Author/publisher:** Chayn
- **Source type:** NGO
- **URL:** https://chayn.notion.site/How-we-practice-trauma-informed-design-at-Chayn-1-Feb-2024-6f5211828e4a4a1db9735fe371febb79 ; https://chayn.notion.site/Principles-c706a97d50514fd2aa8e2f899bb77a1e
- **Published:** 1 Feb 2024
- **How read:** extract
- **Supports:** 8 principles.
- **Limitations:** definitions not read.
- **Tensions:** none.

**NC-46**
- **Title:** Trauma-Informed Computing: Towards Safer Technology Experiences for All
- **Author/publisher:** Chen, McDonald, Zou, Tseng, Roundy, Tamersoy, Schaub, Ristenpart, Dell (CHI 2022)
- **Source type:** peer-reviewed
- **URL:** https://par.nsf.gov/biblio/10347453
- **Published:** 2022
- **How read:** abstract-level
- **Supports:** 6 principles; 22 suggestions.
- **Limitations:** full text not read.
- **Tensions:** none.

**NC-47**
- **Title:** Safety by Design (principles, overview, 2024 TFGBV industry guide)
- **Author/publisher:** eSafety Commissioner
- **Source type:** government or regulator
- **URL:** https://www.esafety.gov.au/industry/safety-by-design ; https://www.esafety.gov.au/sites/default/files/2019-10/SBD%20-%20%20Principles.pdf
- **Published:** 2018/2019; guide Sept 2024
- **How read:** extract
- **Supports:** 3 principles.
- **Limitations:** current wording not verified.
- **Tensions:** none.

**NC-48**
- **Title:** When justice fails: Why women can't get protection from AI deepfake abuse
- **Author/publisher:** UN Women
- **Source type:** government or regulator (intergovernmental)
- **URL:** https://www.unwomen.org/en/articles/explainer/when-justice-fails-why-women-cant-get-protection-from-ai-deepfake-abuse
- **Published:** 26 Feb 2026
- **How read:** full text
- **Supports:**
  - Barriers: laws, forensics, cross-border cooperation, platform data-sharing, credibility attacks, defamation risk, showing images to officials.
  - Needs: being believed, justice, support, prevention.
  - Recommendations; "Self-regulation has not worked."
  - Cites 98%/99% to Security Hero's 2023 "State of Deepfakes" (vendor) and the suicide-ideation figure to Panorama Global (2023).
- **Limitations:** relies on vendor statistics; no survey data on police reporting.
- **Tensions:** statistic provenance (NC-06).

**NC-49**
- **Title:** AI in the Criminal Justice System (slides)
- **Author/publisher:** Doughty Street Chambers
- **Source type:** other (practitioner training)
- **URL:** https://www.doughtystreet.co.uk/sites/default/files/media/document/AI%20in%20the%20CJS%20Slides%20Final.pdf
- **Published:** undated
- **How read:** extract only
- **Supports:** genuine images can be dismissed as AI in trials.
- **Limitations:** opinion; low weight.
- **Tensions:** only source found for the liar's dividend in NCII.

**NC-50**
- **Title:** AAP report on an Australian AI-sextortion prosecution (defendant not named here)
- **Author/publisher:** Australian Associated Press
- **Source type:** journalism
- **URL:** https://aapnews.aap.com.au/news/first-look-at-creep-who-scraped-photos-to-sextort-women
- **Published:** 2026 (date not captured)
- **How read:** extract
- **Supports:** 8 women targeted; edited and original photos recovered from the device.
- **Limitations:** single case.
- **Tensions:** none.

**NC-51**
- **Title:** The Law Caught Up With AI Deepfakes: The Evidence Trail Didn't (plus older victim accounts)
- **Author/publisher:** International Business Times UK
- **Source type:** journalism
- **URL:** https://www.ibtimes.co.uk/uk-deepfake-laws-enforcement-investigations-grok-cases-1824265
- **Published:** 2026 (date not captured)
- **How read:** extract
- **Supports:** UK creation offence (Feb 2026, reported); police problems obtaining platform data and identifying users; older "nothing can be done" accounts.
- **Limitations:** anecdotal; older accounts superseded.
- **Tensions:** none.

## RC: Uncertainty framing and misuse (sources)

All access dates are 2026-11-18.

**RC-01**
- **Title:** ENFSI Guideline for Evaluative Reporting in Forensic Science (approved version 3.0; STEOFRAE project)
- **Publisher:** European Network of Forensic Science Institutes
- **Type:** standards body
- **URL:** https://enfsi.eu/wp-content/uploads/2016/09/m1_guideline.pdf
- **Date:** 2015 (exact approval date not seen in the passages extracted; the file was uploaded in September 2016)
- **How read:** full text of the guideline body (scope, §2.4, §3.13–3.14, guidance notes 1–4, glossary), from the PDF. The worked examples were partly read: the CCTV case was located and its propositions noted.
- **Claims supported:**
  - Evaluative report definition; LR as the measure of support.
  - The four requirements: Balance, Logic, Robustness, Transparency.
  - "not the probability of the propositions"; transposed-conditional definition.
  - Conclusion rules; illustrative verbal scale (LR 1, 2–10, 10–100, 100–1,000, 1,000–10,000, 10,000–1,000,000, ≥1,000,000).
  - Weak-support footnote; hierarchy warning; investigative reporting; variant five-step scale in a worked example; CCTV example.
- **Limitations:** predates generative AI; the scale is "for illustration purposes only"; currency since 2015 not checked.
- **Contradictions/tensions:** consumer detector outputs (RC-12); the variant scale within the same document.

**RC-02**
- **Title:** Best Practices for Image Authentication, 18-I-001-2.0
- **Publisher:** Scientific Working Group on Digital Evidence (SWGDE)
- **Type:** standards body
- **URL:** https://www.swgde.org/wp-content/uploads/2025/03/2025-03-03-Best-Practices-for-Image-Authentication-18-I-001-2.0.pdf
- **Date:** Version 2.0, 3/3/2025. Final Approved Document (approved 2/21/2025). Supersedes v1.0 (released 7/11/2019).
- **How read:** full text, from the PDF.
- **Claims supported:**
  - Scope and integrity distinction; CGI includes "Artificial Intelligence (AI) based generators".
  - Single-image limits; "theoretically possible to generate a single frame… not detectable as virtual by a human".
  - Example propositions; "impossible to prove a negative result" / "unlikely the imagery has been manipulated or digitally created".
  - Camera-source caveat.
  - §8.2 reporting (strength of opinion, no unfounded numerical probability, limitations); §8.3 independent review; §9 "take care not to overstate results"; bias controls.
- **Limitations:** written for lab examiners; the CGI detection approach relies on human-anatomy artefacts; no LR scale.
- **Contradictions/tensions:** consumer tools (RC-12); RC-04 (numerical LRs); the FSR accreditation exemption (RC-17).

**RC-03**
- **Title:** OSAC 2021-S-0036 Standard Guide for Image Authentication (draft, OSAC proposed)
- **Publisher:** NIST OSAC
- **Type:** standards body
- **URL:** https://www.nist.gov/document/osac-2021-s-0036standard-guide-image-authenticationdraft-osac-proposed
- **Date:** undated in the parts read (2021 draft designation)
- **How read:** search result title only
- **Claims supported:** an OSAC proposed image-authentication guide exists.
- **Limitations:** status unknown; possibly superseded.
- **Contradictions/tensions:** none.

**RC-04**
- **Title:** A score based likelihood ratio framework for deepfake image identification in forensic science
- **Authors:** Tianli Guo, Jisong Li, Yunqi Tang (People's Public Security University of China); Scientific Reports 16:12149; doi 10.1038/s41598-026-42176-w
- **Type:** peer-reviewed
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13077008/
- **Date:** published 2026-03-05 (received 2025-11-26; accepted 2026-02-24)
- **How read:** full text (PMC)
- **Claims supported:** propositions; Capsule detector; KDE, PAV and ELUB pipeline; Cllr 0.2899 to 0.1625; RMEP 0.069, RMED 0.092, EER 0.0804; unseen-dataset AUCs 0.621–0.783; quotes on binary outputs, uncalibrated scores and further validation.
- **Limitations:** FF++ faces only, not social-media copies; single team; internal inconsistencies.
- **Contradictions/tensions:** RC-28 (humans beat detectors on a new dataset); RC-05.

**RC-05**
- **Title:** A forensic evaluation method for DeepFake detection using DCNN-based facial similarity scores
- **Publisher:** Forensic Science International
- **Type:** peer-reviewed
- **URL:** https://sciencedirect.com/science/article/pii/S0379073823001974
- **Date:** 2023 (per listing)
- **How read:** search summary only
- **Claims supported:** logistic-regression LR calibration; Cllr 0.077.
- **Limitations:** unverified.
- **Contradictions/tensions:** RC-04.

**RC-06**
- **Title:** Toward Interpretable Speech Deepfake Detection using Artifact-Specific Experts and Calibrated Detection Scores
- **Publisher:** arXiv
- **Type:** preprint
- **URL:** https://arxiv.org/pdf/2607.21127
- **Date:** July 2026 (inferred from the arXiv ID)
- **How read:** search summary only
- **Claims supported:** raw scores are not LRs; calibration data must match the target distribution.
- **Limitations:** unreviewed; audio only.
- **Contradictions/tensions:** none.

**RC-07**
- **Title:** Altay & Gilardi (title as recalled: "People are skeptical of headlines labeled as AI-generated, even if true or human-made, because they assume full AI automation"); PNAS Nexus 3(10): pgae403
- **Authors:** Sacha Altay, Fabrizio Gilardi (University of Zurich)
- **Type:** peer-reviewed
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11443540
- **Date:** 2024-10-01
- **How read:** full text (PMC)
- **Claims supported:** N = 4,976; −0.17 and −0.11 points; mislabelled human headlines −0.12 to −0.20; AI label 2.66 pp against "False" label 9.33 pp; definitions removed the effect; recommendations.
- **Limitations:** text headlines; online panels; small effects; possible date inconsistency for Study 2.
- **Contradictions/tensions:** RC-14.

**RC-08**
- **Title:** Labeling AI-generated media online
- **Authors:** Chloe Wittenberg, Ziv Epstein, Gabrielle Péloquin-Skulski, Adam J. Berinsky, David G. Rand; PNAS Nexus 4(6): pgaf170; doi 10.1093/pnasnexus/pgaf170
- **Type:** peer-reviewed
- **URL:** https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/9/583/files/2026/01/labelingaigenerated_2025.pdf
- **Date:** advance access 2025-05-28 (received 2024-09-15; accepted 2025-04-04)
- **How read:** full text of the main article (abstract through the start of Materials and methods); supplementary information not read
- **Claims supported:**
  - Exp. 1: October 2023, n = 3,223. Exp. 2: December 2023, n = 4,356.
  - Exact label wordings.
  - Belief −0.21 and −0.25 SD; credibility −0.34 SD; "AI-Generated" label −0.14 SD; hybrid −0.34 SD; engagement effects not significant for the AI label.
  - Implied-authenticity and false-positive warnings; limitations.
- **Limitations:** US; single post; small banner; 2023 context; competing interests (Google and Meta funding; one author later joined Meta).
- **Contradictions/tensions:** RC-14.

**RC-09**
- **Title:** The Liar's Dividend: Can Politicians Claim Misinformation to Evade Accountability?
- **Authors:** Kaylyn Jackson Schiff, Daniel S. Schiff, Natália S. Bueno; APSR 119(1): 71–90; doi 10.1017/S0003055423001454
- **Type:** peer-reviewed
- **URL:** https://www.cambridge.org/core/product/687FEE54DBD7ED0C96D72B26606AA073/core-reader
- **Date:** online 2024-02-20; issue February 2025
- **How read:** full text (HTML)
- **Claims supported:** N = 15,287; IU and OR effects; video largely ineffective; S4 OR about 0.14 SD; awareness 22% to 8%; fact-check result; quotes.
- **Limitations:** US online samples; former politicians; near-simultaneous rebuttal; 2021–22 data.
- **Contradictions/tensions:** RC-12 (Netanyahu video); RC-11.

**RC-10**
- **Title:** AI Images Detectors Are Being Used to Discredit the Real Horrors of War
- **Author:** Emanuel Maiberg (404 Media)
- **Type:** journalism
- **URL:** https://www.404media.co/ai-images-detectors-are-being-used-to-discredit-the-real-horrors-of-war/
- **Date:** 2023-10-13
- **How read:** partial (paywalled after the opening)
- **Claims supported:** a detector labelled a war photo as AI; Farid found "no signs" of AI.
- **Limitations:** detector not named in the visible text.
- **Contradictions/tensions:** RC-09.

**RC-11**
- **Title:** How AI Content Detection is Being Weaponized in the Iran War
- **Authors:** shirin anlen and Mahsa Alimardani (WITNESS); Tech Policy Press
- **Type:** NGO / journalism
- **URL:** https://techpolicy.press/how-ai-content-detection-is-being-weaponized-in-the-iran-war
- **Date:** 2026-03-17
- **How read:** full text
- **Claims supported:** Niloofar Square heatmap and chatbot case; NYT ELA/"normal map" case (over 600,000 views; NYT compression statement); expert quotes; Grok verdicts in June 2025; recommendations.
- **Limitations:** advocacy perspective (WITNESS promotes provenance); no prevalence data.
- **Contradictions/tensions:** RC-09; its own "adoption remains limited" caveat.

**RC-12**
- **Title:** Leading AI Image Detection Tools Mislead Online Users, Often Declaring Authentic Content Fake
- **Authors:** Isis Blachez, Sofia Rubinson, Ines Chomnalez (NewsGuard; edited by Dina Contini and Eric Effron)
- **Type:** journalism (structured tool test)
- **URL:** https://www.newsguardtech.com/?p=33448
- **Date:** 2026-05-08
- **How read:** full text
- **Claims supported:**
  - 15 authentic photos and 5 tools: false-positive rates per tool (40%, 20%, 6.67%, 0%, 0%; 13.33% overall).
  - Light-edit flag rates 27–93%; significant-edit detection 33–100%; disagreement on 35 of 45 images.
  - Vendor quotes.
  - Netanyahu café video flagged by Hive at 96.9%.
  - Conclusions.
- **Limitations:** small sample; free or cheapest tiers only; 50% threshold; NewsGuard is a commercial firm.
- **Contradictions/tensions:** vendor accuracy claims (not read); Hive's 0/15 false positives against the Netanyahu case.

**RC-13**
- **Title:** Coverage of Meta replacing "Made with AI" with "AI info"
- **Publishers:** Yahoo/UK news; heise
- **Type:** journalism
- **URLs:** https://uk.news.yahoo.com/meta-changes-label-made-ai-140000227.html ; https://heise.de/-9776887
- **Date:** about July 2024
- **How read:** search summary only
- **Claims supported:** label renamed after real photos were mislabelled; detection reportedly unchanged.
- **Limitations:** secondary; details are in the VE entries.
- **Contradictions/tensions:** RC-07; RC-26 (C2PA calls "Made with AI" ambiguous).

**RC-14**
- **Title:** PsyPost, "Slapping an 'AI-generated' label on political messages doesn't stop people from believing them" (Vladimir Hedrih), on Gallegos, Shani, Shi, Bianchi, Gainsburg, Jurafsky & Willer, "Labeling messages as AI-generated does not reduce their persuasive effects", PNAS Nexus, doi 10.1093/pnasnexus/pgag008
- **Type:** journalism, secondary to a peer-reviewed study
- **URL:** https://www.psypost.org/slapping-an-ai-generated-label-on-political-messages-doesnt-stop-people-from-believing-them/
- **Date:** article 2026-06-24; study 2026 (inferred from the "pgag" DOI prefix)
- **How read:** full secondary article; journal paper not opened
- **Claims supported:** n = 1,601 US (Prolific, 2024 data); persuasion about 9.74 pp; labels had no significant effect on persuasion, accuracy or sharing; 92% believed the label.
- **Limitations:** policy texts that were fact-based and hand-corrected; US; secondary reading.
- **Contradictions/tensions:** RC-07, RC-08.

**RC-15**
- **Title:** Score-based Likelihood Ratios for Deepfake Image Evidence (two Research Square preprints) and a related SSRN paper
- **Publishers:** Research Square; SSRN
- **Type:** preprint
- **URLs:** https://www.researchsquare.com/article/rs-10345546/v1 ; https://www.researchsquare.com/article/rs-8551375/v1 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5361068
- **Date:** undated (2025–2026)
- **How read:** search summary only
- **Claims supported:** Cllr 0.3306 to 0.3174 and 0.0202 to 0.0128.
- **Limitations:** unreviewed; likely the same team as RC-04.
- **Contradictions/tensions:** RC-04.

**RC-16**
- **Title:** Forensic Science Regulator: Code of Practice (version 1), gov.uk publication page
- **Publisher:** UK Forensic Science Regulator / gov.uk
- **Type:** government or regulator
- **URL:** https://www.gov.uk/government/publications/statutory-code-of-practice-for-forensic-science-activities
- **Date:** published 2023-03-13; in force 2023-10-02; **withdrawn 2026-03-06 (superseded by v2)**
- **How read:** full page
- **Claims supported:** statutory basis (FSR Act 2021 s.2); dates; withdrawal.
- **Limitations:** superseded.
- **Contradictions/tensions:** none.

**RC-17**
- **Title:** Forensic science activities: statutory code of practice – version 2
- **Publisher:** UK Forensic Science Regulator
- **Type:** government or regulator
- **URLs:** https://www.gov.uk/government/publications/forensic-science-activities-statutory-code-of-practice-version-2 ; https://assets.publishing.service.gov.uk/media/68401f4be550203c8209cce9/2025_05_20_Code_of_Practice_final.pdf
- **Date:** published 2025-06-05; in force 2025-10-02
- **How read:** partial (publication page in full; targeted passages from the 388-page PDF)
- **Claims supported:**
  - 13.1.8 balanced evaluative opinion; 31.4.6 task-relevant information.
  - Glossary definition of evaluative opinion.
  - §73.3.2 deepfake media sub-activity ("the Code applies but any requirement for ISO accreditation does not apply").
  - Video authenticity "(e.g. deep fakes)" as an opinion activity; DEMS/DAMS outputs for intelligence purposes only; §98.9.17; §98.2.11.
- **Limitations:** only searched passages read; my identification of which forensic science activity §73 and §98 belong to is an inference.
- **Contradictions/tensions:** RC-18 (validation emphasis).

**RC-18**
- **Title:** Forensic Science in Criminal Courts: Ensuring Scientific Validity of Feature-Comparison Methods
- **Publisher:** President's Council of Advisors on Science and Technology (PCAST)
- **Type:** government report
- **URL:** https://obamawhitehouse.archives.gov/sites/default/files/microsites/ostp/PCAST/pcast_forensic_science_report_final.pdf
- **Date:** September 2016
- **How read:** partial (targeted passages)
- **Claims supported:** definitions of foundational validity and validity as applied; "scientifically meaningless" without accuracy estimates; claims implying greater certainty "should not be permitted"; black-box studies with error rates.
- **Limitations:** about feature-comparison methods, not media authentication; US-specific; a 2016 policy context (later DOJ responses not read).
- **Contradictions/tensions:** RC-17.

**RC-19**
- **Title:** Strengthening Forensic Science in the United States: A Path Forward
- **Publisher:** National Research Council / National Academies Press (doi 10.17226/12589)
- **Type:** government report
- **URL:** https://www.nationalacademies.org/read/12589/chapter/2
- **Date:** 2009
- **How read:** **not read.** Page text was unavailable (page images); bibliographic details only.
- **Claims supported:** none (bibliographic only).
- **Limitations:** no verified content.
- **Contradictions/tensions:** none.

**RC-20**
- **Title:** NIST AI 100-4, Reducing Risks Posed by Synthetic Content
- **Publisher:** NIST, U.S. Department of Commerce
- **Type:** government report
- **URL:** https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-4.pdf
- **Date:** November 2024
- **How read:** partial (targeted passages)
- **Claims supported:** provenance "may contribute to trustworthiness but does not guarantee it"; absence of provenance as a signal only where expected; nonzero false positives and false negatives; evaluations should include unseen generators; false positives "extremely damaging"; TPR@FPR, for example 0.01%.
- **Limitations:** the full report was not read; it predates 2025–2026 generators.
- **Contradictions/tensions:** Principle 3 (absence of provenance nuance).

**RC-21**
- **Title:** Deepfake detection by human crowds, machines, and machine-informed crowds
- **Authors:** Matthew Groh, Ziv Epstein, Chaz Firestone, Rosalind Picard; PNAS 119(1): e2110013119
- **Type:** peer-reviewed
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8740705/
- **Date:** online 2021-12-28; issue 2022-01-04
- **How read:** most of the text (final portion not read)
- **Claims supported:** N = 15,016; model 65% and 80%; 82% of participants beat the model (Exp. 1); 66% to 73% with model advice; +10.4% when the model was right and −2.7% when wrong or equivocal; misled in 8 of 10 instances; Kim Jong-un and Putin examples; quotes.
- **Limitations:** 2020-era DFDC deepfakes; web volunteers plus Prolific.
- **Contradictions/tensions:** RC-28; RC-04.

**RC-22**
- **Title:** The Implied Truth Effect: Attaching Warnings to a Subset of Fake News Headlines Increases Perceived Accuracy of Headlines Without Warnings
- **Authors:** Pennycook, Bear, Collins, Rand; Management Science 66(11): 4944–4957
- **Type:** peer-reviewed
- **URLs:** https://dspace.mit.edu/handle/1721.1/130380 ; https://papers.ssrn.com/abstract=3035384
- **Date:** 2020
- **How read:** search summary only (repository not accessible)
- **Claims supported:** implied truth effect; Study 1 n = 5,271; Study 2 N = 1,568; "verified" tags as the remedy.
- **Limitations:** unverified details; text headlines.
- **Contradictions/tensions:** RC-08 (which cites it while noting a contrary finding in RC-07).

**RC-23**
- **Title:** Negative Consequences of Informing Voters about Deepfakes: Evidence from Two Survey Experiments
- **Authors:** John Ternovski, Joshua Kalla, P. M. Aronow; Journal of Online Trust and Safety 1(2); doi 10.54501/jots.v1i2.28
- **Type:** peer-reviewed
- **URL:** https://tsjournal.org/index.php/jots/article/view/28
- **Date:** 2022-02-28
- **How read:** abstract only
- **Claims supported:** warnings did not improve detection and made people believe real videos were fake; quotes.
- **Limitations:** no effect sizes seen; US.
- **Contradictions/tensions:** awareness-raising policy.

**RC-24**
- **Title:** Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security
- **Authors:** Bobby Chesney & Danielle Citron; 107 California Law Review
- **Type:** peer-reviewed (law review)
- **URL:** https://www.californialawreview.org/print/deep-fakes-a-looming-challenge-for-privacy-democracy-and-national-security (PDF: https://www.californialawreview.org/s/2-Chesney-Citron.pdf)
- **Date:** December 2019
- **How read:** partial
- **Claims supported:** liar's dividend quotes; the dividend "flows… in proportion to success in educating the public"; detection limits (Farid's "decades away"; "faring poorly").
- **Limitations:** 2019 technology context; doctrinal and legal argument rather than empirical data.
- **Contradictions/tensions:** RC-09 (video resistance).

**RC-25**
- **Title:** PAI's Responsible Practices for Synthetic Media (framework site, with case studies)
- **Publisher:** Partnership on AI
- **Type:** NGO (multistakeholder)
- **URL:** https://syntheticmedia.partnershiponai.org/
- **Date:** launched February 2023 (a "living document"); case studies March 2024 and November 2024
- **How read:** full landing page; individual case studies not opened
- **Claims supported:** practices on disclosure ("confidently detect"), speculation and uncertainty, provenance, consent; harms list; case-study titles.
- **Limitations:** voluntary; many supporters are industry members (possible conflict of interest); the page lists eight Group 2 case studies but its text says five.
- **Contradictions/tensions:** RC-08 (the limits of labels).

**RC-26**
- **Title:** C2PA User Experience Guidance for Implementers, v2.2
- **Publisher:** Coalition for Content Provenance and Authenticity
- **Type:** standards body (guidance)
- **URL:** https://spec.c2pa.org/specifications/specifications/2.2/ux/UX_Recommendations.html
- **Date:** undated (footer © 2026)
- **How read:** full page (UX guidance only; specification details out of scope)
- **Claims supported:** no "definitive claims about an asset's authenticity"; four-tier disclosure; "Made with AI" ambiguity; avoid value judgements; handling of malformed manifests; "recommendations, not mandates".
- **Limitations:** about provenance display only, not detectors; versions evolve.
- **Contradictions/tensions:** RC-20 (absence of provenance as a signal).

**RC-27**
- **Title:** AP, "Trump falsely claims a crowd photo from Harris' campaign rally in Detroit was created using AI" (syndicated)
- **Publisher:** Associated Press via ABC News and ADN; also FOX TV stations and Spectrum News
- **Type:** journalism
- **URLs:** https://abcnews.go.com/Technology/wireStory/trump-falsely-claims-crowd-photo-harris-campaign-rally-112787686 ; https://www.adn.com/nation-world/2024/08/11/trump-falsely-accuses-harris-campaign-of-fabricated-ai-crowd-photos/
- **Date:** 2024-08-11 to 2024-08-13
- **How read:** headlines from multiple outlets plus a search summary; article body not read
- **Claims supported:** Trump's claim of an AI-faked crowd; the campaign's 15,000-person statement; journalists' documentation; Farid's two-model analysis found no evidence of AI.
- **Limitations:** body text and quotes not verified directly.
- **Contradictions/tensions:** RC-09 (images, not video).

**RC-28**
- **Title:** Over-reliance cluster: (a) arXiv 2508.01906, "Effect of AI Performance, Risk Perception, and Trust on Human Dependence in Deepfake Detection AI system"; (b) CHI 2026 workshop paper (Zenodo record 19700249); (c) arXiv 2603.14658 (humans against detectors on CharadesDF and DF40)
- **Publishers:** arXiv; Zenodo
- **Type:** preprint / workshop paper
- **URLs:** https://arxiv.org/abs/2508.01906v1 ; https://zenodo.org/records/19700249 ; https://arxiv.org/pdf/2603.14658
- **Date:** (a) August 2025; (b) 2026-04-13; (c) March 2026 (from the arXiv ID)
- **How read:** search summary only
- **Claims supported:** n = 400 trust and false-positive-rate study; n = 381 UK study where explanations raised trust but not appropriate reliance; AI 0.537 against human 0.784 on CharadesDF.
- **Limitations:** unreviewed or workshop-level; details unverified.
- **Contradictions/tensions:** RC-04 (in-domain performance); RC-21.
