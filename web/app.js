/* Evidelle C2PA evidence check — runs entirely in this browser.
 *
 * Verification is done by the pinned @contentauth/c2pa-web WebAssembly build, vendored
 * under vendor/. Trust anchors are the official C2PA conformance lists pinned in
 * trust-anchors.js. Nothing is uploaded: the page declares connect-src 'none'.
 *
 * The labels and the "can and cannot conclude" readings are the same fixed rules the
 * repository uses for its local checker, applied to the verifier's own status codes.
 */
import { TRUST, TRUST_TEXTS, TEST_CERT_MARKERS } from './trust-anchors.js';

const ENGINE = {
  name: '@contentauth/c2pa-web',
  version: '0.17.1',
  license: 'MIT',
  npmIntegrity: 'sha512-3JBoLhmffbUX1aQk9iolKsff+J6xOWgHvNshLvWQAbeJKDtL6OjRlOD9O9rJajYYUrguSOfJCiRSfchZ5IdS3Q==',
  wasmEmbedded: true,
};
const MAX_BYTES = 25 * 1024 * 1024;
const MAGIC = [
  ['image/jpeg', [0xff, 0xd8, 0xff]],
  ['image/png', [0x89, 0x50, 0x4e, 0x47]],
  ['image/webp', [0x52, 0x49, 0x46, 0x46]],
];
const SOURCE_TYPE_WORDS = {
  algorithmicMedia: 'created by an algorithm',
  trainedAlgorithmicMedia: 'created by a trained model',
  digitalCapture: 'captured by a camera',
};

let enginePromise = null;
const engineStatus = document.getElementById('engine-status');
const filesEl = document.getElementById('files');
const listEl = document.getElementById('case-list');
const caseEl = document.getElementById('case');
const cases = [];
const byId = {};
let current = null;

function status(text) { engineStatus.textContent = text; }

async function ensureEngine() {
  enginePromise ??= (async () => {
    status('Loading the pinned verifier (about 12 MB, once per visit, from this site’s own files)…');
    const mod = await import('./vendor/c2pa-web/inline.js');
    const c2pa = await mod.createC2pa();
    /* Policy "official": the C2PA conformance trust list + its TSA list.
       Policy "interim": the frozen CAI interim list (what verify.contentauthenticity.org
       uses) + its EKU store, with the interim list itself as the TSA anchors — matching
       c2patool's legacy mode, where the signing anchor set doubles as timestamp-authority
       anchors (why c2patool reports timeStamp.trusted for e.g. the Truepic sample with no
       configured anchors). Two passes keep the lists distinguished, as the interim list's
       own header asks. */
    const base = mod.createVerifySettings({ remoteManifestFetch: false, ocspFetch: false });
    const ctxOfficial = new mod.Context(mod.mergeSettings(
      mod.createTrustSettings({ trustAnchors: TRUST.MANIFEST_TRUST_LIST.pem }),
      mod.createTsaTrustSettings({ trustAnchors: TRUST.TSA_TRUST_LIST.pem }),
      base,
    ));
    const ctxInterim = new mod.Context(mod.mergeSettings(
      mod.createTrustSettings({
        trustAnchors: TRUST.INTERIM_TRUST_LIST.pem,
        trustConfig: TRUST_TEXTS.INTERIM_EKU_STORE,
      }),
      mod.createTsaTrustSettings({ trustAnchors: TRUST.INTERIM_TRUST_LIST.pem }),
      base,
    ));
    status('Verifier ready. Files are checked on this device; nothing is uploaded.');
    return { mod, c2pa, ctxOfficial, ctxInterim };
  })().catch((err) => { enginePromise = null; status('Could not load the verifier: ' + err); throw err; });
  return enginePromise;
}

/* ---------- experimental AI-image detector ----------
 * OwensLab/commfor-model-384 (Community Forensics, MIT), exported by this repo to
 * fp16 ONNX (detector_eval/export_onnx.py — fp32 export verified logit-identical to
 * the PyTorch original; fp16 showed zero sign flips on 120 eval images). Runs via the
 * pinned onnxruntime-web WASM build, fetched from this site only on demand.
 * It produces a probability score — never a verdict. Calibrated on the numbers in
 * RESULTS_DETECTOR.md. */
const DETECTOR = {
  engine: 'onnxruntime-web', engineVersion: '1.31.1',
  npmIntegrity: 'sha512-5GeH+bWQ+HxM10z7erGlsWqryrwMbSvm/1tkIsKTT48g0fI19VXVVC435t4t7VsPdSQeS7NmuZPXrQ73k82URw==',
  modelFile: './detector-model.fp16.onnx',
  modelSha256: '78cc1dc6c49a3a5d68fbc8d160e2799ec21837d12662d5b3f9d978c7bb44c52f',
  modelSource: 'OwensLab/commfor-model-384 (MIT), exported to fp16 ONNX by detector_eval/export_onnx.py',
  downloadBytes: 59 * 1024 * 1024,
};
let detectorPromise = null;

async function ensureDetector(onProgress) {
  detectorPromise ??= (async () => {
    const ort = await import('./vendor/onnxruntime-web/ort.wasm.min.mjs');
    /* wasmPaths defaults to the module's own directory — the glue and .wasm ship together. */
    ort.env.wasm.numThreads = 1;
    const res = await fetch(DETECTOR.modelFile);
    if (!res.ok) { throw new Error('model fetch failed (' + res.status + ')'); }
    const total = DETECTOR.downloadBytes;
    const chunks = [];
    let got = 0;
    const rd = res.body.getReader();
    for (;;) {
      const r = await rd.read();
      if (r.done) { break; }
      chunks.push(r.value); got += r.value.length;
      if (onProgress) { onProgress(got, total); }
    }
    const buf = new Uint8Array(got);
    let off = 0;
    chunks.forEach((c) => { buf.set(c, off); off += c.length; });
    const session = await ort.InferenceSession.create(buf.buffer, { executionProviders: ['wasm'] });
    return { ort, session };
  })().catch((err) => { detectorPromise = null; throw err; });
  return detectorPromise;
}

/* Same recipe as the authors' demo: resize shorter edge to 440, center-crop 384,
 * ImageNet normalization. Canvas downsampling differs slightly from the eval's
 * bicubic path — verified harmless on known eval samples. */
