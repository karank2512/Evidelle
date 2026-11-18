# Media authenticity and deepfake detection

Sources accessed: 18 November 2026.
This is a research report only. It contains no product or build work.

> **Read this first.** This report analyses public sources. It is **not legal advice**, and nothing in it is, or should be used as, a verdict on whether any particular image or video is real or fake. No detector or other analysis tool was run, no media was uploaded or tested, and no intimate imagery was sought, viewed or handled.
>
> Bracketed IDs such as [DS-01] refer to entries in the accompanying source ledger. Each entry gives the source's URL, date, read status, limitations and contradictions. ID prefixes group sources by topic:
> - PV: provenance and watermarking
> - DS: detector science
> - VE: vendor claims and independent tests
> - LG: legal and evidentiary
> - MK: users and market
> - NC: non-consensual intimate imagery
> - RC: uncertainty framing and misuse

## 1. Summary

1. **No single method reviewed establishes, for an arbitrary photo or video under all conditions, whether it is AI-generated.** Reported performance belongs to particular datasets and test dates.
   - **In-the-wild benchmark.** Deepfake-Eval-2024 used items people submitted for checking in 2024. Open-source detectors scored AUC 0.50–0.63 for video and 0.52–0.56 for images, against 0.87–0.99 on their original benchmarks. The best anonymized commercial tools stayed below 90% accuracy on that dataset [DS-01, VE-01].
   - **Platform processing.** In specific studies, platform-style processing sharply reduced some detectors' performance [DS-07, DS-09, DS-11].
   - **Human judgment.** Results vary by media, task and participants. Several studies reviewed reported about 46% to 66%; one small, expert-heavy ASMR video study reported 87.5%. These are not a pooled estimate or a general accuracy range. Several studies documented overconfidence [DS-10, DS-16 to DS-23].
2. **Provenance and watermarks support specific claims, not the truth of a scene.**
   - A valid C2PA Content Credential from a trusted signer supports two things: who signed which claims, and that the file has not changed since signing. A provider's watermark detection supports that that provider's tools were involved.
   - Neither establishes that what is shown happened.
   - In the data found, coverage was low. A crawl found C2PA manifests on 0.43% of images, and in one 2025 test none of eight platforms preserved credentials.
   - **The absence of provenance or of a watermark is not, by itself, evidence either way** [PV-01, PV-09, PV-19, PV-25, PV-66].
3. **In the largest fact-check dataset reviewed, real media in a false context was the most common pattern.** Contextual verification addresses that pattern; pixel-level detectors are not designed to [DS-26, RC-11].
4. **What a detector flag means depends on how common fakes are among the items checked (the base rate).**
   - Hypothetical worked examples show that when fakes are rare, false alarms can outnumber correct flags even for an accurate detector, and a "not detected" result can leave substantial doubt.
   - No measured prevalence of AI-generated content in social-media feeds was found [DS-24; section 5.5].
5. **The forensic standards reviewed recommend reporting the strength of evidence rather than real/fake verdicts.**
   - SWGDE: "it is impossible to prove a negative result", so "no evidence of manipulation" is not proof of authenticity.
   - NIST: detector false positives "can be extremely damaging" [RC-01, RC-02, RC-20].
6. **The published vendor accuracy claims reviewed (95–99.5%) did not disclose the conditions needed to check them.**
   - The largest in-the-wild benchmark anonymized the commercial vendors it tested.
   - In a May 2026 test on 15 authentic war photos, false-positive rates ranged from 0% to 40% across five tools.
   - The US FTC found that one detector advertised as 98% accurate measured 53%. That was a text detector [VE-01, VE-04, VE-15 to VE-22, RC-12].
7. **For non-consensual intimate imagery (NCII), the removal routes reviewed do not ask for a detector verdict.**
   - In the US statutory process, the UK takedown duty, Australia's scheme and StopNCII, a request rests on identity and lack of consent, not on proof that an image is real or fake.
   - Eligibility and outcomes vary by jurisdiction and platform, and removal is not guaranteed.
   - Some routes ask the requester to classify the image. Google Search's route for fake imagery is one example.
   - Whether an image is genuine or fabricated can still matter for which criminal offence applies. New Zealand's current offences may not clearly cover synthetic images, though that is a tentative legal analysis.
   - A verdict can harm in both directions: "it's only fake" minimises the harm, and "it looks real" feeds disbelief [LG-07, LG-17 to LG-19, LG-32, NC-21, NC-24, NC-03, NC-04, NC-07].
   - Section 7 gives the read status of each legal claim.
8. **Misuse is documented.**
   - Detector outputs and forensic-looking visuals were used to falsely "debunk" authentic war photos and video in 2023 and 2026 [VE-06, RC-11, RC-12].
   - Evidence on the "liar's dividend" (real evidence dismissed as fake) is mixed between experiments and field cases [RC-09, RC-24].
9. **No commercial wedge was established.**
   - The evidence gives reasons for caution about consumer "AI or not" verdict tools, about detectors applied to intimate images, and about merging verdicts into survivor support.
   - One hypothesis worth testing is an **independent, standards-aligned evaluation and claims-disclosure service** for authenticity tools. It is unvalidated: no customer interviews were conducted, and ability to pay is unknown.
   - Section 13.3 proposes future questions, none of them started. Failing them would weaken this hypothesis, not show that no market or other approach exists.
10. **Provisional interface assessment.** Keep authenticity tooling and survivor support separate, with a content-free boundary. Authenticity uncertainty should not gate support; this is a design principle. Section 14 is provisional and is not a comparison with any other report.

---

## 2. Methods

- **Scope.** This is a review of public sources, accessed on 18 November 2026, covering seven topics:
  - provenance and watermarking;
  - detector science and failure modes;
  - vendor claims against independent evidence;
  - legal and evidentiary questions;
  - users, the market and practical verification workflows;
  - the context of non-consensual intimate imagery;
  - how to frame uncertainty, and how verdicts get misused.
- **Source types.** Peer-reviewed and preprint research; standards bodies (C2PA, ENFSI, SWGDE); platform and vendor documentation; vendor marketing, kept separate and labelled as such; government and regulator material; legislation and court records; NGO reports; investigative and technology journalism.
- **Read status.** Each source is recorded as read in full, read in part, read as an abstract only, or known only from a secondary account or a search-result summary ("snippet" or "extract"). Findings that rest only on secondary or snippet-level reads are flagged in the text and given lower confidence.
- **Uneven access.** Some primary sources were paywalled, blocked or otherwise unavailable. Where that happened, claims rest on secondary reports, and the ledger records this for each source.
- **No hands-on testing.** No detector, scanner, watermark decoder or other tool was run, and no media was uploaded or tested. Every performance figure comes from published studies, evaluations, NGO casework, journalism or regulators.
- **NCII research.** This was done only through published research, NGO, regulator, platform-policy, court and journalism sources. No intimate imagery was sought or viewed, and no service that produces such imagery was visited.
- **Worked numbers.** Base-rate and error-rate examples are calculations from published figures or from stated hypothetical inputs, and are labelled as such.
- **Limits of the advice.** The legal statements describe sources as read; they are not legal advice. Nothing here is a verdict on any item.

---

## 3. First, separate the questions

People ask "is this real?" but usually mean one of three questions, and each needs different evidence:

1. **Was this made or altered with AI?** Synthetic-media detectors and AI watermarks try to answer this.
2. **Where did this file come from, and has it changed since?** Provenance (C2PA / Content Credentials, signed capture) addresses this, when the signal is present and intact.
3. **Is what it shows true, and in the right context?** Contextual verification addresses this: the source, the account's history, other angles, place and time, and earlier copies.

The third question matters a great deal in practice. Google's AMMeBa analysis covered about 136,000 fact-checked claims, with data to November 2023.
- About 80% of the claims involved media.
- "Context manipulations" (real media with a false caption or setting) dominated at every time point with enough data.
- AI images were "rare until Spring of 2023" and then rose quickly [DS-26].

A detector working as designed would say "real" about a miscaptioned real photo. That answer is correct but does not address the claim being made.

For NCII the relevant legal and practical questions are usually different again: identity and consent. The removal routes reviewed generally turn on whether an image shows, or appears to show, a person in an intimate state without consent. Some criminal offences do turn on whether the image is genuine or fabricated (section 7).

---

## 4. Current approaches and what each can establish

### 4.1 Provenance: C2PA / Content Credentials

**What a credential proves.** A valid C2PA manifest shows two things: which certificate holder signed which claims about a file, and that the file has not changed since signing. C2PA's own explainer is explicit about the limits:
- Content Credentials "do not provide value judgments about whether a given set of provenance data is 'true'".
- Provenance "alone cannot tell you whether the digital content is true, accurate or factual", and is "not a cure-all for misinformation".
- The specification makes the signer responsible only for its own assertions. For example, the signer "is not responsible for the accuracy of a GPS location appearing in EXIF metadata" [PV-01, PV-02].

**The "AI-generated" flag is a declaration, not a detection.** The signing tool records AI involvement in the manifest's `digitalSourceType`, using IPTC terms such as `trainedAlgorithmicMedia`. The flag is only as trustworthy as the signer [PV-01, PV-02, PV-53].

**Valid is not the same as trusted.** C2PA's July 2026 deployment guidance separates two states:
- "Valid" means the credential is intact, but the signer may not be on the C2PA Trust List.
- "Trusted" means the signer is on the Trust List.

The conformance program launched on 4 June 2025, and by 14 May 2026, 54 products from 31 companies had passed. Google's Gemini verifier accepts credentials only from conformant C2PA 2.2+ products. A self-signed "LOCAL USE ONLY" certificate has been seen in the wild [PV-04, PV-05, PV-09, PV-25].

**In the tests found, platforms stripped credentials and labelled AI content inconsistently.**
- In October 2025 the Washington Post uploaded a Sora video carrying Content Credentials to eight platforms. None kept the credentials or let users see them. Only YouTube showed any label: an "Altered or synthetic content" note inside the description [PV-19, PV-63]. The original article is paywalled and was read through two reproductions.
- Indicator's audits found 169 of 516 AI posts (just over 30%) correctly labelled in October 2025 [PV-17].
- In March 2026 the rates were 67% on LinkedIn and Pinterest, about 50% on YouTube, about a third on TikTok, and 15 of 105 images on Instagram [PV-18].

**Provenance signals were rare where measured.** IPTC's Metawatch crawler found a C2PA manifest in 29 of 6,783 images (0.43%) between June and November 2026, mostly on news sites. Only 20 of the 29 were valid [PV-25]. No measurement for social-media feeds was found.

**Signed capture has been subverted.**
- In September 2025 a multiple-exposure technique made a Nikon Z6III sign composites built from unsigned files, including an obviously AI-generated image.
- Nikon suspended the service and revoked every certificate it had issued.
- Two outlets report that validators do not enforce revocation. Heise says standard C2PA validation does not check it. PetaPixel says online validators keep validating images signed by revoked cameras [PV-20 to PV-23].

**Device support is fragmented.**
- Google Pixel 10 signs every JPEG capture at C2PA Assurance Level 2.
- Samsung Galaxy S25 adds credentials only to AI-edited images.
- Apple has not adopted Content Credentials. In September 2026 it launched a separate, opt-in "Apple Reference Image" on the iPhone 18 Pro and Pro Max.
- Sony, Canon and Nikon systems mainly target professionals and newsrooms.

[PV-06, PV-26, PV-42 to PV-46. Several device items rest on secondary sources.]

### 4.2 Watermarks: SynthID and others

**Provider claims are self-reported.**
- For its external variant, SynthID-O, Google DeepMind reports true-positive rates of 99.98% (aggregated) and 99.72% (aggregated worst case) at a 0.1% false-positive rate.
- The same paper says "Achieving perfect security is impossible". It aims to defeat black-box attackers at scale, not "a determined white-box adversary" [PV-10].
- No independent, peer-reviewed robustness test of production SynthID was found.
- An April 2026 open-source "reverse-SynthID" project claims 91% removal of watermark energy. Google disputes it, and the claim is unverified [PV-49].

**Published attacks are strong against academic and open schemes.**
- **Zhao et al. (NeurIPS 2024):** over 99% removal for three pixel-level schemes [PV-11].
- **WAVES (ICML 2024):** Stable Signature's average detection at a 0.1% false-positive rate fell to 0.001 under diffusion regeneration. StegaStamp held at 0.943, so robustness varies by scheme [PV-13].
- **UnMarker (IEEE S&P 2025):** the best detection rate for semantic watermarks fell to 43%. The authors write that "defensive watermarking is not a viable defense against deepfakes" [PV-14].
- **Spoofing and forgery:** watermarks can also be spoofed or forged onto real images, so real media tests as "AI" [PV-12, PV-15].
- **Theory:** Saberi et al. (ICLR 2024) prove that, after diffusion purification, low-perturbation watermarks cannot keep both removal and spoofing errors low [DS-13].

**A negative watermark result is not, by itself, evidence that content is authentic.** Watermark detectors are provider-specific.
- Google's Gemini help page says that if no SynthID is found, the content "wasn't created or edited by Google AI, but it could have been created by other AI systems". Checks are capped at 100 MB, video under 90 seconds, and about 10 checks per day per media type [PV-09].
- TikTok describes its invisible watermark as one "that only we can read". In November 2025 it was still described as a test [PV-39, PV-40].
- YouTube's help page says that if its "Captured with a camera" label is missing, "it doesn't mean the content has modified audio or visuals". The page also names the risk of filming a screen that shows synthetic content [PV-66].
- That open-weight and local tools generally mark nothing is an inference, not a measured finding.

**Visible watermarks have been removed in seconds.**
- 404 Media found three websites that removed Sora 2's visible watermark "in a matter of seconds" [PV-24].
- In one study, removing the Sora 2 watermark cut vision-language-model detection by about 30 points. Some apparent "detection" was really watermark reading [DS-10].
- OpenAI closed the Sora web and app experience on 26 April 2026, and the Sora API on 24 September 2026 [PV-48, secondary].

**Marking mandates are arriving, mostly with feasibility qualifiers.** Read status is given next to each item.

