# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 03 — Analysis: does burning track pre-fire biomass, within rainfall bands?
#
# Staver, Archibald & Levin (2011) argue that fire feedbacks maintain savanna and forest as alternative states:
# where tree cover (biomass) is low, fire is frequent and keeps it low; where it is high, fire is rare.
# Here we test the regional signature of that feedback with independent ESA data: in the Beni, 2024, is the share
# of each cell that burned lower where pre-fire biomass was higher — **within each rainfall tercile**, so that
# the pattern is not only a rainfall effect?
#
# Descriptive association, one region and one fire year: it cannot show the feedback's direction.

# %%
import json
from pathlib import Path

import numpy as np
import pandas as pd

df = pd.read_parquet("../data/clean/beni_cells.parquet")
RES = Path("../results"); RES.mkdir(exist_ok=True)
m = df[["agb_2023_mg_ha", "burned_share_2024", "rain_mm"]].notna().all(axis=1)
d = df[m].copy()
edges = [0, 10, 25, 50, 100, 150, 400]
labels = ["<10", "10–25", "25–50", "50–100", "100–150", "≥150"]
d["agb_class"] = pd.cut(d.agb_2023_mg_ha, edges, right=False, labels=labels)
rt = np.percentile(d.rain_mm, [33.3, 66.7])
d["rain_tercile"] = pd.cut(d.rain_mm, [-np.inf, rt[0], rt[1], np.inf], right=False, labels=["drier", "middle", "wetter"])
print(len(d), "cells")

# %%
rank = lambda s: s.rank().to_numpy()
spear = lambda a, b: float(np.corrcoef(rank(d[a]), rank(d[b]))[0, 1])
table = (d.groupby(["rain_tercile", "agb_class"], observed=False)
         .agg(n_cells=("burned_share_2024", "size"), mean_burned_pct=("burned_share_2024", lambda x: 100 * x.mean()))
         .reset_index())
table.to_csv(RES / "summary.csv", index=False)
within = {}
for t, g in d.groupby("rain_tercile", observed=True):
    within[str(t)] = round(float(np.corrcoef(g.agb_2023_mg_ha.rank(), g.burned_share_2024.rank())[0, 1]), 3)
out = {"n_cells": int(len(d)),
       "spearman_agb_vs_burned": round(spear("agb_2023_mg_ha", "burned_share_2024"), 3),
       "spearman_rain_vs_burned": round(spear("rain_mm", "burned_share_2024"), 3),
       "spearman_rain_vs_agb": round(spear("rain_mm", "agb_2023_mg_ha"), 3),
       "spearman_agb_vs_burned_within_rain_tercile": within,
       "mean_burned_pct_by_agb_class": {k: round(100 * float(v), 1) for k, v in d.groupby("agb_class", observed=False).burned_share_2024.mean().items()},
       "rain_tercile_bounds_mm": [round(float(x)) for x in rt]}
# %% [markdown]
# ## Inside the paper's intermediate-rainfall band only (1000–2500 mm)
# Staver et al. (2011) locate fire-maintained alternative states at 1000–2500 mm annual rainfall with mild
# seasonality. Seasonality is not tested here (a limitation). We repeat the test on cells inside the rainfall band.

# %%
band = d[(d.rain_mm >= 1000) & (d.rain_mm <= 2500)]
out["in_band_1000_2500mm"] = {
    "n_cells": int(len(band)), "share_of_cells_pct": round(100 * len(band) / len(d), 1),
    "spearman_agb_vs_burned": round(float(np.corrcoef(band.agb_2023_mg_ha.rank(), band.burned_share_2024.rank())[0, 1]), 3),
    "mean_burned_pct_by_agb_class": {k: round(100 * float(v), 1) for k, v in band.groupby("agb_class", observed=False).burned_share_2024.mean().items()}}
out["spearman_note"] = "Spearman with average ranks for ties (many cells have zero burned share)."
(RES / "headline.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(json.dumps(out, indent=1, ensure_ascii=False))
table