const DET_MEAN = [0.485, 0.456, 0.406];
const DET_STD = [0.229, 0.224, 0.225];
async function detectorPixels(file) {
  const bmp = await createImageBitmap(file);
  const s = 440 / Math.min(bmp.width, bmp.height);
  const w = Math.max(384, Math.round(bmp.width * s));
  const h = Math.max(384, Math.round(bmp.height * s));
  const a = document.createElement('canvas');
  a.width = w; a.height = h;
  const ca = a.getContext('2d', { willReadFrequently: true });
  ca.imageSmoothingQuality = 'high';
  ca.drawImage(bmp, 0, 0, w, h);
  bmp.close();
  const sx = Math.floor((w - 384) / 2);
  const sy = Math.floor((h - 384) / 2);
  const px = ca.getImageData(sx, sy, 384, 384).data;
  const out = new Float32Array(3 * 384 * 384);
  for (let i = 0; i < 384 * 384; i++) {
    for (let ch = 0; ch < 3; ch++) {
      out[ch * 384 * 384 + i] = (px[i * 4 + ch] / 255 - DET_MEAN[ch]) / DET_STD[ch];
    }
  }
  return out;
}

/* Fixed wording for the score zones — calibrated on RESULTS_DETECTOR.md numbers:
 * balanced accuracy 0.91 at full size, specificity 0.965, but only 66% on the newest
 * generator tested and 38% of fakes caught after a JPEG q50 re-save. */
function detectorZone(p) {
  if (p >= 0.9) {
    return { cls: 'broken', text: 'Scores like the AI-generated images this model was tested on' };
  }
  if (p >= 0.5) {
    return { cls: 'unknown', text: 'Leans toward the AI-generated side of the model’s scale, in its least certain zone' };
  }
  if (p > 0.1) {
    return { cls: 'unknown', text: 'Leans toward the real-photo side of the model’s scale, in its least certain zone' };
  }
  return { cls: 'intact', text: 'Scores like the real photos this model was tested on' };
}

function detectorSection(c) {
  const sec = el('section', { 'aria-labelledby': 'sec-detector' },
    el('h3', { class: 'section-title', id: 'sec-detector', text: '4. Experimental: AI-image check' }));
  const card = el('div', { class: 'card' },
    el('div', { class: 'chips' }, chip('unknown', 'EXPERIMENTAL — a probability score, not a verdict')),
    el('p', { text: 'A pinned AI-image detector runs on this picture, on this device. In offline tests it caught most '
      + 'AI-generated images at full size, missed about 1 in 3 of the newest generator’s, caught only ~2 in 5 after a '
      + 'JPEG re-save, and wrongly flagged ~1 in 28 real photos. A low score is not proof an image is real.' }));
  const body = el('div');
  const run = el('button', {
    class: 'btn', type: 'button',
    text: 'Run the experimental check (~60 MB one-time download from this site)',
    onclick: async () => {
      run.disabled = true;
      body.textContent = '';
      const note = el('p', { class: 'note' });
      body.appendChild(note);
      try {
        const { ort, session } = await ensureDetector((got, total) => {
          note.textContent = 'Downloading the detector model — ' + (got / 1048576).toFixed(0)
            + ' of ~' + Math.round(total / 1048576) + ' MB (once, then cached by this browser)…';
        });
        note.textContent = 'Scoring on this device…';
        const px = await detectorPixels(c.file);
        const input = new ort.Tensor('float32', px, [1, 3, 384, 384]);
        const outMap = await session.run({ pixel_values: input });
        const logit = outMap.logits.data[0];
        const p = 1 / (1 + Math.exp(-logit));
        const zone = detectorZone(p);
        c.detector = { logit, p };
        body.textContent = '';
        body.appendChild(el('div', { class: 'chips' },
          chip('unknown', 'EXPERIMENTAL — a probability score, not a verdict'), chip(zone.cls, zone.text)));
        body.appendChild(facts([
          ['Detector score', p.toFixed(3) + ' toward AI-generated (0–1; 0.5 is the model’s cutoff)'],
          ['Raw logit', logit.toFixed(3), 'hash'],
          ['What it read', 'center 384×384 crop of this image, resized like the eval'],
        ]));
        body.appendChild(el('p', { class: 'note', text: 'What it can say: this score is evidence, stronger when it is '
          + 'near 0 or 1. What it cannot say: whether the image is real or fake. The model is strongest on 2023–24 '
          + 'diffusion generators, weakest on the newest ones and on small or heavily re-compressed images — '
          + 'most pictures saved off social media are re-compressed.' }));
      } catch (err) {
        body.textContent = '';
        body.appendChild(el('p', { text: 'The experimental check could not run: ' + (err && err.message ? err.message : err) }));
        run.disabled = false;
      }
    },
  });
  body.appendChild(run);
  card.appendChild(body);
  card.appendChild(el('p', { class: 'note', text: 'Detector: ' + DETECTOR.modelSource
    + ' · runtime ' + DETECTOR.engine + ' ' + DETECTOR.engineVersion + ' (pinned, vendored) · model SHA-256 '
    + DETECTOR.modelSha256.slice(0, 16) + '… · measured performance in RESULTS_DETECTOR.md' }));
  sec.appendChild(card);
  return sec;
}

/* ---------- small DOM helpers (same shape as the repo's viewer template) ---------- */

function el(tag, attrs) {
  const node = document.createElement(tag);
  const a = attrs || {};
  Object.keys(a).forEach((k) => {
    const v = a[k];
    if (v === null || v === undefined || v === false) { return; }
    if (k === 'class') { node.className = v; }
    else if (k === 'text') { node.textContent = v; }
    else if (k.slice(0, 2) === 'on') { node.addEventListener(k.slice(2), v); }
    else { node.setAttribute(k, v === true ? '' : String(v)); }
  });
  for (let i = 2; i < arguments.length; i++) { append(node, arguments[i]); }
  return node;
}
function append(node, child) {
  if (child === null || child === undefined || child === false) { return; }
  if (Array.isArray(child)) { child.forEach((c) => append(node, c)); return; }
  node.appendChild(child instanceof Node ? child : document.createTextNode(String(child)));
}
function chip(cls, text) { return el('span', { class: 'chip ' + cls, text }); }
function facts(rows) {
  const dl = el('dl', { class: 'facts' });
  rows.forEach((r) => {
    if (!r) { return; }
    dl.appendChild(el('dt', { text: r[0] }));
    dl.appendChild(el('dd', r[2] ? { class: r[2] } : null, r[1]));
  });
  return dl;
}
function checked() {
  return el('p', {
    class: 'checked',
    text: 'Checked on this device · ' + ENGINE.name + ' ' + ENGINE.version + ' (pinned, vendored)',
  });
}

/* ---------- input policy: JPEG/PNG/WebP, up to 25 MB, sniffed by magic bytes ---------- */

