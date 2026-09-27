# 06 — CiTO Citation

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Description:** *"Declare citations between papers or other works, using Citation Typing Ontology"*

## Field-by-field draft

<!-- field: work -->
### Identifier for the citing creative work (text input, required)

URI of the Outcome published in step 05. Pull from `nanopubs/PUBLISHED.md`.

```
<URI of step 05, from nanopubs/PUBLISHED.md>
```

### List citations (repeatable group, required ≥1)

#### Citation 1 — back to the original paper

##### Citation Type (dropdown)

Choose based on the Outcome's validation status:

- Validated → `confirms`
- PartiallySupported → `qualifies`
- Contradicted → `disputes`

For question-rooted chains where there is no original paper to confirm/dispute, use `usesMethodIn` or `citesAsAuthority` for the methodology paper(s).

> **Note:** `replicates` is NOT in the Science Live dropdown (despite existing in upstream CiTO). When citing a notebook/tutorial that was directly reused, use **`credits`** instead.

```
qualifies
```

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.1126/science.1210465
```

#### Additional citations (optional)

If the Outcome cites methods papers, related replications, or upstream tools, add them here.

- Type: usesDataFrom → URL: https://doi.org/10.5285/6429d1aafe1e43b9b414e4a5a7f8b903
- Type: usesDataFrom → URL: https://doi.org/10.5285/d441079fc77f49fabeb41330612b252f
- Type: usesMethodIn → URL: https://doi.org/10.5281/zenodo.22904851 (healpix-connector)

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 06.

This completes the six-step FORRT chain. Optional next layers:

- **Research Software** (`drafts/07_research_software.md`) — if the repo *produces* a reusable software artefact.
- **Research Synthesis** (`drafts/08_synthesis.md`) — if this chain is one of several testing facets of a shared property.
