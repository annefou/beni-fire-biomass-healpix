# 04 — FORRT Replication Study

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify code first:** read the actual reproduction script in `notebooks/03_analysis.py` before writing the methodology field. See `docs/verify-before-drafting.md`.

## Field-by-field draft

<!-- field: study -->
### Short URI suffix for study ID (text input, required)

Slug. Use kebab-case.

```
beni-fire-biomass-healpix-2024
```

<!-- field: label -->
### Label/name of replication study (text input, required)

Human-readable title.

```
Fire versus pre-fire biomass within rainfall bands, Beni lowlands 2024, on WGS84 HEALPix
```

<!-- field: type -->
### Choose the study type (dropdown, required)

- [x] Replication Study - replication with different methodology or conditions
- [ ] Reproduction/Replication Study - study that is both, reproduction and replication
- [ ] Reproduction Study - direct reproduction: same methodology, same tools

<!-- field: claim -->
### Choose FORRT claim (search/select, required)

URI of the Claim published in step 03. Pull from `nanopubs/PUBLISHED.md`.

```
<URI of step 03, from nanopubs/PUBLISHED.md>
```

<!-- field: scope -->
### Describe what part of the claim is reproduced/replicated. (textarea, required)

The **scope** of the claim being tested. Which aspect, what's in/out of scope. NOT methodology. NOT results. See `docs/pico-study-outcome-levels.md`.

```
The regional signature of the fire–vegetation feedback that Staver et al. (2011) invoke for intermediate rainfall: whether, inside that rainfall band, burning is concentrated where woody biomass is low, independently of rainfall. In scope: one savanna–forest mosaic (Beni lowlands, Bolivia), one fire year (2024), pre-fire biomass instead of tree cover. Out of scope: the global extent of bimodality, soils, seasonality, and the direction of causality.
```

<!-- field: methodology -->
### Describe how the claim is reproduced/replicated. (textarea, required)

The **method** in plain prose. Read `notebooks/03_analysis.py` and any config files first. NOT exact numerical results.

```
ESA Biomass CCI v7.0 above-ground biomass (2023), ESA Fire_cci SYN v1.1 burned area (monthly, 2024) and CHELSA v2.1 annual precipitation are binned onto the same HEALPix grid on the WGS84 ellipsoid (nested, depth 11, cells of about 3.2 km) with healpix-connector 0.1.0. A 300 m fire pixel counts as burned if any 2024 month records a day of burn; never-observed and non-burnable pixels are excluded. Per cell: burned share, mean biomass (cells over 90% covered) and rainfall. Cells are grouped into six biomass classes within rainfall terciles; Spearman rank correlations (average ranks for ties) are computed overall, within each tercile, and for cells inside 1000–2500 mm. Supplementary: Sarle's bimodality coefficient of biomass.
```

<!-- field: deviation -->
### Describe any deviations from original methodology. (textarea, optional)

What's different from the original method. Verify against the actual code, don't guess.

```
Different data (ESA CCI products, not MODIS tree cover), a single region and year instead of global data, above-ground biomass as the woody-cover variable, and burned share in one year instead of fire frequency. Seasonality and soils are not modelled; rainfall is controlled by terciles, not by a model.
```

<!-- field: keyword -->
### Search keywords (Wikidata) (search/select, optional)

Provide labels (not QIDs) — the Wikidata search picks up labels.

- Label 1: fire ecology
- Label 2: savanna
- Label 3: alternative stable state
- Label 4: HEALPix
- Label 5: remote sensing

<!-- field: discipline -->
### Search discipline (Wikidata) (search/select, optional)

Provide labels.

- Discipline label: ecology

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 04.