function sniff(bytes) {
  for (const [mime, sig] of MAGIC) {
    if (sig.every((b, i) => bytes[i] === b)) {
      if (mime === 'image/webp') {
        return (bytes[8] === 0x57 && bytes[9] === 0x45 && bytes[10] === 0x42 && bytes[11] === 0x50)
          ? 'image/webp' : null;
      }
      return mime;
    }
  }
  return null;
}
function refusalFor(file, head) {
  if (file.size > MAX_BYTES) {
    return 'over 25 MB (' + (file.size / 1048576).toFixed(1) + ' MB)';
  }
  const mime = sniff(head);
  if (!mime) {
    const ext = (file.name.match(/\.([a-z0-9]+)$/i) || [null, ''])[1].toLowerCase();
    if (ext === 'heic' || ext === 'heif') {
      return 'HEIC — the check supports JPEG, PNG and WebP. Export or share the image as JPEG first.';
    }
    return 'not a JPEG, PNG or WebP file';
  }
  return null;
}

/* ---------- verification ---------- */

async function sha256Hex(buf) {
  const h = await crypto.subtle.digest('SHA-256', buf);
  return Array.from(new Uint8Array(h)).map((b) => b.toString(16).padStart(2, '0')).join('');
}

/* Success/failure/informational code lists, the same fields the repo's runner reads. */
function codeLists(store) {
  const am = (store && store.validation_results && store.validation_results.activeManifest) || null;
  const grab = (key) => new Set(((am && Array.isArray(am[key]) ? am[key] : []))
    .filter((x) => x && typeof x.code === 'string').map((x) => x.code));
  if (am) {
    return { success: grab('success'), failure: grab('failure'), informational: grab('informational') };
  }
  /* Fallback when only the flat validation_status list exists: split by known failure suffixes. */
  const success = new Set();
  const failure = new Set();
  const informational = new Set();
  (((store || {}).validation_status) || []).forEach((x) => {
    if (!x || typeof x.code !== 'string') { return; }
    if (/\.(mismatch|untrusted|expired|revoked|outsideValidity|notTrusted|invalid|error|failure|unavailable|missing|notPresent)$/.test(x.code)) {
      failure.add(x.code);
    } else if (/\.(validated|match|trusted|ok|present|withinValidity)$/.test(x.code)) {
      success.add(x.code);
    } else {
      informational.add(x.code);
    }
  });
  return { success, failure, informational };
}

/* Port of derived_facts.derive() for one manifestStore result. */
function derive(store) {
  const manifests = (store && store.manifests) || {};
  if (!store || Object.keys(manifests).length === 0) {
    return {
      state: 'NO_MANIFEST', manifest: 'absent',
      binding: 'not_checked', signature: 'not_checked', signer_trust: 'not_checked',
    };
  }
  const state = store.validation_state || 'ERROR';
  const { success, failure } = codeLists(store);
  let binding = 'unknown';
  if (success.has('assertion.dataHash.match')) { binding = 'match'; }
  else if ([...failure].some((c) => c.endsWith('dataHash.mismatch'))) { binding = 'mismatch'; }
  let signature = 'unknown';
  if (success.has('claimSignature.validated')) { signature = 'validated'; }
  else if (failure.has('claimSignature.mismatch')) { signature = 'mismatch'; }
  let trust = 'unknown';
  if (success.has('signingCredential.trusted')) { trust = 'trusted'; }
  else if (failure.has('signingCredential.untrusted')) { trust = 'untrusted'; }
  return { state, manifest: 'present', binding, signature, signer_trust: trust };
}

/* Port of claims_from_report(): the active manifest's declared fields. */
function claimsFromStore(store) {
  const manifests = (store && store.manifests) || {};
  const active = manifests[(store && store.active_manifest) || ''] || {};
  const actions = [];
  (Array.isArray(active.assertions) ? active.assertions : []).forEach((a) => {
    if (!a || !String(a.label || '').startsWith('c2pa.actions')) { return; }
    (((a.data) || {}).actions || []).forEach((act) => {
      const keep = {};
      ['action', 'digitalSourceType', 'softwareAgent', 'when', 'parameters'].forEach((k) => {
        if (act && k in act) { keep[k] = act[k]; }
      });
      actions.push(keep);
    });
  });
  return {
    title: active.title ?? null,
    format: active.format ?? null,
    claim_generator: active.claim_generator ?? null,
    claim_generator_info: active.claim_generator_info ?? null,
    signature_info: active.signature_info || {},
    assertion_labels: (Array.isArray(active.assertions) ? active.assertions : []).map((a) => a.label),
    actions,
    ingredients: (Array.isArray(active.ingredients) ? active.ingredients : [])
      .map((g) => ({ title: g.title, format: g.format, relationship: g.relationship })),
    manifest_count: Object.keys(manifests).length,
  };
}

/* Port of template.html overall(): the five honest labels. */
function overall(c) {
  const d = c.derived;
  if (d.manifest === 'absent') { return { cls: 'none', text: 'No credential found', short: 'No credential' }; }
  if (d.manifest !== 'present') { return { cls: 'unknown', text: 'Unknown', short: 'Unknown' }; }
  if (d.binding === 'mismatch') { return { cls: 'broken', text: 'Credential does not match these bytes', short: "Doesn't match" }; }
  if (d.state === 'Invalid') { return { cls: 'broken', text: 'Credential fails validation (see the failure codes)', short: 'Fails validation' }; }
  if ((d.state === 'Valid' || d.state === 'Trusted') && d.binding === 'match' && d.signature === 'validated') {
    return { cls: 'intact', text: 'Credential intact for these bytes', short: 'Intact' };
  }
  return { cls: 'unknown', text: 'Unknown', short: 'Unknown' };
}

function isTestSigner(c) {
  const sig = (c.claims && c.claims.signature_info) || {};
  const hay = [sig.common_name, sig.issuer, sig.org, sig.cert_serial_number].filter(Boolean).join(' ');
  return TEST_CERT_MARKERS.some((m) => hay.includes(m));
}

/* Which pinned list, if any, the signer chains to. 'official' outranks 'interim'. */
function trustState(c) {
  const d = c.derived; const di = c.derived_interim;
  if (!d || d.signer_trust === 'not_checked') { return 'not_checked'; }
  if (d.signer_trust === 'trusted') { return 'official'; }
  if (di && di.signer_trust === 'trusted') { return 'interim'; }
  if (d.signer_trust === 'untrusted') { return isTestSigner(c) ? 'test' : 'untrusted'; }
  return 'unknown';
}

