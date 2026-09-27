# 05 — FORRT Replication Outcome

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify the actual numerical results first** by reading `results/` and `notebooks/03_analysis.py`. Don't quote numbers from memory. See `docs/verify-before-drafting.md`.

## Field-by-field draft

<!-- field: outcome -->
### Short URI suffix for outcome ID (text input, required)

Slug. Use kebab-case.

```
beni-fire-biomass-healpix-2024-outcome
```

<!-- field: label -->
### Plain-text label for the outcome (text input, required)

Descriptive title.

```
Burned share falls with pre-fire biomass within rainfall bands: consistent with Staver et al. 2011, Beni 2024
```

<!-- field: study -->
### Choose study (search/select, required)

URI of the Replication Study published in step 04. Pull from `nanopubs/PUBLISHED.md`.

```
<URI of step 04, from nanopubs/PUBLISHED.md>
```

<!-- field: repo -->
### Repository URL (text input, required)

Use the Zenodo **version DOI** URL for the release the results came from — not a
bare branch URL, and not the concept DOI.

> **Why not the bare repo URL.** `https://github.com/ORG/REPO` names a *moving
> branch*. This Outcome asserts "this code produced this number", in a signed,
> immutable record. A branch URL means that assertion points at whatever `main`
> happens to be years from now — code that may never have produced the number
> above. A concept DOI has the same flaw: it resolves to the latest version.
> The version DOI pins the exact release. `docs/chain-decision-tree.md` § Anchor
> ranks the options: SWHID > Zenodo DOI > repo URL > Wayback.
>
> Both DOIs and the SWHID are in `CITATION.cff` under `identifiers:`, recorded
> automatically at release by `.github/workflows/release-identifiers.yml`. Take
> the one described as *"Version DOI"*.

```
https://doi.org/10.5281/zenodo.23002074
```

<!-- field: date -->
### Choose completion date (text input, required)

```
2026-09-27
```

<!-- field: validationStatus -->
### Choose validation status (dropdown, required)


This dropdown maps to the CiTO intention in step 06: Validated → `confirms`, PartiallySupported → `qualifies`, Contradicted → `disputes`.

- [ ] contradicted
- [ ] inconclusive
- [ ] not tested
- [x] partially supported
- [ ] validated

<!-- field: confidenceLevel -->
### Choose confidence level (dropdown, required)

_Vocabulary not yet captured._

```
moderate
```

- [ ] high - Strong evidence, mostly agrees with original
- [ ] low - Limited evidence, significant disagreement
- [x] moderate - Adequate evidence, partial agreement
- [ ] very high - Extensive evidence, high agreement with original
- [ ] very low - Minimal evidence, major disagreement

<!-- field: conclusion -->
### Describe the overall conclusion about the original claim (textarea, required)

Substantive interpretation. Headline comparison: replication's number vs the paper's number, sign + significance.

```
Consistent with the claim, within its scope. Inside the paper's intermediate-rainfall band (99% of cells), the share of each cell that burned in 2024 falls steadily with pre-fire biomass, and it does so within each rainfall tercile, not only across them, as a fire–vegetation feedback predicts. Biomass itself is strongly skewed with a secondary high-biomass mode, compatible with alternative states. This is an association in one region and one year: it supports the regional signature of the claim, not its global extent or its causal direction.
```

<!-- field: evidence -->
### Describe the evidence that supports your conclusion (textarea, required)

Numerical results, test statistics, model coefficients. Read directly from `results/`.

```
10,344 cells (HEALPix depth 11, WGS84). Mean burned share by biomass class: <10 Mg/ha 32.1%, 10–25 Mg/ha 27.3%, 25–50 Mg/ha 19.7%, 50–100 Mg/ha 13.6%, 100–150 Mg/ha 5.6%, ≥150 Mg/ha 1.4%. Spearman biomass vs burned share: overall -0.383; within rainfall terciles drier -0.229, middle -0.235, wetter -0.39 (tercile bounds 1825 and 1944 mm). In the 1000–2500 mm band: 10,262 cells (99.2%), Spearman -0.378. Rainfall vs biomass 0.471. Biomass bimodality coefficient 0.723 (skewness 1.76).
```

<!-- field: limitations -->
### Describe what limits the conclusions of the study (textarea, optional)

Honest caveats. If the result is partial or contradicted, say so plainly. Don't overclaim.

```
One region and one fire year (2024); an association that cannot separate 'fire keeps biomass low' from 'low biomass burns more'. Burned share in one year stands in for fire frequency, and biomass for tree cover. Seasonality and soils, part of the original claim's conditions, are not tested. The bimodality coefficient is inflated by skew and is indicative only. Rainfall is a 1981–2010 climatology.
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 05.