| Jurisdiction | Mandate and timing |
|---|---|
| **EU** | **AI Act Article 50** applies from 2 August 2026. *Read in full via an unofficial reproduction, not the Official Journal* [LG-28].<br><br>**Regulation (EU) 2026/1744** (the AI Omnibus, 8 July 2026; in force 27 July 2026):<br>• gives generative systems already on the market until 2 December 2026 to add machine-readable marking;<br>• from the same date, bans AI systems that generate "realistic" non-consensual intimate images of identifiable people (Art. 5(1)(ba)) and systems that generate child sexual abuse material (Art. 5(1)(bb)).<br>*Primary text read in full on EUR-Lex* [LG-56].<br><br>**Commission Code of Practice** (finalised 10 June 2026):<br>• asks for "at least two layers" of machine-readable marking;<br>• was "assessed as adequate both by the Commission and the AI Board";<br>• its live list shows 266 unique signatories, 103 of them for the marking section, including Google, Meta, Microsoft and OpenAI.<br>*Commission pages read in full* [PV-28, PV-30]. |
| **China** | Labelling measures in force since 1 September 2025, alongside a mandatory national standard (GB 45438-2025).<br>• Explicit labels must be perceivable by users.<br>• Implicit labels in metadata (the provider's name or code and a content reference number) are required.<br>• Other implicit labels, such as digital watermarks, are encouraged but not required.<br>• Platforms must check metadata and add conspicuous notices when content is confirmed, declared or suspected to be synthetic.<br>• Removing labels is prohibited.<br>*Unofficial translation, read in full via a reproduction; the national standard was seen only in a search summary* [PV-33, PV-34, PV-65]. |
| **India** | IT Rules amendment in force since 20 February 2026.<br>• Labels must be "prominent, easily noticeable, and adequately perceivable".<br>• Takedown deadlines drop from 36 to 3 hours for orders.<br>• For non-consensual nudity or morphed imagery, including deepfake pornography, they drop from 24 to 2 hours.<br>*Law-firm analysis read in full; the Gazette text was not read* [PV-37, PV-64]. |
| **California** | SB 942 became operative on 2 August 2026. AB 853 adds platform duties from 1 January 2027 and capture-device duties from 1 January 2028.<br>*Secondary only* [PV-35].<br><br>A further 2026 amendment, SB 1000, is reported by a single law-firm source and is unverified [LG-49]. |

### 4.3 Detectors: forensic and machine-learning classifiers

**Strong on the generators they were trained on, much weaker on unseen generators, in the studies reviewed.**
- **GenImage:** a ResNet-50 trained on Stable Diffusion v1.4 scores 99.9% on SD v1.4, but 52.0% on BigGAN, 53.5% on ADM and 54.9% on Midjourney [DS-03].
- **Chameleon** (AI images selected because they fooled humans): every one of the ten detectors tested scored at most 65.8% accuracy. On the AI images themselves, most scored 0–27% [DS-02].
- **LaDeDa:** 92.7% on academic benchmarks, but 68.3% on a set of social-media images [DS-06].
- **Community Forensics:** trained on 4,803 generators, it reached 89.2% accuracy on 21 unseen generators, with gains plateauing beyond about 1,000 generators. Its authors say error rates are "still too high for many critical applications" [DS-05].

**On one in-the-wild benchmark, open-source detectors scored near chance.** Deepfake-Eval-2024 used deepfakes from 2024 that people had submitted for checking, collected from 88 websites in 52 languages. Open-source detectors scored these AUCs, against 0.87–1.00 on their original benchmarks:

| Modality | AUC on Deepfake-Eval-2024 | Average AUC drop |
|---|---|---|
| Video | 0.50–0.63 | 50% |
| Audio | 0.43–0.58 | 48% |
| Image | 0.52–0.56 | 45% |

[DS-01 = VE-01.]

An August 2026 crisis-video preprint, RA-Bench, found seven video detectors falling from reference AUCs of 67.6–98.6% to 50.9–57.3% on open-source generators, and 43.9–54.0% on closed-source generators. Those figures apply to that benchmark's content and test conditions [DS-09].

**On the same benchmark, the best commercial tools did better but stayed below 90% accuracy.** The best anonymized commercial detectors scored:
- video: accuracy 0.78, AUC 0.79;
- audio: accuracy 0.89, AUC 0.93;
- image: accuracy 0.82, AUC 0.90, precision 0.99, recall 0.71. A supplementary table lists an image model at 0.86 accuracy.

The authors wrote that "no commercial models that we evaluated had an accuracy of 90% or above". They set that ~90% bar from labeller disagreement, as a proxy for expert analysts. Results were anonymized "to comply with contractual agreements", so no named vendor's claim can be checked against them [DS-01, VE-01]. A simply fine-tuned open model reached 0.81 accuracy and 0.89 AUC on the same images, and caught more than 30% of fakes with zero false positives [DS-25].

**Specialized methods have documented limits.**
- **Physiological (pulse) signals.** High-quality face swaps now carry the driver video's pulse (median r = 0.89), which undermines the premise of blood-flow detectors. This comes from one small study of 12 subjects [DS-15].
- **Partial edits.**
  - Classical forgery localizers found pasted-in inpainting (F1 0.79–0.87) but failed on fully regenerated inpainting (best F1 0.19).
  - Synthetic-image detectors flagged regenerated inpainting but could not say where the edit was.
  - Compression degraded both: localization F1 fell from 0.87 to 0.05–0.13 under JPEG or WEBP [DS-14].
  - On Deepfake-Eval-2024, face-focused video detectors lost 31% accuracy when only some faces were manipulated, and 17.4% when the manipulation was not of a face [DS-01].

### 4.4 Human judgment

Human accuracy varied by study, media type and task. Several studies found near-chance performance on high-quality synthetic faces and images, and documented overconfidence.

| Study | Result |
|---|---|
| Synthetic faces [DS-16] | 48.2% accuracy; 59.0% after training |
| Images, three countries [DS-19] | 45.9–49.9% |
| Deepfake video [DS-18] | 57.6% accuracy. 67.4% of all answers said "authentic". Overconfidence was negatively correlated with accuracy (r = −0.475). |
| About 287,000 judgments of mixed AI and real images [DS-20] | 62% |
| Meta-analysis of 56 papers [DS-21] | Pooled 55.5% (95% CI 48.9–62.1). Search summary only. |
| Veo 3.1 video, n = 40 [DS-23] | 66.4% |

**AI advice cut both ways in one large study.** Seeing a model's prediction raised accuracy from 66% to 73%. When the model was wrong about a political deepfake, accuracy fell from 56% to 34% [DS-17]. In another study, awareness prompts and financial incentives had no effect [DS-18].

### 4.5 Contextual verification

In the largest fact-check dataset reviewed, the most common pattern was real content in a false context [DS-26]. Contextual checks address that pattern directly:
- the original source and its account history;
- earlier copies, found by reverse search;
- other angles of the same event;
- place and time;
- the publisher's records.

In documented 2026 cases, authentic war photos were falsely "debunked" as AI. The false claims were rebutted with provenance-type evidence, not counter-detector scores [RC-11]:
- the photographer published the original and edited versions;
- a second photographer had shot the scene from another position;
- the publisher explained normal compression behaviour.

### 4.6 What each signal can and cannot tell a viewer

| What you observe | What it supports | What it does not establish |
|---|---|---|
| Content Credential intact and **Trusted** (signer on the C2PA Trust List) | The file is unchanged since signing, and a vetted signer made the listed claims. An AI `digitalSourceType` supports that the signer declared AI involvement. A conformant camera or phone signature supports that the pixels came through that device's capture pipeline. | That the scene is real, unstaged, or not a re-photographed screen. YouTube itself names the risk of filming a screen showing synthetic content. It also does not establish anything done before signing, the identity of the people shown, consent, or that the device was not subverted, as in the Nikon case. [PV-01, PV-02, PV-04, PV-20, PV-21, PV-66] |
| Credential intact but signer **untrusted**, self-signed or revoked | Someone holding that key made these claims. | Who the signer is, or whether the claims are true. Anyone can self-sign. [PV-25, PV-21] |
| Credential present but **invalid** (changed after signing) | The file or manifest changed after signing, whether benignly (re-encoding, cropping) or not. | That the content is fake, or that it is real. [PV-25, PV-19] |
| **No credential** (the usual case where measured) | Nothing about origin. | Neither authenticity nor AI generation. Platforms have stripped metadata, screenshots remove it, and few files carried it where measured. YouTube says a missing "Captured with a camera" label "doesn't mean the content has modified audio or visuals". [PV-01, PV-25, PV-66] |
| Provider watermark **detected** (e.g., SynthID) | That provider's tools generated or edited at least the flagged parts, according to the provider's own detector. No independent robustness test was found. | How much is AI, who made it, or consent. Not fully forgery-proof. [PV-09, PV-10, PV-12, PV-15] |
| **No watermark** detected | Only that this provider's mark was not found. | Authenticity. The content could come from another generator, an open model, or a removal attack. [PV-09, PV-11, PV-13, PV-14] |
| Visible AI mark or platform AI label **present / absent** | Presence: someone signalled AI involvement. | Absence is not evidence either way. Visible marks have been removed in seconds. Platform labels missed many AI posts in audits (about 14–67% labelled). A visible mark can be faked onto real media. [PV-24, PV-17, PV-18] |
| Detector says **"AI"** | Depends on the base rate and the detector's real-world operating point (see 5.5). | Proof, or that the event was fabricated. Reported false-positive rates varied widely: 0–40% per tool on authentic war photos in one test. Lightly retouched real photos were flagged as AI 27–93% of the time, and real media can be pushed to look fake. [DS-01, DS-09, DS-12, RC-12, VE-31] |
| Detector says **"not AI"** / "no manipulation found" | Limited support. On Deepfake-Eval-2024, the best commercial image tool missed 29% of fakes (derived from published figures). | Authenticity. SWGDE: "it is impossible to prove a negative result". [DS-01, VE-01, RC-02] |
| Context checks (source, earlier copies, other angles) | Can resolve the most common pattern in the fact-check data: real media in a false context. | Whether pixels were generated, when no earlier or independent copy exists. [DS-26, RC-11] |

---

## 5. Failure modes

### 5.1 New generators

Detectors learn the fingerprints of the generators they were trained on. In the studies reviewed, performance fell substantially on generators they had not seen [DS-02, DS-03, DS-05, DS-06].
- **The lag is a known issue.** Even a vendor page that discloses its limits says there is "a short window after a model launches when detection accuracy on its outputs is lower" [VE-16].
- **Current generators are untested as circulated.** No benchmark read in full measured detectors on Sora 2 or Veo 3 posts as they actually circulate after platform processing.

### 5.2 Re-encoding, resizing and platform processing

In the studies reviewed, platform-style processing degraded several detectors substantially, and the size of the effect varied from detector to detector.
- **FaceForensics++ XceptionNet:** 99.26% on raw video, 95.73% at light compression (c23), 81.00% at heavy compression (c40). A hand-crafted detector fell from 97.63% to 55.98% [DS-11].
- **GenImage:** backbones trained on Stable Diffusion fell to 51.9–55.6% at JPEG quality 65. One detector trained with JPEG augmentation held at 97.3% [DS-03].
- **TrueFake:** one detector's true-positive rate on StyleGAN2 faces fell from 1.00 to 0.00 after upload to Facebook [DS-07].
- **RA-Bench:** this preprint simulated "last-mile" sharing (transcoding, half-resolution downsampling, 8 fps, a news badge). Fine-tuned multimodal detectors' fake recall fell from 46.0% to 1.4%, and detector rankings before and after barely matched (Spearman 0.07) [DS-09].

Screenshots, screen recordings and re-photographing are common laundering steps, but no quantitative study of them was found. WITNESS case work reports that cropping or downscaling an AI image flipped a public detector's verdict from "fake" to "authentic" [VE-02].

### 5.3 Adversarial evasion, and real media made to look fake

In published attacks, largely on 2020-era detectors, small perturbations were enough:
- Flipping the lowest bit of 1% of pixels made half of fakes classify as real.
- A universal patch covering 1% of the image cut AUC from 0.966 to 0.085.
- A black-box transfer attack cut AUC from 0.96 to 0.22 [DS-12].

The same techniques worked in reverse:
- Flipping the lowest bit of just under 7% of pixels made half of real images classify as fake [DS-12].
- Watermark spoofing made real images register as AI-marked [DS-13, PV-12, PV-15].

Real media can also drift toward "fake" without any attacker:
- After Facebook upload, a CLIP-based detector's true-negative rate on real faces fell to 0.79 [DS-07].
- A detector trained on GenImage called uncompressed real photos "natural" only 80.45% of the time [DS-04].
- To catch 95% of fakes, traditional video detectors flagged 83.1–91.8% of real videos [DS-09].

### 5.4 What pixel-level detectors are not designed to assess

- **Real media in a false context.** This is the dominant pattern in the fact-check data reviewed [DS-26].
- **Partial or regenerated edits.** These are hard to detect and harder to localize, especially after compression [DS-14].
- **Partial manipulations in video.** Non-face manipulations, and cases where only some faces are altered [DS-01].
- **Formats outside the training data.** Examples include low-quality phone video, walkie-talkie or radio audio, unsupported languages such as Khmer, and subjects with darker skin tones [VE-02, VE-03].
- **Consent.** No authenticity signal addresses whether consent was given.

### 5.5 Base rates: what a "fake" flag means (hypothetical worked examples)

A detector's sensitivity and specificity do not, on their own, give the chance that a flagged item is fake. That also depends on how common fakes are in the set of items being checked.

**The figures below are arithmetic from standard formulas using stated hypothetical inputs.** They are not measurements of any feed. No measured prevalence of AI-generated content in social-media feeds was found.

| Detector (sensitivity / specificity) | Share of flags that are really fake, at an assumed prevalence of 1% / 10% / 50% |
|---|---|
| 95% / 95% (hypothetical) | 16.1% / 67.9% / 95.0% |
| 90% / 99% (hypothetical) | 47.6% / 90.9% / 98.9% |
| About 71% / 98.9% (derived from published figures for the best commercial image model on Deepfake-Eval-2024) | about 39% (range 30–56%) / about 87% / about 98% |
| 95% sensitivity with an 83% false-positive rate (the best case among traditional video detectors on RA-Bench) | about 1.1% / about 11.3% / — |

What these examples illustrate:
- **When fakes are rare among the items checked,** false alarms can outnumber correct flags even for an accurate detector. Setting a strict threshold reduces false alarms but also catches fewer fakes: on RA-Bench, at a 5% false-positive rate, true-positive rates were 2.8–5.7% [DS-09].
- **A "not detected" result can leave substantial doubt when sensitivity is modest.** For illustration only: assume a 50% prior and the derived commercial image-model figures. A "not detected" result would then leave about a 23% probability that the item is fake. This is a hypothetical calculation, not an estimate for any real population.
- **Small test sets hide false positives.** "Zero false positives" on a few hundred real test images is statistically compatible with a true false-positive rate of about 0.4–2% (the "rule of three"). That matters at low prevalence (calculation).
- **Dataset composition is not prevalence.** Deepfake-Eval-2024's mix (61% of images, 47% of videos and 39% of audio items were fake) reflects how that dataset was assembled from items submitted for checking. It is not a measured prevalence for any population [DS-01].

The base-rate point for deepfakes was made explicitly in Facebook AI's 2019 DFDC preview paper. It noted that deepfakes are far rarer in "organic traffic" than in test sets, and that "precision is paramount for very-rare detection problems", and it introduced a weighted-precision metric for that reason [DS-24].

### 5.6 Evidence and likelihood framing, not binary verdicts

The forensic standards reviewed describe ways to report evidential strength without a verdict.

**ENFSI** [RC-01]:
- requires "Balance, Logic, Robustness and Transparency";
- has reports address "the probability of the findings given the propositions … and not the probability of the propositions given the findings";
- gives an illustrative verbal scale running from "weak support" (likelihood ratio 2–10) to "extremely strong support" (likelihood ratio of 1,000,000 or more);
- warns that weak support for one proposition must not be read as support for the other.

**SWGDE image authentication best practice (2025)** [RC-02]:
- "By definition, it is impossible to prove a negative result". The most a thorough examination can conclude is that "it is unlikely the imagery has been manipulated or digitally created".
- Single-image manipulations may not be adequately detected, and "it is theoretically possible to generate a single frame of a person that is not detectable as virtual by a human".
- "Results should not be reported in terms of numerical probability without a proper scientific foundation".

**UK Forensic Science Regulator Code v2** (in force 2 October 2025) [RC-17]:
- names deepfake analysis explicitly;
- requires evaluative opinions to weigh "the propositions set out by all parties … in a balanced manner";
- lifts the ISO accreditation requirement for that media sub-activity.

**Validation:**
- PCAST (2016): "Without appropriate estimates of accuracy, an examiner's statement … is scientifically meaningless" [RC-18].
- NIST AI 100-4 (November 2024): detector evaluations are "most informative when the evaluation data includes outputs of models not seen" in training. False positives "can be extremely damaging", and NIST recommends reporting true-positive rates at very low false-positive rates such as 0.01%. Provenance "may contribute to trustworthiness but does not guarantee it" [RC-20].

**Applying likelihood ratios to deepfake detectors is early research.** In a peer-reviewed 2026 study, calibration improved results in-domain (Cllr 0.29 to 0.16), but AUC fell to 0.62–0.78 on unseen datasets. The authors say uncalibrated confidence scores "cannot serve as reliable probabilities". They also say the method "requires further validation across diverse real-world scenarios before practical forensic application" [RC-04]. A likelihood ratio calibrated on lab data may not transfer to a recompressed social-media file from an unknown generator.

**Design principles drawn from these sources:**
1. Do not state or imply "real" or "fake" as a finding. Name the competing propositions and give the strength of support. Do not give "the probability it is real" [RC-01, RC-02, RC-17].
2. If no meaningful alternative proposition can be stated, say so, and describe the evidence without evaluating it [RC-01].
3. "No evidence of manipulation" is not "authentic". The ceiling is "unlikely to have been manipulated or digitally created". Missing provenance is not, by itself, evidence of fabrication [RC-02, RC-26, RC-20].
4. Do not present raw detector percentages as probabilities. Show calibrated outputs validated on comparable content, with error rates at strict thresholds [RC-02, RC-18, RC-20, RC-04].
5. Keep integrity, authenticity, content, provenance facts and model estimates separate. C2PA's own UX guidance recommends progressive disclosure "instead of asserting definitive claims about an asset's authenticity" [RC-02, RC-26, RC-11].
6. Say what was edited and how much. "AI was used somewhere" is not "the event is fabricated", and light edits triggered "AI" labels at high rates in one test [RC-12, RC-26, RC-07].
7. Prefer several angles and independent sources over a single still or a single tool, and report when tools disagree [RC-02, RC-12, RC-11].
8. Analyse originals where possible. Do not draw conclusions from screenshots or recompressed copies. Do not publish heatmaps or error-level-analysis images as stand-alone proof [RC-11].
9. Define every label, and label falsity or harm separately from AI involvement [RC-07, RC-08].
10. Show "not checked" as distinct from "checked, nothing found", and do not default to a "real" badge [RC-22, RC-08].
11. Avoid generic "deepfakes are everywhere" warnings. In one experiment they made people disbelieve real videos [RC-23, RC-24].
12. Design against over-reliance. Flag out-of-domain or equivocal outputs, and keep a human verification step [RC-21, RC-28].
13. Communicate uncertainty "without furthering speculation", and correct false "it's fake" claims quickly [RC-25, RC-09].

---

## 6. Claims versus evidence

The four kinds of evidence answer different questions, so they are kept separate here.

### 6.1 Vendor marketing

**What it says:** headline accuracy of 95–99.5%, or superlatives with no number.

**Examples:**
- AI or Not: "98.9% accuracy" across images, text, video and deepfakes [VE-15].
- Resemble AI: "Up to 99.5%" [VE-19].
- DuckDuckGoose: "≈96%" on real-world deepfakes, and "0.01% FPR" [VE-21].
- Intel FakeCatcher: "96%" (2022) [VE-10].
- Superlatives: Sensity, "The Most Accurate…"; Hive, "industry-leading"; GetReal, "forensic-grade precision". Reality Defender, Pindrop, Clarity and Deep Media show no number [VE-12 to VE-22].

**How far it transfers to a social-media post:** unknown. None of the claims reviewed disclosed the test-set provenance, prevalence, threshold, false-positive rate at a fixed detection rate, post-processing conditions, or who ran the test.

### 6.2 Academic benchmarks

**What they say:** 90–99.9% accuracy on data like the training data.

**Examples:** GenImage, 99.9% in distribution [DS-03]; FaceForensics++, 99.26% on raw video [DS-11].

**How far they transfer:** limited, and specific to each dataset and date.
- Benchmarks age as generators change.
- Dataset shortcuts can inflate scores. In GenImage, real images are JPEG and fakes are PNG. Removing the size bias alone changed cross-generator accuracy from 71.7% to 82.7% [DS-04].

### 6.3 Independent and real-world evaluations

**What they say:**
- Open models scored near chance on one in-the-wild benchmark.
- The best commercial tools scored 0.78–0.89 accuracy on that benchmark.
- Named tools were strong on clean synthetic images but weaker under compression, under adversarial perturbation, and on AI edits of real photos.

**Examples:**
- Benchmarks: Deepfake-Eval-2024 [DS-01 = VE-01] and RA-Bench [DS-09].
- WITNESS Deepfakes Rapid Response Force case work [VE-02, VE-03]:
  - false positives (Myanmar, Ghana, Mexico);
  - a false negative after cropping;
  - inconclusive results linked to compression, unsupported language and darker skin tones.
- Named tests: see the list below [VE-27 to VE-29, VE-31 = RC-12].

**How far they transfer:** this is the most informative evidence available, but it is still limited. The test sets are small, the items were chosen by people who wanted them checked, vendors were anonymized in the largest benchmark, and some key tables are internally inconsistent [DS-01, DS-25].

### 6.4 Legal and regulatory findings

**What they say:**
- Accuracy claims must be substantiated.
- One court gave a consumer detector printout no weight.

**Examples:**
- **FTC v. Workado** (proposed April 2025; final order approved 3-0 on 28 August 2025) [VE-04, VE-05, VE-26]. Read status: FTC releases read in full.
  - A detector marketed as "98 percent" accurate was "just 53 percent" accurate on general-purpose content, according to testing the FTC cited.
  - The order bars accuracy claims without "competent and reliable evidence".
  - It concerned a text detector.
  - It is the only enforcement action found against a detector-accuracy claim. Operation AI Comply contained no detector cases.
- ***Head v John Doe*, 2026 BCSC 184 (Canada)** [LG-12, LG-16]. Read status: secondary reports only.
  - A "Deepfake Detected" printout from an online tool reportedly received no weight because its method was undisclosed.

**How far they transfer:**
- The FTC order shows a substantiation duty for marketing claims in the US.
- The Canadian ruling is one decision. It does not establish how courts elsewhere would treat detector output (see 7.1).

### 6.5 Named independent tests

**AI or Not:**
- Caught 100 of 100 clean Midjourney images, but only 3 of 10 after compression [VE-27, Bellingcat 2023].
- Had a 24.47% false-positive rate on human artworks [VE-28, CCS 2024].
- Flagged 13 of 15 lightly AI-retouched real photos as AI [VE-31, NewsGuard 2026].

**Hive:**
- Scored 98.03% with no false positives on clean art. Its miss rate rose from 3.17% to 32.44% under adversarial perturbation [VE-28].
- Caught 9 of 15 significantly AI-edited news photos [VE-31].

**Sightengine:**
- Scored 95.84–100% on text-to-image fakes, but 25.12% and 43.76% on two AI-edited-image subsets [VE-29, 2024].
- Caught 5 of 15 significantly AI-edited photos [VE-31].

**Chatbots:** Google's AI mode, Gemini and Copilot called AI images authentic, including one made with Google's own generator [VE-32, AFP, November 2025].

### 6.6 Vendor-cited studies are narrower than the marketing

- **Hive** cites a 2024 study as showing it "outperforms … human expert analysis".
  - That study covered 280 human and 350 AI art images.
  - Its authors concluded that "a combined team of human and automated detectors provides the best combination of accuracy and robustness", and found Hive weaker against adversarial perturbation [VE-12, VE-28].
- **Sightengine** cites a study of "80,000 images". The paper reports about 144,000, and Sightengine was weak on some edited-image subsets [VE-16, VE-29].

### 6.7 What would make a detector claim checkable

This 15-item checklist is synthesized from the sources cited in this section:
1. Dated, provenance-documented test sets kept separate from training data, with any detector-assisted labelling disclosed.
2. A stated definition of "AI-generated", with separate results for fully synthetic, AI-edited and AI-retouched content.
3. Named generators, with results on held-out generators and the measured lag after new releases.
4. Prevalence, and precision at realistic base rates.
5. The operating threshold, and how "inconclusive" is treated.
6. The false-positive rate at a fixed detection rate, the reverse, and a full confusion matrix.
7. Results after recompression, cropping, screenshots, overlays and adversarial perturbation.
8. Calibration.
9. Results by skin tone, language and recording channel.
10. A stress set of authentic photos: professional, smartphone, low-light, compressed and conventionally edited.
11. Model version, product tier and evaluation date, plus re-test cadence.
12. An independent tester, confidence intervals and attributable results.
13. Performance of the tool plus an analyst, against either alone.
14. How ground truth was set for any "live traffic" figure.
15. Retained substantiation, as the FTC's Workado order requires.

None of the vendor claims reviewed disclosed items 1, 4, 5, 6, 7 or 8.

One vendor page states limits that the others leave out. Sightengine's page says "no detector is 100% reliable", acknowledges a lag after new models launch, and tells users to apply judgment "even if the API returns … 99% or 1%" [VE-16]. The same page still headlines "the highest accuracy".

---

## 7. Legal and evidentiary value

These statements describe sources as read on 18 November 2026. They are not legal advice and not guidance on what to do.

Each claim carries one of these read-status labels:
- *primary, read in full*
- *primary, read in part*
- *via unofficial reproduction*
- *legal commentary or journalism, read in full*
- *secondary only, unverified*

Confirm claims marked unverified against the primary source before relying on them.

### 7.1 Courts and rules of evidence

**United States: rules of evidence**
- No federal evidence rule specific to deepfakes or AI-generated evidence was found to be in force [LG-01, LG-02, LG-51, LG-53]. *Read status: law-firm commentary and journalism, read in full; committee records not read.*
  - On 7 May 2026 the Advisory Committee on Evidence Rules reportedly declined to advance proposed FRE 707 on machine-generated evidence (published for comment August 2025 to February 2026), or any of three redrafts.
  - It reportedly also postponed a draft FRE 901(c) on deepfakes.
  - The earliest possible publication of any amendment was reported as August 2027.
- A Federal Judicial Center survey reportedly found that about 15 of more than 930 responding federal judges had seen a deepfake challenge [LG-01, LG-02]. *Read status: as reported in commentary read in full; the survey itself was not read.*

**Case law (as reported)**
- ***State v. Amyda*** (Iowa Supreme Court, 9 October 2026): "mere speculation" that a video is a deepfake was not enough to exclude it [LG-11, LG-59]. *Read status: legal commentary quoting the opinion, read in full; opinion not read.*
- ***Mendones v. Cushman & Wakefield*** (California Superior Court, 9 September 2025): the court imposed terminating sanctions after finding that exhibits were AI-generated deepfakes [LG-10]. *Read status: legal commentary quoting the order, read in full.*
- ***State v. Puloka*** (Washington Superior Court, King County, 2024): AI-enhanced video was excluded under the Frye reliability test [LG-14]. *Read status: secondary only.*
- ***Matter of M.S.*** (New York Court of Appeals, 17 February 2026): a divided court reportedly held that third-party "found" videos were insufficiently authenticated, citing deepfake risk [LG-13]. *Read status: secondary only, unverified. The vote count is reported inconsistently.*

**Detector outputs**
- The only ruling found on a consumer detector output is the Canadian *Head v John Doe* case (British Columbia). The printout reportedly received no weight because its method was undisclosed [LG-12, LG-16]. *Read status: secondary only, unverified.*
  - It is a single decision, outside the five jurisdictions reviewed. It does not establish how other courts would treat detector output.
  - No ruling on consumer detector output was found in the US, UK, EU, Australia or New Zealand. That absence is a search result, not a legal rule.
- Scholarship by Grimm, Grossman and co-authors describes AI-content detectors as having "proven unreliable and biased" [LG-43]. *Read status: abstract only.*
- At the Advisory Committee's 15 October 2026 meeting, an OpenAI representative reportedly said "no universal method exists to reliably detect every watermark or verify every image or video" [LG-02]. *Read status: journalism, read in full.*

**Provenance**
- No statute, rule or decision found in the five jurisdictions gives C2PA credentials or watermarks an automatic presumption of authenticity or a special evidentiary status.
  - Commentary suggests a manifest might support authentication through expert testimony.
  - How manifests fit the US self-authentication rules is unresolved [LG-48]. *Read status: secondary only.*
- The marking duties that do exist (EU AI Act Art. 50(2); California) are transparency obligations, not rules of evidence [LG-28, LG-49].

**Disclosure of a complainant's own checks**
- No authority was found on whether a complainant's own consumer-detector results could be disclosed or used against them. This is an open risk, not a finding.

### 7.2 Intimate-image and synthetic-media laws

Four questions are kept separate below:
- **(a) Offence elements.** Does it matter whether an image is genuine or fabricated?
- **(b) Removal eligibility.** What content does a duty or scheme cover?
- **(c) What a requester provides.**
- **(d) Process and enforcement.**

Removal is never guaranteed, and eligibility varies.

**United States.** TAKE IT DOWN Act, Public Law 119-12, enacted 19 May 2025 [LG-07, NC-19]. *Read status: primary, read in full.*
- **(a) Offence elements** [LG-07]. *Read status: primary, read in full.*
  - Criminal offences cover publishing authentic intimate depictions (with a privacy-expectation element), and publishing "digital forgeries".
  - A digital forgery is created or altered with software or AI and, "when viewed as a whole by a reasonable person, is indistinguishable from an authentic visual depiction".
  - The adult maximum is 2 years.
  - Realism, not provenance, is an element of the forgery track.
- **(b) Removal eligibility** [LG-07, LG-04]. *Read status: primary text read; the coverage reading is partly inferential.*
  - The platform duty covers "intimate visual depictions" published without consent.
  - Because a digital forgery is defined as a kind of intimate visual depiction, forgeries appear to be covered, which is consistent with FTC guidance.
  - Whether non-realistic fakes are covered depends on a cross-referenced definition (15 U.S.C. 6851) that was not read.
- **(c) What a requester provides** [LG-07, NC-19]. *Read status: primary, read in full.*
  - A signature, information to locate the depiction, "a brief statement that the identifiable individual has a good faith belief that [the depiction] is not consensual", and contact details.
  - The request does not ask for a detector verdict or proof of authenticity.
  - Platforms must remove within 48 hours of a valid request, and make reasonable efforts against known identical copies.
  - Good-faith removal is protected "regardless of whether the intimate visual depiction is ultimately determined to be unlawful or not".
- **(d) Enforcement** [LG-03 to LG-05]. *Read status: FTC releases and guidance, read in full.*
  - FTC enforcement of the platform duties began on 19 May 2026, with a complaint portal.
  - The FTC sent warning letters to 15 platforms and, on 20 May 2026, to 12 "nudify" services.
  - The reported civil penalty is up to $53,088 per violation.
  - No FTC enforcement action was found as of November 2026.
- **Critiques.** CDT, EFF and others point to no counter-notice process, no penalty for false requests, and incentives to over-remove [LG-46, LG-47]. *Read status: secondary only.*
- **DEFIANCE Act** (civil remedy). It passed the Senate on 13 January 2026; the House companion had not moved [LG-08, LG-09]. *Read status: secondary only, unverified.*

**England and Wales offences; UK platform duties**
- **(a) Offence elements**
  - The sharing offence (SOA 2003 s.66B, in force 31 January 2024) covers images that "show, or appear to show" a person in an intimate state [LG-18]. *Read status: primary, read in full.*
    - "Photograph or film" includes an image "whether made or altered by computer graphics or in any other way, which appears to be a photograph or film" (s.66A(5)).
    - Genuine and fabricated images are both covered.
  - The offence of creating a "purported intimate image" (s.66E, in force 6 February 2026) applies only to images that are "not, or not only" a genuine photograph or film. Here, being fabricated or altered is part of the definition [LG-17]. *Read status: primary, read in full.*
  - Making or supplying nudification tools (s.66I) has been an offence since 29 June 2026 [LG-54]. *Read status: primary, read in full.*
  - The Crime and Policing Act 2026 received Royal Assent on 29 April 2026 [LG-55]. *Read status: primary, read in full.*
- **(b) Removal eligibility and (c) what a requester provides** [LG-19]. *Read status: primary, read in part.*
  - The Crime and Policing Act 2026 adds a 48-hour intimate-image takedown duty on user-to-user and search services, in force since 29 June 2026.
  - It is triggered by a report declaring three things:
    - that the content is intimate image content (by reference to s.66B);
    - that the reporter is the person shown or acts for them;
    - that the report is made in good faith.
  - The provider may decline if it considers the content is not intimate image content.
- **(d) Regulator**
  - Ofcom has issued a statement recommending hash-matching for intimate image abuse that covers explicit deepfakes [LG-21, NC-42]. *Read status: secondary only, unverified.* Reported dates differ (May or June 2026), and whether the code measures are in force is unconfirmed. One extract says 30 September 2026.
  - Ofcom opened an investigation into X over Grok on 12 January 2026. It was still open in the sources found [LG-22, NC-15]. *Read status: secondary only, unverified.*
  - Ofcom issued non-binding guidance on violence against women and girls (November 2025), and fined a nudify site £50,000 for age-assurance failures [LG-23, LG-24]. *Read status: secondary only.*

**European Union**
- **(a) Offence elements**
  - Directive (EU) 2024/1385 Art. 5(1)(b) requires Member States to criminalise "producing, manipulating or altering and subsequently making accessible to the public" material that "makes it appear as though" a person is engaged in sexually explicit activities. The conduct must be without consent and likely to cause serious harm. The transposition deadline is 14 June 2027 [LG-27]. *Read status: primary, read in full on EUR-Lex.*
  - Commentators note that nudified images and private sharing may fall outside this offence [LG-27, LG-29]. *Read status: secondary.*
- **AI Act**
  - Art. 50(4): deployers must disclose deepfakes, from 2 August 2026 [LG-28]. *Read status: read in full via unofficial reproduction.*
  - Regulation (EU) 2026/1744 bans AI systems that generate "realistic" non-consensual intimate images of identifiable people (Art. 5(1)(ba)), and systems that generate CSAM (Art. 5(1)(bb)), from 2 December 2026 [LG-56]. *Read status: primary, read in full on EUR-Lex.* The ban has a realism threshold.
- **(b)–(d) Removal and process**
  - The Directive provides for removal orders (Art. 23) [LG-27]. *Read status: primary, read in full.*
  - This review did not separately verify the DSA notice-and-action route. Do not rely on this report for its current procedure.
  - The Commission opened DSA proceedings against X over Grok on 26 January 2026 [NC-16]. *Read status: Commission page, read in full.*

**Australia**
- **(a) Offence elements.** Criminal Code s.474.17A (since 3 September 2024) covers material "depicting, or appearing to depict" an adult. It is irrelevant whether the material was "created, or altered in any way, using technology", and creating or altering it is an aggravating factor [LG-32, LG-57]. *Read status: secondary only; the operative text was not available.*
- **(b) Removal eligibility.** The Online Safety Act image-based abuse scheme covers images that "show, or appear to show" a person [LG-36]. *Read status: secondary only.* eSafety says intimate images include digitally altered images [NC-10]. *Read status: extract.*
- **(d) Enforcement**
  - In *eSafety Commissioner v Rotondo (No 4)* [2025] FCA 1191, the court imposed a A$343,500 civil penalty for posting deepfake intimate images [LG-33]. *Read status: secondary only.*
  - A Digital Duty of Care Bill is pending [LG-35]. *Read status: secondary only.*

**New Zealand (tentative)**
- Commentators argue that the intimate-visual-recording offences (Crimes Act s.216G ff.; HDCA s.22A) are built on a "recording", so they may not clearly cover synthetic images.
- Netsafe says the HDCA civil regime covers harmful AI images.
- These views may concern different provisions. This is legal analysis from secondary sources, not a settled rule [LG-37, LG-39].
- The Deepfake Digital Harm and Exploitation Bill would extend coverage to images "created, synthesised or altered". It passed first reading on 20 May 2026; its later stage is unconfirmed [LG-37, LG-58]. *Read status: secondary only, unverified.*

**Platform and NGO processes** (these are policy, not law)
- **Google Search.** Its route for fake explicit imagery asks the requester to state that "The content is fake and falsely depicts you". Real images go through a different category on the same page. Someone who cannot tell whether an image is fabricated or a stolen real photo has to choose between them [NC-24]. *Read status: policy page, read in full.*
- **Meta.** Meta removes AI-generated or manipulated nudity "regardless of photorealism" under its adult-nudity rules, with exceptions [NC-27]. *Read status: read in full.*
  - It still handles AI nudes of real people under a "derogatory sexualized photoshop" rule.
  - It is "assessing feasibility" of treating AI generation as a signal of non-consent.
  - It does "not expect" to replace "derogatory" with "non-consensual".
- **Microsoft.** Microsoft says it applies its NCII policy "consistently across real and synthetic content" [NC-26]. *Read status: partly read via extract.*
- **X.** X's policy covers AI-generated NCII [NC-28]. *Read status: extract.* A 2024 audit found that copyright (DMCA) reports removed 25 of 25 test images of synthetic personas, against 0 of 25 through the NCII route within three weeks [NC-31]. *Read status: preprint, read in full.* The audit predates TAKE IT DOWN enforcement.
- **StopNCII** [NC-21]. *Read status: FAQ, read in full.*
  - Its definition of NCII includes deepfakes and synthetic images.
  - It requires that you are the person shown, were 18 or older in the image, and have access to the image.
  - Hashing happens on the device, and it works only with partner platforms.
- **NCMEC Take It Down** [NC-22]. *Read status: FAQ, read in full.*
  - It is for images taken when the person was under 18, and the image must already be on the device.
  - The FAQ says "Do not download or share any nude, partially nude or sexually explicit image or video in order to submit".
  - The FAQ does not mention AI-generated images.

**What this means across the regimes reviewed**
- A removal request does not require a detector verdict or proof of authenticity.
- Eligibility depends on identity, consent, and definitions specific to each jurisdiction or policy. Removal is not guaranteed.
- Authenticity classifications still come in at several points:
  - some platform intake routes, such as Google's;
  - some offence definitions: UK s.66E, the US forgery track, the EU ban's "realistic" threshold, and aggravation in Australia;
  - possibly New Zealand's current criminal law.
- The statutory request processes reviewed do not ask for a consumer detector verdict.

---

## 8. Users, needs and the existing market

### 8.1 Who needs authenticity information, and for what

- **The public wants to know, and doubts its own ability.**
  - In Pew's June 2025 survey (n = 5,023), 76% of US adults said it is "extremely or very important" to tell whether pictures, videos and text were made by AI or by people. 53% were not confident they could [MK-01].
  - Concern about fake content online averaged 62% across 48 markets in 2026, up 4 points. The Reuters Institute links the rise partly to deepfakes and "AI slop" [MK-02, MK-03].
- **People mostly check through trusted sources, not detectors.**
  - First ports of call: trusted news (38%), official sources (35%), search engines (33%), fact-checkers (25%).
  - Weekly chatbot use for news rose to 10%, but only 20% trust chatbot answers [MK-02, MK-03].
- **Fact-checkers see the problem but are financially fragile.** In the 2026 IFCN survey of 141 signatories [MK-18, MK-49]:
  - 49.6% called deepfakes and synthetic media a major challenge;
  - 53.3% used AI tools in their work;
  - 76% described their finances as "vulnerable or in crisis";
  - 30 fact-checking outlets closed and 10 opened in 2025.
- **Practitioners need more than a score.**
  - Fact-checkers "frequently report difficulty interpreting confidence scores", and probabilities do not say what was altered.
  - In one study, journalists over-relied on tool results that matched their first impressions [MK-04, MK-05, MK-19].
  - Practitioners report failures on compressed or re-recorded files, noisy or radio audio, local languages, darker skin tones, and people with little reference footage [MK-04, MK-05, VE-02].
- **People targeted by NCII prioritise removal, being believed, control and support** (section 9.2).

### 8.2 Competitive landscape (as reviewed; not exhaustive)

**Free or freemium consumer detectors** [MK-07 to MK-10, MK-46 to MK-51]
- Hive: free web detector and Chrome extension; gives an AI-or-not verdict and a predicted generator.
- AI or Not: freemium, plus a business API.
- Is It AI: web tool.
- Illuminarty: free, $10 or $30 a month, or enterprise.
- Sightengine: developer API and demo.
- *Notes:* maintenance is uneven; Hive's extension was last updated 12 January 2025 and is rated 3.1/5 from 414 ratings [MK-10]. In one 2026 test, false-positive rates on authentic photos ranged from 0% to 40% per tool [RC-12].

**Security-suite features** [MK-11, MK-21]
- McAfee's and Norton's deepfake features analyse media on the device, on specific AI PCs.
- *Notes:* both target scam audio and video. No check of still images or intimate-image cases was found.

**Platform-native checks**
- Google Gemini checks SynthID plus Content Credentials. It is free with sign-in and has daily quotas [MK-06, PV-09].
- YouTube likeness detection protects enrolled creators, not viewers [MK-59 to MK-61].
- Platform AI labels (Meta, TikTok, YouTube, LinkedIn, X) were applied to roughly 14–67% of AI posts in audits [PV-17, PV-18].
- *Notes:* each answers a narrow question, such as "is this from our generator?"

**Provenance tools**
- Content Credentials Verify (now verify.contentauthenticity.org) and Adobe's Content Authenticity inspection tools [MK-30, MK-31, MK-57].
- Truepic, Digimarc and camera makers.
- *Notes:* free, but few files carried credentials where measured (0.43% in one crawl) [PV-25].

**Enterprise and forensic** [MK-22, MK-23]
- Reality Defender: $33M expanded Series A, October 2024.
- GetReal Security: $17.5M Series A, March 2025. An enterprise platform plus human forensic analysts; no self-serve tier.
- Also in this segment, not researched in depth: Sensity, Pindrop, Clarity, Deep Media, Intel, Amped and Magnet.
- *Notes:* verified funding in this review went to enterprise, fraud, identity and government buyers. Pricing is on request, and credible offerings include human analysts.

**NGO and academic** [MK-14, MK-17, MK-04, MK-56, MK-58]
- TrueMedia.org: its free service was sunset in January 2025. Since 16 April 2025 it has run as a closed beta at Georgetown's McCourt School ("Non-partisan, open source, free"), with human forensic review.
- WITNESS Deepfakes Rapid Response Force: expert escalation for frontline partners.
- The InVID-WeVerify plugin and the University at Buffalo DeepFake-o-meter.
- *Notes:* public-interest supply has been fragile; free tools have shut down or become more expensive [MK-04, MK-14].

**Independent evaluation**
- Deepfake-Eval-2024, with vendors anonymized under contract [DS-01].
- RA-Bench, an academic preprint [DS-09].
- NIST GenAI. No public image-discriminator results were found, and its rules bar public cross-team comparison without consent [DS-30, DS-31, VE-23].
- DARPA's AI FORCE challenges, now run by UL Research Institutes' DSRI [DS-27, DS-28].
- WITNESS TRIED, which is a framework rather than a test lab [VE-02].
- NewsGuard's ad hoc tests [RC-12].
- *Notes:* this review found no public, attributable, regularly refreshed evaluation of named tools on social-media-processed content. That gap motivates the hypothesis in section 13.

### 8.3 Privacy and data handling (what published terms say about uploads)

- **Sightengine** (policy updated 6 November 2026): the most protective found. Content is "deleted once it has been processed", API content is "only used to return results to you", and processing is mostly in the EU [MK-46].
- **Is It AI** (October 2026): images "may be stored anonymously to improve our detection models", and media are sent to a third-party detection provider [MK-07].
- **AI or Not:** says nothing about uploaded images or video; retention is "as long as you have an open account" [MK-08, MK-47].
- **Hive:** its privacy link now redirects to a different company policy ("Deploy") that does not mention detector uploads [MK-48].
- **Illuminarty:** policy dated 2022; images kept "only for the duration necessary" [MK-51].
- **Google Gemini verification** [MK-45, MK-06]:
  - The upload becomes a Gemini chat.
  - "A subset of chats are reviewed by human reviewers".
  - Reviewed chats are kept "for up to 3 years, even if you delete them".
  - Google asks users not to enter confidential information.

No consumer tool reviewed checks still images on the device. For sensitive or intimate media, any upload-based check creates copies whose retention the person cannot control (section 9.4).

### 8.4 Unmet needs with evidence behind them

The unmet needs documented in the sources come mainly from practitioners, not consumers [MK-04, MK-05, MK-18, MK-19]:
- robustness on the formats people actually share;
- coverage of the Global Majority (languages, accents, darker skin tones, local public figures);
- explainable, plain-language and calibrated outputs;
- affordability;
- maintained tools with honest status;
- clear retention terms;
- a route to human experts.

The groups with the strongest documented needs (fact-checkers, frontline NGOs) report the weakest finances. A consumer niche for privacy-safe guidance that needs no upload of sensitive media is a hypothesis: no direct user research showing demand was found.

---

## 9. Non-consensual fake intimate images (NCII): what targeted people need from authenticity information

This section draws only on published research, NGO, regulator, platform-policy, court and journalism sources. No intimate media was sought or viewed, and no service that produces it was visited.

### 9.1 Scale and pattern

Prevalence is measurable and not rare. Estimates vary about threefold with definition, age group and year.
- **Adults, 10 countries.** A survey of 16,693 adults (fieldwork May–June 2023) found 2.2% reporting victimisation and 1.8% reporting perpetration [NC-01].
- **Adults, Australia, UK and US.** A survey with 2024 fieldwork, published in 2026 (n ≈ 7,230), found:
  - 6.9% reporting AI-generated image-based sexual abuse since age 18;
  - 15% reporting abuse involving digitally altered images of any kind [NC-02].
  
  This study was funded by Google, a potential conflict of interest. Only its abstract page and press release were read.
- **Young people.**
  - Thorn (2025, ages 13–20): 1 in 17 had been targeted [NC-03].
  - CDT (US, 2023–24 school year): 15% of high-school students knew of deepfake NCII at their school [NC-05].
  - Internet Matters (UK, 2024): 13% of teens reported some "experience" with nude deepfakes [NC-06]. *Read status: extract.*
  - Common Sense Media (US, July 2026): 18% of teens had made AI sexual imagery or knew someone who had [NC-07].
- **Who is targeted is contested.**
  - Adult self-report surveys find more men reporting victimisation: 10.2% of men against 3.8% of women in the three-country study. Women report broader and more severe harm.
  - School and regulator data find that mostly girls are depicted. In eSafety's data, 4 in 5 under-18 reports concerned girls [NC-01, NC-02, NC-05, NC-08].

**Production is industrialised.** Traffic and revenue figures in this paragraph are third-party estimates, mostly read only in part or as extracts [NC-11 to NC-14].
- In one month of 2023, "nudify" services drew 24 million unique visitors to 34 sites.
- A July 2025 analysis estimated that 85 such sites "may be worth up to $36 million a year". Of those, 62 were hosted or served by major cloud or CDN providers, and 53 used a major tech company's sign-in.

**AI image editing inside X (Grok), late December 2025 to January 2026.** It produced sexualised edits of real people at scale.
- CCDH estimated about 3 million sexualised images in about 11 days. The estimate came from a model-classified sample that did not assess consent [NC-18]. *Read status: extract.*
- Responses:
  - Ofcom opened an investigation on 12 January 2026 [NC-15, LG-22]. *Read status: secondary/extract.*
  - The European Commission opened DSA proceedings on 26 January 2026 [NC-16]. *Read status: Commission page, read in full.*
  - California's Attorney General issued a cease-and-desist on 16 January 2026 [NC-17]. *Read status: extract.*
  - Indonesia and Malaysia temporarily blocked Grok.

### 9.2 What targeted people say they need

Across the studies reviewed, targeted people prioritise [NC-32, NC-33, NC-35, NC-36, NC-48, NC-05, NC-04]:
- fast removal, ideally with content hidden while a report is reviewed;
- stopping re-uploads and copies;
- being believed without heavy proof burdens;
- not having to find, re-view and re-submit the material;
- clear, human communication;
- control, anonymity and privacy;
- emotional support;
- evidence and legal options that do not depend on the targeted person doing forensic work.

Studies also document institutional failures:
- content left up during review;
- opaque decisions;
- police unable or unwilling to act;
- schools that punished perpetrators but rarely helped victims get content removed. In CDT's survey, 5% of US teachers said their school had helped victims get deepfakes removed [NC-05].

**None of these needs, as reported, is a verdict on whether the image is AI-generated.**

### 9.3 Removal requests generally do not depend on proving authenticity, but eligibility varies

In the routes reviewed, a request rests mainly on identity ("is it you?") and consent ("did you consent?"). It does not rest on a detector verdict or on proof that an image is fake or real. Eligibility, scope and outcomes differ by jurisdiction and platform, and removal is not guaranteed (section 7.2 gives read status).

**Routes that do not ask for a detector verdict:**
- **US TAKE IT DOWN request.** A signed request, information to locate the image, and a good-faith statement of non-consent [NC-19, LG-07]. *Read status: primary, read in full.*
- **StopNCII.** It includes deepfakes and synthetic images in its definition of NCII, and hashes images on the person's own device ("the images will not leave your device"). It requires the person to hold the image [NC-21]. *Read status: FAQ, read in full.*
- **Microsoft.** It says it applies its NCII policy "consistently across real and synthetic content" [NC-26]. *Read status: partly via extract.*
- **Meta.** It removes AI-generated or manipulated nudity "regardless of photorealism" under its adult-nudity rules, with exceptions [NC-27]. *Read status: read in full.*
- **eSafety (Australia).** Its definition of an intimate image includes digitally altered images [NC-10]. *Read status: extract.*
- **UK schools guidance.** It applies the same law and safeguarding response to AI-generated nudes of children as to real ones [NC-41]. *Read status: read in full.*
- **UK police messaging.** It says sharing without consent, "whether they are real images or not, is deeply violating" [NC-38]. *Read status: read in full.*
- **Ofcom (UK).** Its 2026 hash-matching measure covers explicit deepfakes. Whether it is in force is unconfirmed [NC-42]. *Read status: extract, unverified.*

**Where authenticity still enters, or creates friction** [NC-24, NC-27, NC-31, NC-19, NC-21, NC-22]:
- **Google Search's route for fake imagery.** The requester must state that "The content is fake and falsely depicts you", while real images use a different category on the same page. A person who cannot tell whether an image is fabricated or a stolen real photo must still choose a category.
- **Meta's bullying rule.** Meta keeps AI nudes of real people under a "derogatory sexualized photoshop" bullying rule.
  - In July 2024 the Oversight Board recommended treating AI generation as a signal of non-consent, and replacing "derogatory" with "non-consensual".
  - Meta is "assessing feasibility" of the first and does "not expect" to make the second.
- **The copyright route.** In a 2024 audit of X, copyright (DMCA) reports removed 25 of 25 test images, against 0 of 25 via the non-consensual-nudity route within three weeks. The test used synthetic personas, not real people.
- **Criminal offences.** A US federal "digital forgery" must be "indistinguishable from an authentic visual depiction" to a reasonable person. That makes realism a criminal element. Some UK, EU and Australian provisions also distinguish genuine from fabricated or altered material (section 7.2).
- **Hash tools.** They work only on images already on the person's device, and they can miss edited variants. Synthetic abuse often involves images the targeted person has never received, and generators can produce many variants.

### 9.4 Where an authenticity verdict can hurt

Both directions of a verdict can harm a targeted person.

**"It's just fake" minimises the harm.**
- 23% of US teens think AI nudes are less harmful than real ones "because no one gets hurt" [NC-07].
- In Thorn's survey, 16% saw deepfake nudes as not harmful or harmful only in some contexts, and 28% of that group cited the images being "not real" [NC-03].
- Adults across 10 countries rated real non-consensual imagery as worse than synthetic equivalents [NC-01].
- In England and Wales, most adults rated being the victim of a sexual deepfake as less harmful than phone theft or scams. About 1 in 4 felt "nothing wrong with, or are neutral about" creating and sharing sexual deepfakes without consent [NC-38].
- Perpetrators describe the abuse as "just a joke" [NC-34]. *Read status: abstract and press only.*

**"It looks real" feeds disbelief and leverage.**
- Thorn: "When deepfakes are involved, the fear of not being believed can intensify". In Thorn's data, about 10% of financial-sextortion reports involved inauthentic images [NC-04].
- Offenders alter benign photos of real children to coerce them [NC-40].
- A detector's "likely real" or "no manipulation detected" output could be read by family, a school or an employer as confirmation that the person took or sent the image. That includes ordinary false negatives on new generators. **This harm is inferred.** No documented case was found of a school, police force or employer using a detector output against a victim.

**"It's AI" can be used to deny real images.** A UK barristers' training deck warns that genuine images can be dismissed as possibly AI-generated, undermining a complainant [NC-49]. *Read status: extract only.* No documented NCII case of a successful "it's AI" defence was found.

**Checking authenticity can re-expose people and create risk. The guidance differs by age and context.**
- **Where anyone shown may be under 18,** the guidance reviewed is consistent [NC-10, NC-22, NC-41]:
  - do not view, download, make new copies of, or forward the images;
  - do not upload them anywhere;
  - record non-image details instead: URLs, usernames, dates and report reference numbers.

  UK schools guidance says staff "must not intentionally view" such images and should "never copy, print, share, store or save them; this is illegal" [NC-41]. NCMEC says "Do not download or share any nude, partially nude or sexually explicit image or video in order to submit" [NC-22].
- **For adults, the guidance reviewed is less uniform.**
  - eSafety's evidence guidance emphasises recording URLs, usernames and dates, and involving a trusted person. The extract reviewed also says not to screenshot illegal and restricted content [NC-10]. *Read status: extract; exact scope for adult images unconfirmed.*
  - Hash-based services work only from an image already on the person's device [NC-21].
  - The sources reviewed do not support a blanket rule against adults keeping evidence. Following the guidance of the specific service, helpline or legal adviser involved is the safer course.
- **Uploading intimate images to third-party "deepfake detectors"** creates copies with unclear retention. Several free detectors' published terms either allow retention and model training or say nothing about uploads (section 8.3). For images of minors, uploading may also create legal risk for whoever uploads. Avoiding such uploads is a recommended safety practice, not a universal legal rule. No NGO statement specifically about detector sites was found.
- **UK police** are exploring image hashing so cases can proceed without the image being shown repeatedly [NC-38].

### 9.5 Authenticity information that can genuinely help, and who should produce it

Authenticity information helps where a specific decision turns on it:
- a prosecution where realism or fabrication is an element;
- rebutting an "it's AI" claim about a genuine image;
- attribution: whose device made the edit, and from which source photo;
- finding copies.

[NC-50, NC-51, NC-23, NC-42, NC-01, NC-19, NC-48]

The forms best supported in the sources are produced by institutions with lawful access:
- device forensics in investigations. In one 2026 Australian sextortion prosecution, investigators found both the edited and the original benign photos on the accused's phone [NC-50]. *Read status: extract.*
- platform duplicate and hash matching;
- provenance marks applied when content is generated;
- qualified expert evidence with documented error rates.

A probabilistic consumer detector score is weaker evidence than any of these, and relying on one tends to shift the burden back onto the targeted person. Helping someone locate the benign, non-intimate source photo may help rebut "this is real". It should be optional, supported, and never require uploading the intimate image.

### 9.6 Design principles from trauma-informed and safety-by-design frameworks

The frameworks reviewed:
- Chayn's trauma-informed design principles: safety, agency, equity, privacy, accountability, plurality, power-sharing, hope [NC-45]. *Read status: extract.*
- Chen et al.'s trauma-informed computing principles (CHI 2022) [NC-46]. *Read status: abstract-level.*
- eSafety's Safety by Design [NC-47]. *Read status: extract.*

NCII-specific research adds further practices [NC-32, NC-33]:
- presumptive removal during review;
- reduced re-exposure;
- human support;
- status updates;
- not penalising reporters.

Applied to any authenticity-related tool a targeted person might meet, these suggest the following design recommendations. They are not legal rules:
1. **Do not require uploads of intimate images.** Where content may depict a minor, do not process the image. Point to specialist routes, such as NCMEC Take It Down, eSafety or other help the person chooses.
2. **Lead with routes that need no detector verdict.** For example: "You can ask for removal without proving whether this is real or AI-generated. What qualifies depends on where you are and which platform."
3. **Do not give a binary real/fake verdict on intimate content.**
4. **Use language that rejects minimisation.** Non-consensual sexual imagery is abuse whether real or fabricated.
5. **Minimise re-exposure, and allow a trusted person to act on the person's behalf.**
6. **Keep data to a minimum:** no accounts and no retention unless the person chooses otherwise.
7. **For disputes with a court, school or workplace, point to evidence from institutions and qualified experts** rather than self-generated scores.

No source evaluated a trauma-informed authenticity tool [NC-45, NC-46, NC-47].

---

## 10. Misuse and trust risks

1. **Verdicts used to "debunk" authentic media.**
   - **October 2023.** A free online detector labelled as AI-generated an authentic war photo shared by Israel's official accounts. Hany Farid found "no signs it was created by AI" [VE-06, RC-10]. Secondary sources name the tool; the article read does not.
   - **March 2026.** Heatmaps, error-level-analysis screenshots, a "normal map" render and chatbot outputs were used to brand authentic Iran-war news photos as fabricated [RC-11].
     - The targets included photos published by The Telegraph, The Guardian and The New York Times.
     - One thread passed 600,000 views on X.
     - Experts called it "forensic cosplay", and the NYT said the analysis "misrepresents standard image compression behavior".
   - **2026.** An authentic Netanyahu "proof-of-life" café video was circulated with a detector result reading "likely to be AI-Generated" at 96.9%, to claim he had been killed [RC-12].
   - **No good detector is needed for this.** Free tools, chatbots and generic filters supplied enough technical-looking "proof" in these cases [RC-11].
   - **NewsGuard's May 2026 test** ran five consumer tools on 15 authentic Iran-war photos from Reuters, AP, the NYT, The Guardian and Google Earth [RC-12]:
     - Authentic photos flagged as AI: ScamAI 6 of 15, ZeroGPT 3, AI or Not 1, Hive 0, Sightengine 0 (13.33% across all tools).
     - Lightly AI-edited versions were labelled "AI-generated" in 27–93% of runs, depending on the tool.
     - At least one tool disagreed with the others on 35 of 45 images.
     - Sightengine caught 33% of significantly AI-edited images.
     - Hive cleared every authentic photo in this test, yet a Hive score was used against the authentic Netanyahu video. Results on one test set did not predict the next case.
2. **The "liar's dividend": real evidence dismissed as fake.**
   - **Experiments.** Five preregistered experiments (N = 15,287; 2021–2022 data) found that false claims of misinformation raised politicians' support by about 0.17–0.21 SD for text scandals, but were "largely ineffective against video evidence". Fact-checks cut the gain to negligible [RC-09]. The authors themselves caution that the protection video gave may not last as generated video becomes photoreal.
   - **Field case.** A Ghanaian candidate dismissed a genuine multi-angle video as a deepfake. WITNESS: "bad actors don't need to fake media—they just need to claim it's fake", and it is "inherently more difficult to prove lack of manipulation" [VE-02, VE-03].
   - **August 2024.** Donald Trump falsely claimed a Harris rally crowd photo was AI-faked. Journalists at the scene and a forensic analysis found it authentic [RC-27]. *Read status: headline and summary level.*
   - **Awareness campaigns can feed the problem.** Chesney and Citron argue the liar's dividend "flows, perversely, in proportion to success in educating the public about the dangers of deep fakes" [RC-24]. In one experiment, deepfake warnings did not improve detection but "consistently induced [participants] to believe the videos they watched were fake, even when they were real" [RC-23]. *Read status: abstract only.*
3. **False reassurance.**
   - A "real" or "not detected" result is limited evidence (5.5).
   - Cropping or downscaling has flipped a detector's verdict from fake to authentic [VE-02].
   - In NewsGuard's test, one tool caught a third of significantly AI-edited images [RC-12].
   - General-purpose chatbots, now a common way people "check", called AI images authentic, including one made with Google's own generator. In a Tow Center study reported by AFP, all seven chatbots tested failed to identify the provenance of 10 real news photos [VE-32].
   - In Groh et al. (PNAS, N = 15,016), "inaccurate or equivocal model predictions led participants astray in 8 of 10 instances". On one political deepfake that the model scored as only 2% likely to be fake, human accuracy fell from 56% to 34% [RC-21, DS-17].
   - No documented case was found in which a false "real" verdict enabled fraud or other harm. The risk rests on measured false-negative rates.
4. **Labels can lower belief in true content.**
   - "AI-generated" labels lowered belief in true and human-made headlines too, by about a third as much as a "False" label. Defining the label removed the penalty [RC-07].
   - On misleading AI images, any label cut belief by 0.21–0.25 SD. "AI-Generated" alone cut belief by 0.14 SD, with no significant effect on engagement. The authors warn of an "implied authenticity" effect for unlabelled content [RC-08].
   - Meta renamed its "Made with AI" label to "AI info" on 1 July 2024. It said labels on content with minor AI retouching "weren't always aligned with people's expectations" [VE-30, RC-13].
   - The tools tested do not share a definition of "AI-generated". Five tools flagged between 27% and 93% of lightly retouched authentic photos as AI. NewsGuard: "There is no industry consensus on what counts as AI-generated content" [VE-31].
   - Automated labelling at platform scale, with non-zero false positives, would discount some authentic content. That is an inference from the findings above.
5. **Harm to people targeted by NCII.** Minimisation, disbelief, re-exposure, and privacy and legal risk from uploads (section 9.4).
6. **Privacy of uploaded media.** Free detectors' published terms vary, and some allow retention or model training (section 8.3). For sensitive media, the act of checking can itself be a disclosure.
7. **Over-removal and abuse of takedown systems.** Civil-liberties groups argue that the TAKE IT DOWN Act's design invites over-removal: no counter-notice, no penalty for false requests, and immunity for good-faith removal [LG-04, LG-46, LG-47]. This is a risk to legitimate speech. It is not a barrier to targeted people requesting removal.
8. **Detector output mistaken for proof.**
   - In the one ruling found (Canada; secondary reports only), a detector printout received no weight [LG-12, LG-16].
   - That does not establish how other courts would treat such output. It does suggest that unexplained consumer scores are weak evidence compared with institutional or expert evidence.
   - Whether a complainant's own detector results could be disclosed or used against them is untested in the sources found.

---

## 11. A practical, privacy-conscious workflow

This workflow is synthesized from several sources [MK-52 to MK-54, MK-05, MK-04, MK-06, RC-02, NC-10, NC-21, NC-22]:
- SIFT;
- the Verification Handbook chapter by WITNESS;
- Bellingcat;
- the Tow Center;
- WITNESS TRIED;
- Google's guidance;
- the forensic standards above;
- NGO guidance on intimate images.

It is guidance on reasoning, not a verdict procedure.

### 11.1 For a photo or video you have come across

1. **Pause.** Don't reshare, and don't "debunk" in public yet.
2. **Name the question and the decision.** Do you need to know whether it was made with AI, whether it was altered, or whether it shows what the caption says? What would you do differently depending on the answer?
3. **Check the source and context. This needs no upload.**
   - Who posted it, and what is the account's history?
   - Where is the earliest copy you can find through text and handle searches?
   - Does trusted reporting, an official source or a fact-checker cover it?
   - What was cut, and what happened before and after? "The caption could be misleading" [MK-52].
4. **Look for corroboration:** other angles and independent footage of the same event, consistency across images, and disclosures. A single still with no other angle is a reason for caution, not proof of fakery [MK-53, RC-02].
5. **Read labels for what they are.** A platform AI label or a visible watermark signals AI involvement. Its absence is not evidence either way (section 4.6) [PV-17, PV-18, PV-24].
6. **Check provenance if you hold the original file and it is not sensitive.**
   - Interpret the result using section 4.6. A trusted credential speaks to the signer and to integrity since signing, not to truth.
   - Web verifiers and Gemini involve uploading the file. Gemini chats may be reviewed by humans and kept for up to three years [MK-06, MK-45, MK-31].
7. **If you use detectors at all, use them last, and only on non-sensitive media.**
   - Check the tool's data terms first (8.3).
   - Treat the output as one weak signal. Remember base rates (5.5), and that tools often disagree [RC-12].
   - Do not treat "not detected" as "authentic".
   - Do not post a detector screenshot as proof.
8. **Consider expert help when:**
   - tools disagree, or flag material known to be authentic;
   - the media are degraded, compressed or not in English;
   - the stakes are legal or the potential harm is high;
   - someone needs to show that an item is authentic against a "that's fake" claim.

   Options include professional fact-checkers, expert networks such as WITNESS's, qualified forensic examiners, and legal advice. Whether to involve police depends on the situation, the location and the person's choice [MK-04, MK-05].
9. **Report findings, not a verdict.** Say what you checked, what supports which explanation, and what remains unknown (section 5.6).

### 11.2 If you are the person shown in a fake intimate image

This is a short note about authenticity questions. It is not legal advice or a full support guide, and what applies depends on where you are and which platforms are involved.

- **You can ask for removal without first getting a detector verdict.**
  - The routes reviewed, including platform reporting and statutory processes in some jurisdictions, rest on identity and consent rather than proof of authenticity (sections 7.2 and 9.3).
  - Eligibility and outcomes vary, and removal is not guaranteed.
  - Some routes ask you to say whether an image is fake or real. Google Search's route for fake imagery is one example [NC-24]. That can be hard to judge, and it is reasonable to say so.
- **If anyone shown may be under 18:**
  - do not download, make new copies of, or forward the image;
  - do not upload it anywhere, including to detection tools;
  - record non-image details instead: URLs, usernames, dates and report reference numbers;
  - follow the retention guidance of the specialist service or authority you choose to work with [NC-10, NC-22, NC-41].
- **For adults, guidance on keeping evidence varies between sources.**
  - Some evidence guidance focuses on recording URLs, usernames and dates, and involving a trusted person [NC-10].
  - If you keep evidence, store it securely and follow the guidance of the helpline, NGO or legal adviser you are working with.
  - Uploading intimate images to third-party detection tools is not needed for removal requests, and it creates copies with unclear retention. Avoiding it is the safer default (a recommendation, not a legal rule).
- **Hashing tools need an image already available on your device.** For images taken while anyone shown was under 18, do not download, copy or share an image to submit it. For adults, follow the service's evidence and eligibility guidance.
  - StopNCII is for adults. You must be the person shown, have been 18 or older in the image, and have access to the image [NC-21].
  - NCMEC Take It Down is for images taken when you were under 18 [NC-22].
- **Getting help is your choice.** Depending on your location, how urgent things are, and what you prefer, options include:
  - platform reporting tools;
  - specialist helplines and NGOs, for example eSafety in Australia or Netsafe in New Zealand [LG-36, LG-39];
  - legal advice;
  - the police.

  None of these happens automatically.
- **If authenticity becomes relevant,** for example in a prosecution, or when someone claims a real image is "AI" or a fake is "real", qualified forensic examiners and the institutions handling the matter are better placed than consumer tools (9.5).

---

## 12. What can and cannot be known

### 12.1 Supported with confidence by the sources reviewed

1. **No single method reviewed establishes, for arbitrary items under all conditions, whether a photo or video is AI-generated.** Performance figures apply to particular datasets and test dates.
   - On Deepfake-Eval-2024, open-source detectors scored AUC 0.50–0.63 for video and 0.52–0.56 for images. The best commercial tools stayed below 90% accuracy [DS-01, VE-01].
   - In several studies, detectors fell to roughly 44–68% on generators or content they were not trained on [DS-02, DS-03, DS-06, DS-09].
2. **Platform-style processing degraded several detectors substantially in the studies reviewed.** In one case, a detector caught every fake before Facebook upload and none after [DS-07, DS-09, DS-11].
3. **Human accuracy varied by study, media and task, from about 46% to 66%.** Several studies documented overconfidence [DS-16, DS-18, DS-19, DS-23].
4. **A valid, trusted Content Credential supports specific claims (who signed what, and integrity since signing), not the truth of a scene.** Where measured, credentials were rare: 0.43% of crawled images. In one 2025 test, none of eight platforms preserved them [PV-01, PV-02, PV-19, PV-25].
5. **Missing provenance or a missing watermark is not, by itself, evidence of authenticity or of fabrication.** Watermark checks find only the participating provider's marks [PV-01, PV-09, PV-66].
6. **The meaning of a detector flag depends on the base rate among the items checked.** Hypothetical worked examples show false alarms can outnumber correct flags when fakes are rare. No measured prevalence for social-media feeds was found [DS-24; section 5.5].
7. **In the largest fact-check dataset reviewed (to November 2023), real media in a false context was the dominant pattern.** Pixel-level detectors are not designed to address it [DS-26].
8. **The published vendor accuracy claims reviewed did not disclose the conditions needed to check them.**
   - In the largest independent benchmark, vendors were anonymized.
   - Named tests found tools strong on clean synthetic images but weaker on compressed files and on AI edits of real photos.
   - The one regulator finding on a detector claim found 98% advertised against 53% measured, for a text detector.
   
   [VE-01, VE-04, VE-05, VE-15 to VE-22, VE-27 to VE-31]
9. **In the NCII removal routes reviewed, a request does not require a detector verdict or proof of authenticity.**
   - These routes are the US statutory request process, the UK takedown duty, Australia's scheme and StopNCII.
   - Eligibility conditions differ. StopNCII, for example, requires the person to hold the image.
   - Some routes ask the requester to classify the image, such as Google's route for fake imagery.
   - Removal is not guaranteed.
   
   [LG-07, LG-19, LG-36, NC-19, NC-21, NC-24; read status in section 7.2]
10. **No statute, rule or decision found in the five jurisdictions gives C2PA credentials or watermarks an automatic presumption of authenticity** [LG-48].
11. **Detector outputs and forensic-looking visuals have been used to falsely "debunk" authentic media,** in 2023 and again in 2026 [VE-06, RC-10, RC-11, RC-12].
12. **For content that may depict a minor, the guidance reviewed consistently advises against downloading, copying, forwarding or uploading images.** It advises recording non-image details instead [NC-10, NC-22, NC-41].

### 12.2 Uncertain (thin, conflicting or secondary evidence)

1. How current commercial detectors perform on 2025–26 generators (Sora 2, Veo 3 and similar) after platform processing. No independent evaluation naming the tools was found [DS-01, DS-09].
2. What share of social-media content is AI-generated, or carries any provenance signal. Neither was measured in any source found [PV-25].
3. How robust production SynthID is against determined attackers. The provider self-reports, and an April 2026 removal claim is disputed and unverified [PV-10, PV-49].
4. Whether platforms now preserve or display credentials better than in October 2025. Labelling improved on some platforms in later audits [PV-18, PV-19].
5. Whether the experimental finding that "it's fake" claims fail against authentic video still holds as video generators improve [RC-09].
6. How large label effects are for images and video. The strongest evidence concerns text headlines [RC-07, RC-08].
7. Whether detector outputs have actually been used against people targeted by NCII. This is plausible but undocumented.
8. How consumer detector outputs would be treated in courts in the five jurisdictions. The only ruling found is Canadian and was read through secondary reports [LG-12, LG-16].
9. Several late-2026 legal details rest on secondary sources (section 7):
   - Ofcom's hash-matching status;
   - the X/Grok investigations;
   - New Zealand's bill stage;
   - several US judgments;
   - Australian statutory text.
10. Whether likelihood-ratio reporting for synthetic media can be validated under social-media conditions. Lab results did not transfer out of domain in the one study read [RC-04].
11. Who would pay for better authenticity evidence, and how much.
    - Funded demand appears mainly in enterprise fraud and identity detection.
    - The groups with the strongest social-media verification needs report fragile finances.
    - No market sizing or customer research was done [MK-18, MK-22, MK-23].
12. Whether vendors' terms of service permit independent benchmarking and publication of named results. Not reviewed.

### 12.3 What cannot be known from the evidence available for a typical item

1. **Authenticity from pixels alone.** "No evidence of manipulation" cannot establish that an item is authentic.
   - SWGDE: "by definition, it is impossible to prove a negative result". The most a thorough examination can say is that manipulation or digital creation is "unlikely", and a single generated frame may be "not detectable as virtual by a human" [RC-02].
   - WITNESS: proving the absence of manipulation is "inherently more difficult" than finding it [VE-02].
   - The formal results reviewed show trade-offs rather than impossibility. As generators approach the real-image distribution, single-item detection is expected to get harder [DS-13, DS-32].
2. **Origin, from missing provenance or a missing watermark alone** [PV-01, PV-09].
3. **Whether an event happened, or whether consent was given.** No authenticity signal addresses consent, and credentials do not attest to the truth of a scene [PV-01, PV-02].
4. **A detector's error rate on a generator it has never been tested against.** It stays unknown until someone measures it [VE-16, DS-05].
5. **A calibrated probability that a specific item is fake, without a defensible prior.** The answer depends on the base rate in the population the item came from and on how it came to attention, and that base rate is usually unknown.
6. **Who made a synthetic image, from the image alone.** Attribution typically needs institutional data such as device evidence, platform logs, or payment and account records [NC-50, NC-51].

---

## 13. Hypotheses for further work (no commercial wedge established)

This section offers judgments and one testable hypothesis, not a validated product recommendation. Other approaches were not assessed in depth, so it is not an exhaustive market analysis.

### 13.1 Approaches the reviewed evidence gives reasons to be cautious about

1. **A consumer "is this AI?" verdict tool.**
   - Free tools already exist (8.2).
   - Performance on content as it circulates is weak and condition-dependent in the evaluations reviewed (4.3, 5.2), and tools disagree with each other [RC-12].
   - Verdicts have been misused against authentic media (10).
   - Base rates complicate what flags mean (5.5).
   - Uploads raise privacy issues (8.3).
   - No evidence was found that consumers would pay.
   - These are reasons for caution, not proof that no viable consumer product exists.
2. **Detectors applied to intimate images, or offered to people targeted by NCII.**
   - The removal routes reviewed do not ask for a verdict (7.2, 9.3).
   - Verdicts can harm in both directions (9.4).
   - Handling intimate media conflicts with the guidance reviewed, especially for minors (9.4).
3. **Combining authenticity verdicts with survivor support.** See section 14.
4. **A stand-alone provenance reader as a differentiated product.**
   - Free tools from the standard's backers and from Google already exist (8.2).
   - Credentials were rare where measured, and platforms have stripped them [PV-25, PV-19].
   - Provenance infrastructure is being built by device makers, platforms and standards bodies under regulatory pressure (4.2).

### 13.2 One hypothesis worth testing: independent evaluation and claims disclosure

**The hypothesis:** there may be demand for an independent, standards-aligned service that evaluates authenticity tools and publishes disclosures about them. It would work as a test lab plus an open disclosure standard, not as a detector, and it would not give verdicts on individual items. **It is unvalidated. No customer interviews were conducted, and ability or willingness to pay is unknown.**

**What it would do, if pursued:**
- **Test sets.** It would maintain dated, provenance-documented test sets of photos and short videos as they circulate after platform processing (recompression, resizing, screenshots and overlays). The sets would include:
  - authentic photos, including lightly edited ones;
  - outputs of new generators.
  
  The sets would use only consented, licensed material. **No intimate imagery would be included.**
- **Reporting.** It would report attributable results in the way NIST AI 100-4 and forensic validation norms describe [RC-20, RC-18, RC-02]:
  - true-positive rates at very low false-positive rates;
  - false-positive rates at a fixed detection rate;
  - calibration;
  - results by subgroup and by post-processing condition;
  - the lag after a new generator launches.
- **Open standard.** It would publish the 15-item disclosure checklist from section 6 as an open standard.

**Evidence consistent with a gap:**
- None of the vendor claims reviewed disclosed the conditions needed to check them (section 6.7). Named tests show performance changing sharply with conditions [VE-27 to VE-29, VE-31].
- The largest independent in-the-wild evaluation anonymized vendors under contract [DS-01].
- No public results were found from NIST's image-discriminator evaluation, whose rules restrict public comparison [DS-30, DS-31, VE-23]. No published results were found for the AI FORCE challenges either [DS-27, DS-28].
- Validation gaps are recognised in forensic practice. The UK regulator names deepfake analysis but lifts ISO accreditation for it [RC-17], and PCAST calls claims without accuracy estimates "scientifically meaningless" [RC-18].
- The FTC's Workado order requires "competent and reliable evidence" for detector accuracy claims [VE-04].
- Tool choice matters:
  - false-positive rates on authentic photos ranged from 0% to 40% across five tools in one test [RC-12];
  - detector rankings barely held under simulated sharing (Spearman 0.07) [DS-09].
- Enterprise and government buyers have funded detection [MK-22, MK-23], and practitioners say they need interpretable, calibrated evidence [MK-04, MK-05].

**Possible buyers (untested):**
- platform trust-and-safety and procurement teams;
- public-sector buyers and regulators;
- newsrooms and fact-checkers, through funders;
- lawyers and expert witnesses;
- insurers;
- vendors seeking third-party validation. Vendor-paid certification would create a conflict of interest that needs structural safeguards.

**Reasons it could fail:**
- The groups with the strongest documented needs report fragile finances, and free public-interest detection has struggled [MK-18, MK-14].
- Vendor terms may restrict benchmarking or publication.
- Existing or planned evaluators could fill the gap, as partners or competitors: NIST, UL's DSRI, academic benchmarks, NewsGuard.
- Test sets age quickly, and fresh, ethically sourced ground truth is costly.
- Publishing named results may carry legal risk. Assessing that needs legal advice, which this report is not.
- Scorecards could be misread as authority for verdicts on individual items.

### 13.3 Proposed future validation questions (not started)

These are proposals. None has been started, and any work, including desk research, outreach, account creation or testing, would follow the owner's direction and approvals.

**Proposed desk questions**

| Question | Suggested decision criterion |
|---|---|
| D1. Do the published terms of service of the most-cited detection tools restrict benchmarking or publishing results? | If most restrict it, reshape the hypothesis toward commissioned private evaluations or vendor-consented testing. |
| D2. Do existing or planned evaluators (NIST GenAI, UL DSRI and AI FORCE, the Georgetown Deepfake-Eval program, academic benchmark teams, NewsGuard, WITNESS TRIED, biometric test labs) already publish attributable, refreshed, post-processing results for named tools? | If one does, partner with it or drop this hypothesis. |
| D3. Is there a lawful, consented route to a test set of at least 1,000 items containing no intimate content? | If there is none, this hypothesis is not feasible in this form. |

**Possible later tests** (only with explicit owner approval)

| Hypothesis | Method | Suggested pass | Suggested fail |
|---|---|---|---|
| H1. Demand | Structured interviews with target buyers and funders (for example, 20–25) | Several describe a current decision blocked by lack of independent evidence, and at least two commit to a paid or funded pilot | Fewer than two commitments |
| H2. Size of the gap | A pilot evaluation, compliant with terms, of at least 5 tools on at least 1,000 items, processed through real platform upload pipelines | Material gaps between claims and measured performance, or unstable rankings under processing | All tools close to their claims, with stable rankings |
| H3. Decision value | A randomised task study with practitioners, comparing vendor marketing with standards-aligned scorecards | Fewer over-reliance errors, or better tool choice | No measurable difference |
| H4. Freshness economics | Cost and time to add new generators and re-run tests | Within committed willingness to pay | Well above it |
| H5. Harm check | Consented review of scorecard design with fact-checkers and an NCII support organisation | Scorecards are not read as licence for item-level verdicts | Persistent misreading after redesign |

**How to read a failure.** Missing the suggested criteria would weaken this particular hypothesis. It would not show that no market exists, or that no other approach could work. Other approaches were not assessed here.

**What could change the assessment:**
- A regulator or major platform mandating independent detector testing would strengthen the case.
- NIST or UL publishing attributable results routinely would point toward partnership instead.
- Credentials becoming common, and preserved by platforms, would shift attention toward provenance infrastructure.

---

## 14. Provisional interface assessment: authenticity work and a separate survivor-support idea

**This is a provisional assessment based only on the evidence in this report.** It is not a comparison with any other report, and it does not research or assume the design of any survivor-support idea.

**Governing design principle: authenticity uncertainty should not gate support for a harmed person.** The evidence reviewed supports this principle:
- the removal routes reviewed do not ask for a verdict (7.2, 9.3);
- verdicts can harm in both directions (9.4);
- detector output has carried little evidentiary weight where examined (7.1);
- detector performance on content as it circulates is weak and condition-dependent in the evaluations reviewed (4.3, 5.5).

It is a recommended principle, not a legal rule.

### 14.1 Where the two ideas could legitimately touch

**1. Authenticity-neutral messaging**
- *What crosses:* plain-language, sourced statements that removal requests in the routes reviewed do not require proving whether an image is real or AI-generated. Each statement carries its jurisdiction-specific basis and read status, and notes that eligibility varies and removal is not guaranteed.
- *Conditions:* content only, with no data flows. Kept current as laws and policies change [LG-07, LG-17 to LG-19, LG-32, LG-36, LG-37].

**2. Optional referral for the rare cases where authenticity matters**
- *What crosses:* criteria for when expert involvement may help. Examples:
  - an offence turns on realism or fabrication;
  - a genuine image is being dismissed as "AI";
  - New Zealand's current recording-based offences may not clearly cover synthetic images (tentative);
  - disputes with a school or employer.
- *Conditions:* optional, and chosen by the person. Routes depend on location, urgency and preference: legal advice, NGOs, qualified forensic examiners, or police. Expert reports should follow evaluative-reporting norms (5.6) [NC-50, LG-14, LG-16, RC-01].

**3. Content-free evidence practice**
- *What crosses:* shared guidance that distinguishes minors from adults (9.4). For anyone who may be under 18: no downloading, copying, forwarding or uploading, and record URLs, usernames, dates and report IDs instead. For adults: follow the guidance of the service or adviser involved.
- *Conditions:* follows the eSafety, NCMEC and UK schools guidance [NC-10, NC-22, NC-41].

**4. Copy-finding knowledge**
- *What crosses:* how hash matching works, its limits (edited variants are missed; only images already on the device can be hashed), and which platforms accept StopNCII hashes.
- *Conditions:* on-device hashing through existing NGO tools only. For images taken while anyone shown was under 18, do not download or copy images to qualify. Adults should follow the service's evidence guidance [NC-21, NC-22, NC-25, NC-26].

**5. Policy evidence**
- *What crosses:* shared findings on intake designs that force a real-or-fake choice (for example Google Search's route for fake imagery), or that key on "photoshop" rather than consent.
- *Conditions:* advocacy inputs only [NC-24, NC-27, NC-31].

**6. Counter-messaging for discrediting**
- *What crosses:* wording that answers both "it's only fake" and "it's real, so you sent it" without relying on any verdict. For example: "Real or fabricated, sharing it without consent is abuse."
- *Conditions:* draws on 9.4 [NC-03, NC-04, NC-38].

### 14.2 Reasons not to combine them into one product or flow

1. **Implicit gating.** A detector placed inside a support flow signals that authenticity matters to getting help, and it invites triage by verdict. People already fear not being believed (9.4) [NC-04].
2. **Verdicts can harm in both directions.**
   - "Fake" can fuel minimisation.
   - "Likely real", including ordinary false negatives on new or unmarked generators, can fuel disbelief and sextortion leverage [NC-01, NC-03, NC-38, NC-04, NC-40; DS-01].
3. **Privacy and legal risk.** Detection needs the media, and the guidance reviewed cautions against copying or uploading intimate images, strongly so for minors [NC-10, NC-22, NC-41]. The NGO tools reviewed hash images on the device without uploading them [NC-21]. Not requiring intimate uploads is a recommended safety design, not a universal legal rule.
4. **Reliability.**
   - In the evaluations reviewed, open detectors performed near chance on content as it circulated.
   - On Deepfake-Eval-2024, the best commercial image tool missed 29% of fakes. The best video tool flagged about 21% of real videos and missed about 23% of fakes. These figures are derived from published precision and recall [DS-01, VE-01].
   - No source in this review evaluated detectors specifically on synthetic NCII. This report does not recommend collecting intimate imagery to build one.
5. **Limited evidentiary weight.** The one ruling found on a consumer printout (Canada; secondary reports) gave it no weight [LG-16]. Institution-produced evidence, such as investigative device forensics and platform confirmations, carries more weight in the sources reviewed (9.5).
6. **Dual use.** A public detector next to an abuse-support service could be used to test whether a fake "passes". Its "not AI" outputs could be screenshotted to shame a person, as detector outputs have been used against authentic war imagery [RC-11]. The oracle risk is an inference; evasion research shows that detectors can be steered with small changes [DS-12].
7. **Different duties and data regimes.**
   - Support for people harmed by abuse carries safeguarding, child-protection and special-category data obligations.
   - A verification tool for journalists or trust-and-safety teams carries different ones.
   - Combining them could mix legal obligations and incentives, depending on jurisdiction and the data handled. Improving detection may encourage data collection, while support should minimize retention. This is a design-risk assessment, not a settled legal conclusion.
8. **Measurement conflict.**
   - Support succeeds on removal speed, reduced re-exposure and the person's sense of control [NC-32, NC-33].
   - Detection succeeds on calibrated error rates.
   - A single product optimising both risks being judged, and tuned, on the wrong metric for one of its user groups.

**Provisional bottom line.** On this report's evidence, keep the two as separate efforts, with a one-way, content-free boundary. If authenticity information appears in a survivor context at all, it should be:
- optional;
- offered after removal and support routes;
- produced by an institution or a qualified expert;
- never a binary verdict;
- never dependent on uploading intimate media.

---

## 15. Limits of this research

- **Uneven reading depth and access.** Many sources were read in full, but others were read only in part, as abstracts, or through secondary accounts or search-result summaries. Some primary sources were paywalled, blocked or otherwise unavailable. Read status is recorded for every source in the ledger and flagged next to key claims. Findings that rest on secondary reads should be checked before anyone relies on them.
- **No hands-on testing, by design.** Every performance figure is second-hand: from papers, NGO casework, journalism or regulators. No detector was run, and no media was uploaded or tested.
- **Primary sources that were unavailable** include:
  - the original Washington Post test article;
  - parts of the Ofcom, eSafety and US congressional sites;
  - AFP and Internet Matters;
  - several court judgments (New York, British Columbia, Iowa);
  - Australian and New Zealand legislative texts;
  - some PDF reports.
- **Coverage bias.** Sources are mostly English-language, with law from the US, UK, EU, Australia and New Zealand. Evidence from the Global Majority comes mainly from WITNESS casework.
- **Fast decay.** Generator releases, platform policies and laws changed repeatedly during 2025–26, so figures can age within months.
- **Conflicts of interest in sources:**
  - vendor pages (marketing);
  - a benchmark built by a detection nonprofit, with vendors anonymized under contract;
  - a Google-funded prevalence study;
  - a provider-run watermark evaluation.
- **Internal inconsistencies.** Some key sources, notably Deepfake-Eval-2024's tables, contradict themselves. The ledger records these. This report uses the main-text or main-table figures and notes the variants.
- **No primary user research.** Evidence on needs comes from published surveys, NGO casework and studies. In particular, there is no direct evidence on what people targeted by NCII want from authenticity information. No customer or buyer interviews were conducted.
- **Not legal advice.** The legal statements describe sources as read on 18 November 2026, with their read status. Several rest on secondary reporting.

---

## 16. Unanswered questions

1. What share of social-media photos and videos is AI-generated, and what share carries any provenance signal?
2. How do named commercial detectors perform today on current generators (the Sora 2 and Veo 3 class) after real platform processing?
3. How robust are production watermarks, especially SynthID, against determined attackers, as measured independently?
4. Do platforms preserve or display Content Credentials in late 2026?
5. Has any court in the US, UK, EU, Australia or New Zealand weighed C2PA data or a consumer detector output?
6. Have detector outputs been used against people targeted by NCII, in schools, workplaces or courts?
7. What, if anything, do people targeted by NCII want from authenticity information, and in what form?
8. Who would pay for independent evaluation, and how much? Do vendors' terms permit it?
9. What is the status of the open legal items?
   - New Zealand's deepfake bill.
   - Australia's Digital Duty of Care Bill.
   - Ofcom's X/Grok investigation.
   - Whether Ofcom's hash-matching measures are in force.
   - Any US evidence-rule amendment.
   - Whether the TAKE IT DOWN removal duty reaches non-realistic fakes. That depends on 15 U.S.C. 6851, which was not read.
10. How large are label and warning effects for images and video, as opposed to text?
11. Can likelihood-ratio reporting for synthetic media be validated under social-media conditions?

---

## 17. Possible next steps (proposed; none started)

1. **Close evidence gaps.**
   - Re-read the primary sources that were unavailable: the Washington Post test, Ofcom's statement, eSafety guidance, the *M.S.*, *Head* and *Amyda* judgments, and the Australian and New Zealand legislation.
   - Look for NIST image-discriminator results and any AI FORCE outcomes.
   - Read 15 U.S.C. 6851.
2. **Consider the desk questions in 13.3 (D1–D3)** if the owner wants the evaluation hypothesis explored further.
3. **Treat outreach, account creation and any testing (13.3, H1–H5) as subject to explicit owner approval.**
4. **Keep the provisional survivor-support boundary in section 14** as a working assumption until the separate harm-response report is available for the requested comparison.

---

## Appendix: key sources

This table lists the sources cited most often in this report. The accompanying ledger has the full entry for every source ID, with URL, date, read status, claims, limitations and contradictions.

Read status means:
- **full text:** read in full;
- **most of the text:** read except a final portion;
- **partial:** read in part;
- **abstract only;**
- **secondary/snippet:** known only through a secondary account or search-result summary.

Long titles and dates are shortened.

| ID | Source | Type | Date | How read | URL |
|---|---|---|---|---|---|
| PV-01 | C2PA and Content Credentials Explainer, v2.3 | standards body | undated (©2026) | full text | https://spec.c2pa.org/specifications/specifications/2.3/explainer/Explainer.html |
| PV-02 | C2PA Technical Specification 2.3 | standards body | version history "2.3 - December 2025" (… | partial | https://spec.c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html |
| PV-04 | Content Credentials: Deployment Guidance, v1.0 | standards body | 2026-07-08 | partial | https://c2pa.org/wp-content/uploads/sites/33/2026/07/Content-Credentials-Deployment-Guidance.pdf |
| PV-09 | Verify AI-generated images, videos, and audio (Gemini Apps Help) | platform documentation | undated (live page) | full text | https://support.google.com/gemini/answer/16722517?hl=en |
| PV-10 | SynthID-Image: Image watermarking at internet scale | preprint | 2025-10-10 | partial | https://arxiv.org/html/2510.09263v1 |
| PV-11 | Invisible Image Watermarks Are Provably Removable Using Generative AI | peer-reviewed (NeurIPS 2024) | v1 2023-06-02; v3 2024-10-31 | full text | https://arxiv.org/abs/2306.01953 |
| PV-13 | WAVES: Benchmarking the Robustness of Image Watermarks | peer-reviewed (ICML 2024) | v1 2024-01-16; v3 2024-06-07 | partial | https://arxiv.org/abs/2401.08573 |
| PV-14 | UnMarker: A Universal Attack on Defensive Image Watermarking | peer-reviewed (IEEE S&P 2025) | v1 2024-05-14; v2 2024-11-22 | abstract only | https://arxiv.org/abs/2405.08363 |
| PV-17 | Tech platforms fail to label AI content (C2PA metadata audit) | journalism / independent evaluation | 2025-10-23 | partial (paywalled) | https://indicator.media/p/tech-platforms-fail-to-label-ai-content-c2pa-metadata |
| PV-18 | AI labeling is still very much a work in progress | journalism / independent evaluation | 2026-03-18 | partial (paywalled) | https://indicator.media/p/ai-labeling-is-still-very-much-a-work-in-progress |
| PV-19 | "We uploaded a fake video to 8 social apps. Only one told users it wasn't real." | journalism / independent evaluation | 2025-10-22 | secondary/snippet | https://www.washingtonpost.com/technology/2025/10/22/ai-deepfake-sora-platforms-c2pa/ |
| PV-20 | Nikon struggles with security problems in photo authentication | journalism | 2025-09-23 | full text | https://heise.de/-10667707 |
| PV-25 | Metawatch: C2PA content credentials | NGO / standards body measurement (indep… | live page; crawl series about 2026-06-0… | full text | https://metawatch.iptc.org/c2pa/ |
| PV-30 | Strong backing for the Code of Practice on transparency of AI-generated content | government or regulator | 2026-07-31 (last updated 2026-11-17) | full text | https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content |
| PV-64 | MeitY notifies the IT Amendment Rules 2026 | other (law-firm analysis) | 2026-02-16 | full text | https://www.khaitanco.com/thought-leadership/MeitY-notifies-the-IT-Amendment-Rules-2026 |
| PV-65 | Measures for Labeling of AI-Generated Synthetic Content (AGORA entry reproducing China La… | legislation (unofficial translation, re… | enacted 2025-03-07; effective 2025-09-01 | full text | https://agora.eto.tech/instrument/2096 |
| PV-66 | Building trust on YouTube: 'Captured with a camera' disclosure | platform documentation | undated (©2026) | full text | https://support.google.com/youtube/answer/15446725?hl=en |
| DS-01 | Deepfake-Eval-2024: A Multi-Modal In-the-Wild Benchmark of Deepfakes Circulated in 2024 | preprint | benchmark release 4 Mar 2025; version r… | most of the text | https://arxiv.org/html/2503.02857 |
| DS-02 | A Sanity Check for AI-generated Image Detection (Chameleon dataset; AIDE) | preprint (reported as ICLR 2025; venue … | v1 June 2024; v3 15 Feb 2025 | full text | https://arxiv.org/html/2406.19435 |
| DS-03 | GenImage: A Million-Scale Benchmark for Detecting AI-Generated Image | peer-reviewed (NeurIPS 2023 Datasets & … | arXiv June 2023; NeurIPS Dec 2023 | full text | https://ar5iv.labs.arxiv.org/html/2306.08571 |
| DS-05 | Community Forensics: Using Thousands of Generators to Train Fake Image Detectors | preprint (reported as CVPR 2025; not co… | v1 Nov 2024; v2 9 Jun 2025 | full text | https://arxiv.org/html/2411.04125 |
| DS-07 | TrueFake: A Real World Case Dataset of Last Generation Fake Images also Shared on Social … | preprint (repo labelled IJCNN25; unconf… | 29 Apr 2025 | full text | https://arxiv.org/html/2504.20658 |
| DS-09 | Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systemati… | preprint | v1 14 Aug 2026; v2 17 Aug 2026 | full text | https://arxiv.org/html/2608.14391 |
| DS-11 | FaceForensics++: Learning to Detect Manipulated Facial Images | peer-reviewed (ICCV 2019) | arXiv Jan 2019; ICCV Oct 2019 | full text | https://ar5iv.labs.arxiv.org/html/1901.08971 |
| DS-12 | Evading Deepfake-Image Detectors with White- and Black-Box Attacks | peer-reviewed (CVPR Workshops 2020) | arXiv Apr 2020 | full text | https://ar5iv.labs.arxiv.org/html/2004.00622 |
| DS-13 | Robustness of AI-Image Detectors: Fundamental Limits and Practical Attacks | peer-reviewed (ICLR 2024) | arXiv 30 Sep 2023; ICLR May 2024 | most of the text | https://arxiv.org/html/2310.00076 |
| DS-16 | AI-synthesized faces are indistinguishable from real faces and more trustworthy | peer-reviewed (PNAS) | published 14 Feb 2022 | full text | https://pmc.ncbi.nlm.nih.gov/articles/PMC8872790 |
| DS-17 | Deepfake detection by human crowds, machines, and machine-informed crowds | peer-reviewed (PNAS 2022, vol. 119 no. … | arXiv May 2021; PNAS Jan 2022 | full text | https://ar5iv.labs.arxiv.org/html/2105.06496 |
| DS-18 | Fooled twice: People cannot detect deepfakes but think they can | peer-reviewed (iScience 24(11)) | published 19 Nov 2021 | full text | https://pmc.ncbi.nlm.nih.gov/articles/PMC8602050 |
| DS-24 | The Deepfake Detection Challenge (DFDC) Preview Dataset | preprint | Oct 2019 | full text | https://ar5iv.labs.arxiv.org/html/1910.08854 |
| DS-26 | AMMeBa: A Large-Scale Survey and Dataset of Media-Based Misinformation In-The-Wild | preprint | May 2024 (data through 18 Nov 2023) | most of the text | https://arxiv.org/html/2405.11697 |
| VE-02 | "TRIED: Truly Innovative and Effective AI Detection Benchmark, developed by WITNESS" | NGO report (preprint). | v2 1 May 2025 (v1 30 Apr 2025). | full text | https://arxiv.org/html/2504.21489v2 |
| VE-03 | "Five Real-World Failures Expose Need for Effective Detection of AI-Generated Media" | NGO perspective in a journalism outlet. | June 26, 2025. | full text | https://techpolicy.press/five-real-world-failures-expose-need-for-effective-detection-of-ai-generated-media |
| VE-04 | "FTC Order Requires Workado to Back Up Artificial Intelligence Detection Claims" | government / regulator. | April 28, 2025. | full text | https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-order-requires-workado-back-artificial-intelligence-detection-claims |
| VE-05 | "FTC Approves Final Order against Workado, LLC, Which Misrepresented the Accuracy of its … | government / regulator. | August 28, 2025. | full text | https://www.ftc.gov/node/297697 |
| VE-06 | "AI Images Detectors Are Being Used to Discredit the Real Horrors of War" | journalism. | Oct 13, 2023. | full text (paywalled) | https://www.404media.co/ai-images-detectors-are-being-used-to-discredit-the-real-horrors-of-war/ |
| VE-15 | AI or Not homepage | vendor marketing. | undated. | full text | https://www.aiornot.com/ |
| VE-16 | Sightengine, "Detect AI-generated images" | vendor marketing. | undated. | full text | https://sightengine.com/detect-ai-generated-images |
| VE-27 | "Testing AI or Not: How Well Does an AI Image Detector Do Its Job?" | journalism / independent test. | Sept 11, 2023. | full text | https://www.bellingcat.com/resources/how-tos/2023/09/11/testing-ai-or-not-how-well-does-an-ai-image-detector-do-its-job/ |
| VE-28 | "Organic or Diffused: Can We Distinguish Human Art from AI-generated Images?" | peer-reviewed (ACM CCS 2024). | v1 Feb 5, 2024; v3 Jul 2, 2024; CCS Oct… | full text | https://arxiv.org/abs/2402.03214 |
| VE-29 | "The Adversarial AI-Art: Understanding, Generation, Detection, and Benchmarking" (ARIA) | preprint. | Apr 22, 2024 (v1). | full text | https://arxiv.org/abs/2404.14581 |
| VE-30 | "Our Approach to Labeling AI-Generated Content and Manipulated Media" | platform documentation. | Apr 5, 2024; updated May 10, Jul 1 and … | full text | https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/ |
| VE-31 | "Leading AI Image Detection Tools Mislead Online Users, Often Declaring Authentic Content… | journalism / independent evaluation. | May 8, 2026. | full text | https://www.newsguardtech.com/?p=33448 |
| VE-32 | "AI's blind spot: Tools fail to detect their own fakes" | journalism. | Nov 21, 2025. | full text | https://www.rnz.co.nz/news/business/579586/ai-s-blind-spot-tools-fail-to-detect-their-own-fakes |
| LG-01 | Machine-Generated Evidence: Rules Advisory Committee Hits Pause to Consider Significant R… | other (law-firm practitioner commentary) | July 2026 | full text | https://www.redgravellp.com/publication/machine-generated-evidence--rules-advisory-committee-hits-pause-to-consider-significant-revisions-to-proposed-federal-rule-of-evidence-707-addressing-evidence-generated-by-artificial-intelligence |
| LG-07 | Public Law 119-12 (TAKE IT DOWN Act) | legislation | enacted 19 May 2025 | full text | https://www.govinfo.gov/content/pkg/PLAW-119publ12/html/PLAW-119publ12.htm |
| LG-10 | Court Throws Out Case After Finding Plaintiffs Submitted Deepfake Videos and Altered Imag… | legal scholarship (blog) quoting a cour… | 25 Sep 2025 | partial | https://reason.com/volokh/2025/09/25/court-throws-out-case-after-finding-plaintiffs-submitted-deepfake-videos-and-altered-images/ |
| LG-11 | Claiming Video Was "Deepfake" Not Enough to Require Excluding It, Even Absent Evidence of… | legal scholarship (blog) quoting a cour… | 13 Oct 2026 | full text | https://reason.com/volokh/2026/10/13/claiming-video-was-deepfake-not-enough-to-require-excluding-it-even-absent-evidence-of-who-recorded-it/ |
| LG-13 | Matter of M.S. (M.H.), 2026 NY Slip Op 00825 | court record (secondary) | 17 Feb 2026 | secondary/snippet | https://nycourts.gov/reporter/3dseries/2026/2026_00825.htm |
| LG-14 | State v. Puloka, No. 21-1-04851-2 (Wash. Super. Ct. King County), Findings of Fact and Co… | court record (secondary) | 29 Mar 2024 (ruling); April–May 2024 (r… | secondary/snippet | https://gtlaw.com/en/insights/2024/5/washington-court-rejects-novel-use-of-ai-enhanced-video-in-trial |
| LG-16 | Head v John Doe, 2026 BCSC 184 (Canada), as reported | court record (secondary) / practitioner… | judgment 4 Feb 2026; IBA April 2026 | secondary/snippet | https://www.ibanet.org/authenticating-evidence-in-the-age-of-AI |
| LG-17 | Sexual Offences Act 2003, section 66E (Creating purported intimate image of adult) | legislation | in force 6 Feb 2026; page current to 18… | full text | https://www.legislation.gov.uk/ukpga/2003/42/section/66E |
| LG-18 | Sexual Offences Act 2003, sections 66A, 66B, 66D | legislation | in force 31 Jan 2024 | full text | https://www.legislation.gov.uk/ukpga/2003/42/section/66B |
| LG-19 | Crime and Policing Act 2026, Part 5, Chapter 4 | legislation | Royal Assent 29 Apr 2026 (see LG-55) | partial | https://www.legislation.gov.uk/ukpga/2026/20/part/5/chapter/4 |
| LG-27 | Directive (EU) 2024/1385 on combating violence against women and domestic violence (Art. … | legislation (secondary read) plus legal… | adopted 14 May 2024; OJ 24 May 2024; in… | full text | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202401385 |
| LG-28 | Regulation (EU) 2024/1689 (AI Act), Art. 50 and Art. 3(60) | legislation (secondary read); other (la… | Act 2024; Art. 50 applies from 2 Aug 20… | full text | https://artificialintelligenceact.eu/transparency-rules-article-50/ |
| LG-32 | Criminal Code Amendment (Deepfake Sexual Material) Act 2024 (No. 78, 2024), Sch. 1; Bills… | legislation (secondary read); government | assent 2 Sep 2024; commenced 3 Sep 2024 | secondary/snippet | https://classic.austlii.edu.au/au/legis/cth/num_act/ccasma2024387/sch1.html |
| LG-33 | Court orders $343,500 penalty for posting deepfakes of Australian women | government or regulator | 26 Sep 2025 | secondary/snippet | https://www.esafety.gov.au/newsroom/media-releases/court-orders-343500-penalty-for-posting-deepfakes-of-australian-women |
| LG-37 | Deepfake bill passes first reading in Parliament; ACT release; ACT MP says deepfake bill … | journalism; government/political | 20 May 2026; 22 Jul 2026 | secondary/snippet | https://www.rnz.co.nz/news/politics/595813/deepfake-bill-passes-first-reading-in-parliament |
| LG-39 | Understanding Deep Fakes; The Harmful Digital Communications Act | NGO (approved agency under statute) | undated | secondary/snippet | https://netsafe.org.nz/online-abuse-and-harassment/understanding-deep-fakes |
| LG-43 | Deepfakes in Court: How Judges Can Proactively Manage Alleged AI-Generated Material in Na… | legal scholarship | 2024 (SSRN); published 2025 | abstract only | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4943841 |
| LG-56 | Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 am… | legislation | 8 Jul 2026; OJ L 24 Jul 2026; in force … | full text | https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng |
| MK-01 | "How Americans View AI and Its Impact on People and Society" |  | 2025-09-17. | full text | https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/ |
| MK-02 | Digital News Report 2026, Executive Summary |  | 2026-06-16. | partial | https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary |
| MK-04 | "TRIED: Truly Innovative and Effective AI Detection Benchmark" |  | v2 2025-05-01. | partial | https://arxiv.org/html/2504.21489v2 |
| MK-07 | Privacy Policy, Is It AI? |  | "Last updated: October 2026". | full text | https://isitai.com/privacy |
| MK-18 | "State of the Fact-Checkers: Audiences grow as finances worsen" |  | 2026-04-06. | secondary/snippet | https://www.poynter.org/ifcn/2026/state-fact-checkers-2025/ |
| MK-22 | "Reality Defender Banks $33M to Tackle AI-Generated Deepfakes" |  | 2024-10-23. | secondary/snippet | https://www.securityweek.com/reality-defender-banks-33m-to-tackle-ai-generated-deepfakes/ |
| MK-23 | "Has GetReal cracked the code on AI deepfakes? $18M and an impressive client list says ye… |  | 2025-03-26. | secondary/snippet | https://techcrunch.com/2025/03/26/has-getreal-cracked-the-code-on-ai-deepfakes-18m-and-an-impressive-client-list-says-yes |
| MK-45 | Gemini Apps Privacy Hub |  | updated 2026-11-16/17. | full text | https://support.google.com/gemini/answer/13594961?hl=en |
| MK-46 | Privacy Policy, Sightengine |  | "Last updated: November 6, 2026". | full text | https://sightengine.com/policies/privacy |
| MK-52 | "SIFT (The Four Moves)" |  | 2019-06-19. | partial | https://hapgood.us/2019/06/19/sift-the-four-moves/ |
| MK-54 | Verification Handbook 3, ch. 6, "How to think about deepfakes and emerging manipulation t… |  | undated (c. early 2020). | full text | https://datajournalism.com/read/handbook/verification-3/investigating-actors-content/6-how-to-think-about-deepfakes-and-emerging-manipulation-technologie |
| NC-01 | Non-Consensual Synthetic Intimate Imagery: Prevalence, Attitudes, and Knowledge in 10 Cou… | peer-reviewed | arXiv 26 Jan / 13 Feb 2024; CHI May 2024 | full text | https://arxiv.org/html/2402.01721v2 |
| NC-02 | "That Experience Still Haunts Me to This Day": A Multi-Region Survey on AI-Generated Imag… | peer-reviewed | 2026 (RMIT release 4 Nov 2026; one sour… | abstract only | https://www.rmit.edu.au/news/all-news/2026/nov/image-based-abuse |
| NC-03 | Deepfake Nudes & Young People (report); blog "Deepfake nudes are a harmful reality for yo… | NGO | 3 Mar 2025 | full text | https://www.thorn.org/blog/deepfake-nudes-are-a-harmful-reality-for-youth-new-research-from-thorn/ |
| NC-04 | Will I be believed? How deepfakes are adding fears to youth experiencing sextortion | NGO | 26 Sept 2024 | full text | https://www.thorn.org/blog/will-i-be-believed-how-deepfakes-are-adding-fears-to-youth-experiencing-sextortion/ |
| NC-05 | In Deep Trouble: Surfacing Tech-Powered Sexual Harassment in K-12 Schools (report page an… | NGO | 26 Sept 2024 | full text | https://cdt.org/insights/report-in-deep-trouble-surfacing-tech-powered-sexual-harassment-in-k-12-schools/ |
| NC-07 | Common Sense Media Releases New Research on Teens and AI-Generated Explicit Material | NGO | 21 Jul 2026 | full text | https://about.commonsensemedia.org/press-room/press-releases/common-sense-media-releases-new-research-on-teens-and-ai-generated-explicit-material |
| NC-10 | eSafety image-based abuse FAQ; IBA Scheme Regulatory Guidance (Feb 2024); How to collect … | government or regulator | Feb 2024 and others undated | secondary/snippet | https://www.esafety.gov.au/key-topics/image-based-abuse/faq-about-image-based-abuse |
| NC-19 | TAKE IT DOWN Act (S.146, enrolled) | legislation | signed 19 May 2025 | full text | https://www.govinfo.gov/content/pkg/BILLS-119s146enr/html/BILLS-119s146enr.htm |
| NC-21 | StopNCII.org FAQ | NGO | undated (©2026) | full text | https://stopncii.org/faq/ |
| NC-22 | Take It Down FAQ | NGO | undated (©2026) | full text | https://takeitdown.ncmec.org/faq/ |
| NC-24 | Remove involuntary fake pornography / sexual content from Google (Search Help) | platform documentation | undated | full text | https://support.google.com/websearch/answer/9116649?hl=en |
| NC-27 | Explicit AI Images of Female Public Figures (Oversight Board release); Meta transparency … | platform documentation (quasi-judicial) | 25 Jul 2024; Meta page updated 26 Sept … | full text | https://www.oversightboard.com/news/new-decision-addresses-metas-rules-on-non-consensual-deepfake-intimate-images/ |
| NC-31 | Reporting Non-Consensual Intimate Media: An Audit Study of Deepfakes | preprint | 18 Sept 2024 | full text | https://arxiv.org/html/2409.12138v1 |
| NC-38 | Examining public attitudes to deepfakes (Crest Advisory); Police warn of rising threat fr… | government or regulator | 24 Nov 2025 (Crest updated 12 Dec 2025) | full text | https://www.crestadvisory.com/post/examining-public-attitudes-to-deepfakes |
| NC-41 | Sharing nudes and semi-nudes: advice for education settings working with children and you… | government or regulator | updated 11 Mar 2024 (disclaimer says Fe… | full text | https://www.gov.uk/government/publications/sharing-nudes-and-semi-nudes-advice-for-education-settings-working-with-children-and-young-people/sharing-nudes-and-semi-nudes-advice-for-education-settings-working-with-children-and-young-people |
| NC-45 | How we practice trauma-informed design at Chayn; Chayn Principles | NGO | 1 Feb 2024 | secondary/snippet | https://chayn.notion.site/How-we-practice-trauma-informed-design-at-Chayn-1-Feb-2024-6f5211828e4a4a1db9735fe371febb79 |
| NC-50 | AAP report on an Australian AI-sextortion prosecution (defendant not named here) | journalism | 2026 (date not captured) | secondary/snippet | https://aapnews.aap.com.au/news/first-look-at-creep-who-scraped-photos-to-sextort-women |
| RC-01 | ENFSI Guideline for Evaluative Reporting in Forensic Science (approved version 3.0; STEOF… | standards body | 2015 (exact approval date not seen in t… | full text | https://enfsi.eu/wp-content/uploads/2016/09/m1_guideline.pdf |
| RC-02 | Best Practices for Image Authentication, 18-I-001-2.0 | standards body | Version 2.0, 3/3/2025. Final Approved D… | full text | https://www.swgde.org/wp-content/uploads/2025/03/2025-03-03-Best-Practices-for-Image-Authentication-18-I-001-2.0.pdf |
| RC-04 | A score based likelihood ratio framework for deepfake image identification in forensic sc… | peer-reviewed | published 2026-03-05 (received 2025-11-… | full text | https://pmc.ncbi.nlm.nih.gov/articles/PMC13077008/ |
| RC-07 | Altay & Gilardi (title as recalled: "People are skeptical of headlines labeled as AI-gene… | peer-reviewed | 2024-10-01 | full text | https://pmc.ncbi.nlm.nih.gov/articles/PMC11443540 |
| RC-08 | Labeling AI-generated media online | peer-reviewed | advance access 2025-05-28 (received 202… | abstract only | https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/9/583/files/2026/01/labelingaigenerated_2025.pdf |
| RC-09 | The Liar's Dividend: Can Politicians Claim Misinformation to Evade Accountability? | peer-reviewed | online 2024-02-20; issue February 2025 | full text | https://www.cambridge.org/core/product/687FEE54DBD7ED0C96D72B26606AA073/core-reader |
| RC-11 | How AI Content Detection is Being Weaponized in the Iran War | NGO / journalism | 2026-03-17 | full text | https://techpolicy.press/how-ai-content-detection-is-being-weaponized-in-the-iran-war |
| RC-12 | Leading AI Image Detection Tools Mislead Online Users, Often Declaring Authentic Content … | journalism (structured tool test) | 2026-05-08 | full text | https://www.newsguardtech.com/?p=33448 |
| RC-17 | Forensic science activities: statutory code of practice – version 2 | government or regulator | published 2025-06-05; in force 2025-10-… | partial | https://www.gov.uk/government/publications/forensic-science-activities-statutory-code-of-practice-version-2 |
| RC-18 | Forensic Science in Criminal Courts: Ensuring Scientific Validity of Feature-Comparison M… | government report | September 2016 | partial | https://obamawhitehouse.archives.gov/sites/default/files/microsites/ostp/PCAST/pcast_forensic_science_report_final.pdf |
| RC-20 | NIST AI 100-4, Reducing Risks Posed by Synthetic Content | government report | November 2024 | partial | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-4.pdf |
| RC-21 | Deepfake detection by human crowds, machines, and machine-informed crowds | peer-reviewed | online 2021-12-28; issue 2022-01-04 | most of the text | https://pmc.ncbi.nlm.nih.gov/articles/PMC8740705/ |
| RC-23 | Negative Consequences of Informing Voters about Deepfakes: Evidence from Two Survey Exper… | peer-reviewed | 2022-02-28 | abstract only | https://tsjournal.org/index.php/jots/article/view/28 |
| RC-24 | Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security | peer-reviewed (law review) | December 2019 | partial | https://www.californialawreview.org/print/deep-fakes-a-looming-challenge-for-privacy-democracy-and-national-security |
| RC-26 | C2PA User Experience Guidance for Implementers, v2.2 | standards body (guidance) | undated (footer © 2026) | full text | https://spec.c2pa.org/specifications/specifications/2.2/ux/UX_Recommendations.html |