function trustChip(c) {
  switch (trustState(c)) {
    case 'official':
      return { cls: 'intact', text: 'Signer chains to the pinned official C2PA trust list', short: 'Trusted: official list' };
    case 'interim':
      return { cls: 'interim', text: 'Signer chains to the pinned CAI interim trust list (frozen; the Verify site’s list)', short: 'Trusted: interim list' };
    case 'test':
      return { cls: 'test', text: 'Signed with the public C2PA TEST credential (its private key is public)', short: 'TEST credential' };
    case 'untrusted':
      return { cls: 'untrusted', text: 'Signer on neither pinned trust list', short: 'Untrusted signer' };
    case 'not_checked':
      return c.derived.manifest === 'absent'
        ? { cls: 'na', text: 'No signer to check (no manifest)', short: 'Trust n/a' }
        : { cls: 'unknown', text: 'Trust unknown (no usable verifier result)', short: 'Trust unknown' };
    default:
      return { cls: 'unknown', text: 'Trust unknown', short: 'Trust unknown' };
  }
}

function trustMeaning(c, pol) {
  const d = pol === 'interim' ? c.derived_interim : c.derived;
  if (!d) { return 'This policy was not run (no manifest was found in the first pass).'; }
  if (d.signer_trust === 'not_checked') {
    return d.manifest === 'absent'
      ? 'No manifest, so there was no signer to check.'
      : 'The verifier did not produce a usable result, so the signer was not checked.';
  }
  const listName = pol === 'interim' ? 'the frozen CAI interim list' : 'the official C2PA conformance list';
  if (d.signer_trust === 'trusted') {
    const t = pol === 'interim' ? TRUST.INTERIM_TRUST_LIST : TRUST.MANIFEST_TRUST_LIST;
    return 'The signer’s certificate chain ends at a root on ' + listName + ' (' + t.certificates
      + ' CAs, fetched ' + t.fetched + ', pinned by SHA-256). Trusted means the signer is a listed '
      + 'authority — it does not mean the declared claims are true.'
      + (d.state === 'Invalid' ? ' The overall state is still Invalid (see the failure codes).' : '');
  }
  if (d.signer_trust === 'untrusted') {
    return pol === 'interim'
      ? 'The signer does not chain to the frozen interim list either — the same list the C2PA Verify site uses. '
        + (isTestSigner(c)
          ? 'The signer declares the public C2PA TEST credential, whose private key is published: anyone can produce this. It is not production trust.'
          : 'Not evidence of manipulation: many legitimate signers predate both lists.')
      : 'The signer does not chain to the official conformance list. It may still chain to the frozen interim list — see the other policy.';
  }
  return 'Unknown.';
}

/* ---------- fixed reading rules: "can and cannot conclude" ---------- */

function reading(c) {
  const o = overall(c);
  const d = c.derived;
  const can = []; const cannot = []; const unknown = []; let what;
  if (o.cls === 'none') {
    what = 'No C2PA manifest was found in this file.';
    can.push('The verifier found no C2PA manifest in this file.');
    cannot.push('Anything about origin. Removing a credential is easy and leaves no trace in the picture, and many tools never add one.');
    cannot.push('That the image is AI-generated, edited or authentic. A missing credential is not evidence either way.');
    unknown.push('Who made the file, whether it was ever signed, and whether it was edited.');
    unknown.push('Whether a credential is stored outside the file: remote (cloud) manifests are not fetched.');
    unknown.push('Whether the platform you got it from stripped the credential when it was uploaded — many do.');
  } else if (o.cls === 'intact') {
    what = 'The file carries a C2PA manifest that validates for these exact bytes.';
    can.push('The claim signature validates (claimSignature.validated), and the hard-binding hash matches these bytes '
      + '(assertion.dataHash.match), so the bound bytes have not changed since signing.');
    const ts = trustState(c);
    if (ts === 'official') {
      can.push('The signer chains to the pinned official C2PA conformance trust list: a listed conformant authority signed this.');
    } else if (ts === 'interim') {
      can.push('The signer chains to the pinned CAI interim trust list (frozen; the list the C2PA Verify site uses).');
    } else if (ts === 'test') {
      can.push('The signer is the public C2PA TEST credential — a valid signature anyone can produce; it is not production trust.');
    } else if (ts === 'untrusted') {
      can.push('The signature is intact, but the signer is on neither pinned trust list.');
    }
    cannot.push('That the declared claims are true, or that the scene is real. Validation checks that the claims are signed and unchanged since signing, not that they are true.');
    cannot.push('What happened to the content before it was signed.');
    if (ts !== 'official' && ts !== 'interim') {
      unknown.push('Who the signer is in a production sense: they are on neither pinned trust list.');
    }
  } else if (o.short === "Doesn't match") {
    what = 'The file carries a C2PA manifest, but its hard-binding hash does not match these bytes.';
    if (d.signature === 'validated') {
      can.push('These are not the bytes the credential was signed for: its hard-binding hash does not match them '
        + '(assertion.dataHash.mismatch). The verifier reports the credential as ' + d.state + '.');
      can.push('The claim signature still validates: the claim itself is intact, but it does not bind to these bytes.');
    } else {
      can.push('The hard-binding hash in the manifest does not match these bytes (assertion.dataHash.mismatch), and the '
        + 'claim signature was not reported as validated. The verifier reports the credential as ' + d.state + '.');
    }
    cannot.push('Whether the file was edited, re-encoded or given a credential copied from another file. All of these give the same mismatch.');
    cannot.push('What differs, or where. Validation does not locate the difference.');
    cannot.push('Anything about whether the content is genuine.');
    unknown.push('What the signed content was, beyond what the manifest records.');
  } else if (o.cls === 'broken') {
    const fails = [...codeLists(c.store).failure].filter((k) => k !== 'signingCredential.untrusted');
    what = 'The file carries a C2PA manifest that fails validation.';
    can.push('The verifier reports the credential as Invalid' + (fails.length ? ', with these failure codes: ' + fails.join(', ') + '.' : '.'));
    cannot.push('Which of the declared claims, if any, still hold. An invalid credential supports no conclusion about origin.');
    cannot.push('Anything about whether the content is genuine.');
    unknown.push('What the failure means for this file beyond the reported codes.');
  } else if (d.state === 'ERROR') {
    what = 'The verifier did not produce a usable result for this file, so the result is unknown. See the raw output.';
    cannot.push('Anything about this file’s credential: there is no usable result.');
    unknown.push('Whether the file carries a C2PA manifest.');
  } else {
    what = 'This tool cannot classify the verifier’s result for this file. See the raw output.';
    cannot.push('Anything beyond the raw verifier output: the result does not match a case this tool recognises.');
    unknown.push('What this result means.');
  }
  if (d.manifest === 'present') {
    unknown.push('Revocation: OCSP fetching is off, so no certificate revocation status was fetched.');
    unknown.push('Timestamp-authority trust is checked against the pinned C2PA TSA list; the verifier’s own timestamp checks still apply.');
    if (c.claims && c.claims.manifest_count > 1) {
      unknown.push('This file carries ' + c.claims.manifest_count + ' manifests; the newest (active) one is shown.');
    }
  }
  return {
    label: c.name,
    sublabel: c.mime + ' · ' + c.size.toLocaleString('en') + ' bytes',
    title: c.name,
    what,
    image_alt: 'The checked file ' + c.name + ', shown from the exact bytes that were checked',
    can, cannot, unknown,
  };
}

