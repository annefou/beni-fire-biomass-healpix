# 01 — Quote-with-comment (paper-rooted chains)

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> If this is a question-rooted chain, use `01_pico.md` or `01_pcc.md` instead — see `docs/chain-decision-tree.md`.
>
> **After choosing the chain shape, delete the two step-1 alternates you aren't using.** Once you've decided this chain is paper-rooted and keep `01_quote.md`, run:
> ```bash
> rm nanopubs/drafts/01_pico.md nanopubs/drafts/01_pcc.md
> ```

**Form heading:** *"Annotate a paper quotation — Annotating a paper quotation with personal interpretation"*

## Field-by-field draft

<!-- field: paper -->
### Cited DOI (text input, required)

Format: starts with `10.` — bare DOI, **NOT** `https://doi.org/...` form.

```
10.1126/science.1210465
```

### Quote mode (radio button)

- [x] **Quote whole text (less than 500 characters)**
- [ ] Quote start/end *(use this if the quote exceeds 500 chars)*

<!-- field: quotation -->
### The exact quotation from the paper (max. 500 characters) (textarea, required)

Verbatim from the paper PDF in `paper/`. Character-for-character. ≤ 500 chars in whole-text mode.

> SOURCE: abstract of the paper, retrieved via the OpenAlex API (2026-09-27). **Verify character-for-character against the PDF in `paper/` before publishing.**

```
Climate influences tree cover globally but, at intermediate rainfall (1000 to 2500 millimeters) with mild seasonality (less than 7 months), tree cover is bimodal, and only fire differentiates between savanna and forest.
```

Character count: 219 / 500.

<!-- field: quotation-end -->
### End of quotation (optional - use when quoting beginning and end of a longer passage, max. 500 characters) (textarea, optional)

Only when quoting the beginning *and* end of a longer passage — set the mode above to
**Quote start/end**, put the opening phrase under the previous heading and the closing
phrase here. Leave empty for a single short quote.

```

```

<!-- field: comment -->
### Our interpretation and explanation of why this quotation is relevant (max. 800 characters) (textarea, required)

Why this quote matters and what the replication tests. Connect the paper's claim to the work this repo does. Don't repeat the quote.

```
This is the claim we test regionally with independent, newer data: if fire, not climate alone, separates savanna from forest at intermediate rainfall, then within a mosaic in that rainfall band the share burned should fall with pre-fire biomass, and should do so within each rainfall band, not only across them. We test it in the Beni lowlands of Bolivia (CHELSA annual rainfall inside 1000–2500 mm) with ESA Biomass CCI 2023 and ESA Fire_cci 2024 burned area, joined on one equal-area HEALPix grid on the WGS84 ellipsoid (healpix-connector, GRID4EARTH). One region and one fire year: a test of consistency, not of the feedback's direction.
```

Character count: 640 / 800.

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 01.
