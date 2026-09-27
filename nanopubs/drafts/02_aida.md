# 02 — AIDA Sentence

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Form heading:** *"AIDA Sentence — Make structured scientific claims following the AIDA model"*

## Field-by-field draft

<!-- field: aida -->
### AIDA sentence (text input, required)

Atomic, Independent, Declarative, Absolute. One empirical finding. Must end with a full stop.

> _If your draft AIDA contains "and" linking two distinct findings, split into two AIDA nanopubs._

```
In the Beni savanna–forest mosaic of Bolivia, the share of land that burned in 2024 decreased with pre-fire above-ground biomass within each rainfall tercile.
```

<!-- field: topic -->
### Select related topics/tags (search/select, optional)

Predefined topic vocabulary — list the labels you intend to pick from the dropdown.

```
fire ecology
savanna
alternative stable state
remote sensing
```

<!-- field: project -->
### Relates to this nanopublication (search/select, required)

URI of the nanopub the AIDA derives from.

- For paper-rooted chains: the Quote-with-comment URI (from step 01).
- For question-rooted chains: the PICO or PCC URI (from step 01).

Pull the URI from `nanopubs/PUBLISHED.md`.

```

```

<!-- field: dataset -->
### Supported by datasets (text input, optional)

DOIs/URLs of datasets that ground the AIDA claim.

- DOI 1: https://doi.org/10.5285/6429d1aafe1e43b9b414e4a5a7f8b903 (ESA Biomass CCI v7.0)
- DOI 2: https://doi.org/10.5285/d441079fc77f49fabeb41330612b252f (ESA Fire_cci SYN v1.1)
- DOI 3: https://doi.org/10.16904/envidat.228 (CHELSA v2.1)

<!-- field: publication -->
### Supported by other publications (text input, optional)

DOIs/URLs of publications that support the AIDA claim — e.g. peer-reviewed methods papers, or the original paper if not already cited via the Quote.

- _DOI 1: ___
- _DOI 2: ___

> **Known platform bug (2026-04-26):** if both *Supported by datasets* AND *Supported by other publications* are populated and publishing fails, fall back to publishing this AIDA via Nanodash. The URI namespace becomes `https://w3id.org/np/...` (still valid and citable).

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 02.