/* ---------- report cards ---------- */

function codeEntriesForStore(store, filter) {
  const am = ((store || {}).validation_results || {}).activeManifest || {};
  const out = [];
  ['success', 'informational', 'failure'].forEach((kind) => {
    const seen = {};
    (Array.isArray(am[kind]) ? am[kind] : []).forEach((x) => {
      if (!x || typeof x.code !== 'string' || !filter(x.code)) { return; }
      if (seen[x.code]) { seen[x.code].count += 1; return; }
      seen[x.code] = { kind, code: x.code, explanation: typeof x.explanation === 'string' ? x.explanation : '', count: 1 };
      out.push(seen[x.code]);
    });
  });
  if (!out.length && (store || {}).validation_status) {
    /* flat-list fallback: entries are prefixed so the kinds still render */
    (store.validation_status || []).forEach((x) => {
      if (!x || typeof x.code !== 'string' || !filter(x.code)) { return; }
      out.push({ kind: 'status', code: x.code, explanation: typeof x.explanation === 'string' ? x.explanation : '', count: 1 });
    });
  }
  return out;
}
function codeEntries(c, filter) { return codeEntriesForStore(c.store, filter); }
function codeList(entries) {
  if (!entries.length) { return el('p', { class: 'note', text: 'No codes of this kind were reported.' }); }
  return el('ul', { class: 'codes' }, entries.map((e) => el('li', null,
    el('span', { class: 'kind', text: e.kind }), el('span', { class: 'k', text: e.code }),
    e.count > 1 ? ' ×' + e.count : '',
    e.explanation ? el('span', { class: 'x', text: ' — ' + e.explanation }) : null)));
}

function imageSection(c) {
  const ip = c.reading;
  const img = el('img', { alt: ip.image_alt, decoding: 'async' });
  img.src = c.objectUrl;
  return el('section', { 'aria-labelledby': 'sec-image' },
    el('h3', { class: 'section-title', id: 'sec-image', text: '1. The image' }),
    el('div', { class: 'media' },
      el('figure', null, img,
        el('figcaption', { text: 'Shown from the exact bytes that were checked (they never left this device).' })),
      el('div', { class: 'card' },
        facts([
          ['File', c.name],
          ['Format', c.mime + ', ' + c.size.toLocaleString('en') + ' bytes'],
          ['File SHA-256', c.sha256, 'hash'],
          ['Checked', c.checkedAt],
        ]),
        checked())));
}

function declaredAssertions(store) {
  const m = ((store || {}).manifests || {})[(store || {}).active_manifest] || {};
  const items = [];
  (Array.isArray(m.assertions) ? m.assertions : []).forEach((a) => {
    if (!a || String(a.label).startsWith('c2pa.actions')) { return; }
    const data = a.data; const parts = [];
    if (data && typeof data === 'object' && !Array.isArray(data)) {
      Object.keys(data).forEach((k) => {
        if (k === '@context') { return; }
        const v = data[k];
        if (v === null || typeof v !== 'object') { parts.push(k + ': ' + v); }
        else if (Array.isArray(v)) { parts.push(k + ': [' + v.length + ' value' + (v.length === 1 ? '' : 's') + ']'); }
        else { parts.push(k + ': {…}'); }
      });
    }
    items.push(el('li', null, el('span', { class: 'mono', text: a.label }), parts.length ? ' — ' + parts.join('; ') : ''));
  });
  return items;
}

function signerCard(c) {
  const card = el('section', { class: 'card', 'aria-labelledby': 'h-signer' },
    el('h3', { id: 'h-signer', text: 'Signer and declared claims' }));
  const absent = c.derived.manifest === 'absent';
  if (absent || !c.store) {
    card.appendChild(el('div', { class: 'chips' },
      absent ? chip('na', 'Unknown: no manifest') : chip('unknown', 'Unknown: no readable result')));
    card.appendChild(el('p', { text: absent
      ? 'There is no manifest, so there is no signer and there are no declared claims to read.'
      : 'The verifier did not produce a readable result for this file, so the signer and the declared claims are unknown.' }));
    card.appendChild(checked());
    return card;
  }
  const cl = c.claims; const sig = cl.signature_info || {};
  const gen = cl.claim_generator || (Array.isArray(cl.claim_generator_info) ? cl.claim_generator_info : [])
    .map((g) => (g && g.name ? g.name + (g.version ? ' ' + g.version : '') : '?')).join(', ');
  const actions = (cl.actions || []).map((a) => {
    let t = a.action;
    if (a.digitalSourceType) {
      const st = String(a.digitalSourceType).split('/').pop();
      t += ' · digitalSourceType ' + st + (SOURCE_TYPE_WORDS[st] ? ' (declared: ' + SOURCE_TYPE_WORDS[st] + ')' : '');
    }
    if (a.parameters && a.parameters.name) { t += ' · ' + a.parameters.name; }
    return el('li', { text: t });
  });
  const ingredients = (cl.ingredients || [])
    .map((g) => el('li', { text: (g.title || '?') + ' (' + (g.relationship || '?') + ', ' + (g.format || '?') + ')' }));
  const others = declaredAssertions(c.store);
  card.appendChild(el('div', { class: 'chips' }, chip('declared', 'Declared by the signer, not verified as true'),
    isTestSigner(c) ? chip('test', 'Public C2PA TEST credential') : null));
  card.appendChild(facts([
    ['Certificate issuer', sig.issuer || 'not reported'],
    ['Certificate common name', sig.common_name || 'not reported'],
    ['Signature algorithm', sig.alg || 'not reported'],
    ['Timestamp', sig.time ? sig.time + ' (from the signature’s timestamp)' : 'None: the signature carries no timestamp'],
    ['Declared title', cl.title || 'none'],
    ['Claim generator', gen || 'not reported'],
    ['Manifests in file', String(cl.manifest_count)],
  ]));
  if (actions.length) { card.appendChild(el('p', { class: 'note', text: 'Declared actions:' })); card.appendChild(el('ul', { class: 'assertions' }, actions)); }
  if (ingredients.length) { card.appendChild(el('p', { class: 'note', text: 'Declared ingredients:' })); card.appendChild(el('ul', { class: 'assertions' }, ingredients)); }
  if (others.length) { card.appendChild(el('p', { class: 'note', text: 'Other declared assertions (as the verifier reported them):' })); card.appendChild(el('ul', { class: 'assertions' }, others)); }
  card.appendChild(el('p', { class: 'note', text: 'Everything in this box is the signer’s statement. Validation checks that it is signed and unchanged since signing, not that it is true.' }));
  card.appendChild(checked());
  return card;
}

