# Evidence viewer: summary-label logic

The local C2PA evidence viewer shows one summary label per file. This folder holds only that logic and its tests.

- `src/template.html`: the viewer page template. Its `overall()` function picks the label:
  - "Intact" only when c2patool's own state is Valid or Trusted, the data hash matched and the claim signature
    validated;
  - "Doesn't match" when the data hash does not match these bytes;
  - "Fails validation" for any other result that c2patool reports as Invalid;
  - "No credential" when there is no manifest, and "Unknown" for everything else, including states it does not know.
- `src/derived_facts.py`: `derive()`, which turns one c2patool summary (state, success codes, failure codes) into the
  facts `overall()` reads. It is copied unchanged from the viewer's capture script.
- `tests/`: runs the template's own `overall()` under node on synthetic state/code patterns. It also checks that
  the previous `overall()` labelled two of those patterns "Intact".

## Run the tests

Needs Python 3 (standard library only) and node. Nothing is installed or downloaded.

    cd viewer
    python3 -I -B -m unittest discover -s tests -v

## Limits

- The fixture patterns are hand-written. They are not measured validation results and not evidence of accuracy.
- This folder cannot build or show the viewer page: the build script, the recorded evidence and the images are not
  included.
- The labels describe credential checks only. They are not real-or-fake verdicts.