function bindingCard(c) {
  const d = c.derived;
  const card = el('section', { class: 'card', 'aria-labelledby': 'h-binding' },
    el('h3', { id: 'h-binding', text: 'Asset binding (hash match)' }));
  if (d.binding === 'not_checked' && d.manifest !== 'absent') {
    card.appendChild(el('div', { class: 'chips' }, chip('unknown', 'Unknown: no usable verifier result')));
    card.appendChild(el('p', { text: 'The verifier did not produce a usable result for this file, so the binding was not checked.' }));
  } else if (d.binding === 'not_checked') {
    card.appendChild(el('div', { class: 'chips' }, chip('na', 'Not applicable: no manifest')));
    card.appendChild(el('p', { text: 'Nothing to check: there is no manifest, so there is no hash binding the claims to these bytes.' }));
  } else if (d.binding === 'match') {
    card.appendChild(el('div', { class: 'chips' }, chip('intact', 'Hash matches these bytes')));
    card.appendChild(el('p', { text: (d.state === 'Valid' || d.state === 'Trusted')
      ? 'The manifest’s hard-binding hash matches this file, so the bound bytes have not changed since signing.'
      : 'The hard-binding hash recorded in the manifest matches this file, but the overall result is not Valid or Trusted (see the codes), so this alone does not show that the bytes are unchanged since signing.' }));
  } else if (d.binding === 'mismatch') {
    card.appendChild(el('div', { class: 'chips' }, chip('broken', 'Hash does not match these bytes')));
    card.appendChild(el('p', { text: d.signature === 'validated'
      ? 'The hard-binding hash in the manifest does not match this file: these are not the bytes that were signed. A harmless re-encode, a deliberate edit and a credential copied from another file all give this result, and the check does not say which, or what differs.'
      : 'The hard-binding hash in the manifest does not match this file. The claim signature was not reported as validated either, so it is unknown what the credential was signed for.' }));
  } else {
    card.appendChild(el('div', { class: 'chips' }, chip('unknown', 'Unknown')));
    card.appendChild(el('p', { text: 'The result has no data-hash entry, so the binding is unknown.' }));
  }
  card.appendChild(codeList(codeEntries(c, (k) => /dataHash/.test(k))));
  card.appendChild(checked());
  return card;
}

function signatureCard(c) {
  const d = c.derived;
  const card = el('section', { class: 'card', 'aria-labelledby': 'h-sig' },
    el('h3', { id: 'h-sig', text: 'Signature validation' }));
  if (d.signature === 'not_checked' && d.manifest !== 'absent') {
    card.appendChild(el('div', { class: 'chips' }, chip('unknown', 'Unknown: no usable verifier result')));
    card.appendChild(el('p', { text: 'The verifier did not produce a usable result for this file, so the signature was not checked.' }));
  } else if (d.signature === 'not_checked') {
    card.appendChild(el('div', { class: 'chips' }, chip('na', 'Not applicable: no manifest')));
    card.appendChild(el('p', { text: 'Nothing to validate: there is no claim signature in this file.' }));
  } else if (d.signature === 'validated') {
    const uri = codeEntries(c, (k) => /^assertion\.hashedURI\./.test(k));
    const uriBad = uri.some((e) => e.code === 'assertion.hashedURI.mismatch');
    const uriOk = !uriBad && uri.some((e) => e.code === 'assertion.hashedURI.match');
    card.appendChild(el('div', { class: 'chips' }, chip('intact', 'Claim signature validates')));
    card.appendChild(el('p', { text: (uriBad
      ? 'The claim signature validates, but at least one assertion it lists no longer matches its recorded hash (assertion.hashedURI.mismatch), so the credential fails validation.'
      : d.state === 'Invalid' && d.binding !== 'mismatch'
        ? 'The claim signature validates, but the verifier still reports the credential as Invalid. The reason is in the failure codes.'
        : uriOk ? 'The claim signature validates, and the assertions it lists are unchanged.' : 'The claim signature validates.')
      + (d.binding === 'mismatch' ? ' The claim itself is intact, but it does not bind to these bytes (see Asset binding).' : '') }));
  } else {
    card.appendChild(el('div', { class: 'chips' },
      chip(d.signature === 'mismatch' ? 'broken' : 'unknown',
        d.signature === 'mismatch' ? 'Claim signature does not validate' : 'Unknown')));
  }
  const ts = codeEntries(c, (k) => /^timeStamp/.test(k));
  card.appendChild(codeList(codeEntries(c, (k) => /^claimSignature|^assertion\.hashedURI/.test(k)).concat(ts)));
  if (ts.length) {
    card.appendChild(el('p', { class: 'note', text: 'Timestamp authorities are checked against the pinned C2PA TSA trust list; '
      + 'timestamp-authority revocation is not fetched.' }));
  } else if (d.signature !== 'not_checked') {
    card.appendChild(el('p', { class: 'note', text: 'No timestamp: this result depends on the signing certificate being inside its validity period.' }));
  }
  card.appendChild(checked());
  return card;
}

function trustCard(c) {
  const card = el('section', { class: 'card', 'aria-labelledby': 'h-trust' },
    el('h3', { id: 'h-trust', text: 'Trust check (two pinned lists)' }));
  const t = trustChip(c);
  card.appendChild(el('div', { class: 'chips' }, chip(t.cls, t.text)));
  const policies = [
    ['official', 'Official C2PA conformance list', c.derived, c.store],
    ['interim', 'CAI interim list (frozen; Verify’s list)', c.derived_interim, c.store_interim],
  ];
  const rows = policies.map(([pol, name, d, store]) => {
    const code = d ? codeEntriesForStore(store, (k) => /^signingCredential/.test(k)).map((e) => e.code).join(', ') : '';
    return el('tr', null,
      el('td', null, el('strong', { text: name })),
      el('td', null, el('span', { class: 'mono', text: d ? '"' + d.state + '"' + (code ? ' · ' + code : '') : 'not run' })),
      el('td', { text: trustMeaning(c, pol) }));
  });
  card.appendChild(el('table', { class: 'policy' },
    el('thead', null, el('tr', null,
      el('th', { scope: 'col', text: 'Trust list' }),
      el('th', { scope: 'col', text: 'Verifier state and code' }),
      el('th', { scope: 'col', text: 'What it means here' }))),
    el('tbody', null, rows)));
  const tl = TRUST.MANIFEST_TRUST_LIST; const ti = TRUST.INTERIM_TRUST_LIST; const tsa = TRUST.TSA_TRUST_LIST;
  card.appendChild(el('p', { class: 'note', text: 'Pinned trust sources: official conformance list ('
    + tl.certificates + ' CAs, SHA-256 ' + tl.sha256.slice(0, 16) + '…, ' + tl.fetched + ', github.com/c2pa-org/conformance-public) '
    + '+ its TSA list (' + tsa.certificates + ' authorities); '
    + 'frozen CAI interim list (' + ti.certificates + ' CAs, SHA-256 ' + ti.sha256.slice(0, 16) + '…, ' + ti.fetched
    + ', contentcredentials.org/trust/anchors.pem), which also serves as the timestamp-authority anchors for that pass — '
    + 'as c2patool’s legacy mode does. Nothing is fetched at check time.' }));
  card.appendChild(checked());
  return card;
}

function concludeSection(c) {
  const ip = c.reading;
  function block(cls, title, items) {
    return el('div', { class: 'card ' + cls }, el('h4', { text: title, style: 'margin:0;font-size:.95rem' }),
      el('ul', null, (items.length ? items : ['None recorded.']).map((t) => el('li', { text: t }))));
  }
  return el('section', { 'aria-labelledby': 'sec-conclude' },
    el('h3', { class: 'section-title', id: 'sec-conclude', text: '3. What this can and cannot conclude' }),
    el('p', { class: 'interp-label', text: 'Fixed reading rules applied to the results above — the same rules for every file. It is not a real-or-fake verdict.' }),
    el('div', { class: 'conclude' }, block('can', 'Can conclude', ip.can), block('cannot', 'Cannot conclude', ip.cannot), block('unk', 'Unknown', ip.unknown)));
}

function evidenceSection(c) {
  const det = el('details', { class: 'evidence' },
    el('summary', { text: 'Raw verifier output (manifest store JSON)' }),
    el('div', { class: 'evidence-body' },
      el('p', { class: 'note', text: 'Exactly what the pinned verifier returned for these bytes, before this page interpreted it.' }),
      el('pre', { class: 'raw', tabindex: '0', text: c.store ? JSON.stringify(c.store, null, 2) : String(c.error || 'no result') })));
  const tool = el('details', { class: 'evidence' },
    el('summary', { text: 'Verifier, trust lists and settings' }),
    el('div', { class: 'evidence-body' },
      facts([
        ['Verifier', ENGINE.name + ' ' + ENGINE.version + ' (' + ENGINE.license + '), vendored at vendor/c2pa-web/'],
        ['Package integrity', ENGINE.npmIntegrity, 'hash'],
        ['Trust lists', 'two passes: (1) official C2PA conformance lists — ' + TRUST.MANIFEST_TRUST_LIST.certificates
          + ' signing CAs (SHA-256 ' + TRUST.MANIFEST_TRUST_LIST.sha256 + ') + ' + TRUST.TSA_TRUST_LIST.certificates
          + ' timestamp authorities (SHA-256 ' + TRUST.TSA_TRUST_LIST.sha256 + '), ' + TRUST.MANIFEST_TRUST_LIST.fetched
          + '; (2) frozen CAI interim list — ' + TRUST.INTERIM_TRUST_LIST.certificates + ' CAs (SHA-256 '
          + TRUST.INTERIM_TRUST_LIST.sha256 + '), ' + TRUST.INTERIM_TRUST_LIST.fetched
          + ' — the list verify.contentauthenticity.org uses'],
        ['Settings', 'remoteManifestFetch: off · ocspFetch: off · timestamp trust: pinned TSA list'],
        ['Network', 'This page declares connect-src \'self\' — it can fetch only this site’s own files; your image is '
          + 'never sent anywhere. Confirm in DevTools → Network, or check it in airplane mode.'],
      ])));
  function setAll(open) {
    caseEl.querySelectorAll('details.evidence').forEach((d) => { d.open = open; });
  }
  return el('section', { 'aria-labelledby': 'sec-evidence' },
    el('div', { class: 'evidence-head' },
      el('h3', { id: 'sec-evidence', text: '5. Evidence' }),
      el('div', { class: 'chips' },
        el('button', { class: 'btn', type: 'button', onclick: () => setAll(true), text: 'Expand all' }),
        el('button', { class: 'btn', type: 'button', onclick: () => setAll(false), text: 'Collapse all' }))),
    det, tool);
}

function renderCase(c) {
  caseEl.textContent = '';
  const ip = c.reading; const o = overall(c); const t = trustChip(c);
  caseEl.appendChild(el('div', { class: 'case-head' },
    el('h2', { id: 'case-title', tabindex: '-1', text: ip.title }),
    el('p', { text: ip.what }),
    el('div', { class: 'chips' }, chip(o.cls, o.text), chip(t.cls, t.text))));
  caseEl.appendChild(imageSection(c));
  caseEl.appendChild(el('h3', { class: 'section-title', text: '2. What the verifier checked' }));
  caseEl.appendChild(el('div', { class: 'checks' }, signerCard(c), bindingCard(c), signatureCard(c), trustCard(c)));
  caseEl.appendChild(concludeSection(c));
  if (c.file) { caseEl.appendChild(detectorSection(c)); }
  caseEl.appendChild(evidenceSection(c));
}

function renderNav() {
  listEl.textContent = '';
  cases.forEach((c, i) => {
    const o = c.derived ? overall(c) : { cls: 'pending', short: c.pendingLabel || 'Checking…' };
    const t = c.derived ? trustChip(c) : null;
    const btn = el('button', {
      class: 'case-btn', type: 'button', 'aria-current': String(current === c.id),
      onclick: () => selectCase(c.id, true),
      onkeydown: (ev) => {
        const k = ev.key;
        const step = (k === 'ArrowDown' || k === 'ArrowRight') ? 1 : (k === 'ArrowUp' || k === 'ArrowLeft') ? -1 : 0;
        if (!step) { return; }
        ev.preventDefault();
        const next = cases[(i + step + cases.length) % cases.length];
        selectCase(next.id, false);
        const nb = listEl.querySelector('.case-btn[data-id="' + next.id + '"]');
        if (nb) { nb.focus(); }
      },
    },
    el('span', { class: 't', text: c.name }),
    el('span', { class: 's', text: c.sublabel }),
    el('span', { class: 'chips' }, chip(o.cls, o.short), t ? chip(t.cls, t.short) : null));
    btn.setAttribute('data-id', c.id);
    listEl.appendChild(el('li', null, btn));
  });
}

function selectCase(id, focus) {
  if (!Object.prototype.hasOwnProperty.call(byId, id)) { id = cases[0] && cases[0].id; }
  if (!id) { return; }
  current = id;
  renderNav();
  const c = byId[id];
  if (c.derived) { renderCase(c); } else { caseEl.textContent = ''; }
  const h = document.getElementById('case-title');
  if (focus && h) { h.focus(); }
}

/* ---------- intake ---------- */

let seq = 0;
async function checkFile(file) {
  const head = new Uint8Array(await file.slice(0, 16).arrayBuffer());
  const c = {
    id: 'f' + (++seq), file, name: file.name || 'unnamed file', size: file.size,
    mime: file.type || 'unknown', checkedAt: null, derived: null, claims: null,
    store: null, error: null, objectUrl: URL.createObjectURL(file),
    sublabel: (file.type || '?') + ' · ' + file.size.toLocaleString('en') + ' bytes',
    pendingLabel: 'Checking…',
  };
  const refusal = refusalFor(file, head);
  if (refusal) {
    c.derived = { state: 'REFUSED', manifest: 'unknown', binding: 'not_checked', signature: 'not_checked', signer_trust: 'not_checked' };
    c.error = 'Refused: ' + refusal;
    c.sublabel = 'refused — ' + refusal;
    c.reading = {
      label: c.name, sublabel: c.sublabel, title: c.name,
      what: 'This file was refused before checking: ' + refusal + '. The verifier never saw it.',
      image_alt: 'The refused file ' + c.name,
      can: ['Nothing — the file was refused before checking.'],
      cannot: ['Anything about this file’s credential or content. Only JPEG, PNG and WebP up to 25 MB are accepted.'],
      unknown: ['Whether the file carries a C2PA credential.'],
    };
    return c;
  }
  c.mime = sniff(head) || file.type || 'unknown';
  try {
    const { mod, c2pa, ctxOfficial, ctxInterim } = await ensureEngine();
    const buf = await file.arrayBuffer();
    c.sha256 = await sha256Hex(buf);
    const blob = new Blob([buf], { type: c.mime });
    let store = null; let storeInterim = null;
    const reader = await mod.Reader.fromBlob(c2pa, blob.type || undefined, blob, ctxOfficial);
    try { store = reader ? await reader.manifestStore() : null; }
    finally { if (reader) { await reader.free(); } }
    if (store && store.manifests && Object.keys(store.manifests).length) {
      const r2 = await mod.Reader.fromBlob(c2pa, blob.type || undefined, blob, ctxInterim);
      try { storeInterim = r2 ? await r2.manifestStore() : null; }
      finally { if (r2) { await r2.free(); } }
    }
    c.store = store;
    c.store_interim = storeInterim;
    c.derived = derive(store);
    c.derived_interim = storeInterim ? derive(storeInterim) : null;
    c.claims = claimsFromStore(store);
  } catch (err) {
    c.derived = { state: 'ERROR', manifest: 'unknown', binding: 'not_checked', signature: 'not_checked', signer_trust: 'not_checked' };
    c.error = String(err && err.message ? err.message : err);
  }
  c.checkedAt = new Date().toISOString().replace('T', ' ').slice(0, 19);
  c.sublabel = c.mime + ' · ' + c.size.toLocaleString('en') + ' bytes';
  c.reading = reading(c);
  return c;
}

async function intake(fileList) {
  const files = [...fileList].filter((f) => f && f.size !== undefined);
  if (!files.length) { return; }
  filesEl.hidden = false;
  for (const f of files) {
    const placeholder = { id: 'p' + (++seq), name: f.name, sublabel: 'queued', pendingLabel: 'Queued', derived: null };
    cases.push(placeholder);
    byId[placeholder.id] = placeholder;
    renderNav();
    const c = await checkFile(f);
    const idx = cases.indexOf(placeholder);
    if (idx >= 0) { cases[idx] = c; }
    delete byId[placeholder.id];
    byId[c.id] = c;
    if (!current || current === placeholder.id) { selectCase(c.id, false); } else { renderNav(); }
  }
}

/* Debug/inspection handle: the raw results the verifier produced, for tests and tinkerers. */
window.__evidelle = { cases };

/* Installable + fully offline after first visit. Failure to register only means
 * no offline caching — the check still works. */
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js').catch(() => {});
  });
}

const input = document.getElementById('file-input');
input.addEventListener('change', () => { intake(input.files); input.value = ''; });
const drop = document.getElementById('drop');
['dragenter', 'dragover'].forEach((e) => drop.addEventListener(e, (ev) => { ev.preventDefault(); drop.classList.add('dragover'); }));
['dragleave', 'drop'].forEach((e) => drop.addEventListener(e, (ev) => { ev.preventDefault(); drop.classList.remove('dragover'); }));
drop.addEventListener('drop', (ev) => { if (ev.dataTransfer && ev.dataTransfer.files.length) { intake(ev.dataTransfer.files); } });

/* ---------- footer ---------- */

(function about() {
  const f = document.getElementById('about');
  f.appendChild(el('h2', { text: 'About this check' }));
  f.appendChild(el('p', { text: 'This page runs the pinned C2PA WebAssembly verifier on files you choose, entirely on '
    + 'this device. It answers a narrow question — is there a C2PA credential here, is it intact for these bytes, and '
    + 'is the signer on the pinned production trust list — and reports what stays unknown. It is not a real-or-fake '
    + 'verdict and not an AI detector.' }));
  f.appendChild(facts([
    ['Verifier', ENGINE.name + ' ' + ENGINE.version + ' (' + ENGINE.license + '), vendored under vendor/ — npm integrity ' + ENGINE.npmIntegrity],
    ['Trust lists', 'official C2PA conformance list (' + TRUST.MANIFEST_TRUST_LIST.certificates + ' CAs) + TSA list ('
      + TRUST.TSA_TRUST_LIST.certificates + ') + frozen CAI interim list (' + TRUST.INTERIM_TRUST_LIST.certificates
      + ' CAs) — all pinned by SHA-256, fetched ' + TRUST.MANIFEST_TRUST_LIST.fetched],
    ['Accepted inputs', 'JPEG, PNG or WebP up to 25 MB, sniffed by magic bytes — other types are refused'],
    ['Experimental check', 'Optional on-device AI-image score (OwensLab/commfor-model-384, fp16 ONNX, pinned ' + DETECTOR.modelSha256.slice(0, 16) + '…) — evidence, never a verdict'],
    ['Not evaluated', 'Certificate revocation (OCSP off), remote (cloud) manifests, watermarks, SynthID'],
    ['Note on platforms', 'Many social platforms strip credentials on upload, so “no credential” is the common answer — and it says nothing either way'],
  ]));
})();
