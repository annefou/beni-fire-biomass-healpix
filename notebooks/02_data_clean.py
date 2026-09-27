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
# # 02 — Put the three layers on one grid
#
# Every layer is binned onto the same **HEALPix grid on the WGS84 ellipsoid** (nested, depth 11, cells of
# about 3.2 km), with `healpix-connector` (GRID4EARTH). Fire_cci pixel codes (JD layer): day of year = burned;
# 0 = not burned; −1 = not observed; −2 = not burnable. These meanings are in the Fire_cci Product User Guide,
# not in the GeoTIFF itself — so the rule is declared here, in code.
#
# Output: `data/clean/beni_cells.parquet` — one row per cell: burned share 2024, AGB 2023, annual rainfall.

# %%
import json
from pathlib import Path

import healpix_connector
import numpy as np
import pandas as pd
from healpix_connector.binning import bin_to_cells
from healpix_connector.sources import chelsa
from healpix_connector.sources.geotiff import read_window
from healpix_connector.sources.gridded import sample_cells_from_grid

RAW = Path("../data/raw")
CLEAN = Path("../data/clean")
CLEAN.mkdir(parents=True, exist_ok=True)
BBOX = (-67.5, -15.5, -64.5, -12.5)
DEPTH = 11
print("healpix-connector", healpix_connector.__version__)

# %% [markdown]
# ## Burned area 2024 (Fire_cci)
# A 300 m pixel counts as burned if any month has a day of burn; it is excluded if never observed or not burnable.

# %%
burned = observed = unburnable = None
for m in range(1, 13):
    jd = read_window(str(RAW / f"fire_2024{m:02d}_JD.tif"), BBOX)
    j = jd.values
    if burned is None:
        burned = np.zeros(j.shape, bool); observed = np.zeros(j.shape, bool); unburnable = np.ones(j.shape, bool)
        lon, lat, res = jd.lon, jd.lat, jd.res_deg
    burned |= j > 0; observed |= j >= 0; unburnable &= j == -2
frac = np.where(observed & ~unburnable, burned.astype(float), np.nan)
fire = bin_to_cells(frac, lon, lat, DEPTH, res)
print(f"{fire.cell_ids.size} cells; burned share of observed burnable pixels: {100*np.nanmean(frac):.1f}%")

# %% [markdown]
# ## Pre-fire biomass 2023 (Biomass CCI) and rainfall (CHELSA)
# Biomass: area-weighted mean per cell, kept only where the tile covers more than 90% of the cell.

# %%
agb_w = read_window(str(RAW / "S10W070_AGB_2023_v7.tif"), BBOX)
st = bin_to_cells(agb_w.values, agb_w.lon, agb_w.lat, DEPTH, agb_w.res_deg)
cells = fire.cell_ids
j = np.searchsorted(st.cell_ids, cells); j[j >= st.cell_ids.size] = 0
ok = (st.cell_ids[j] == cells) & (st.coverage[j] > 0.9)
agb = np.full(cells.size, np.nan); agb[ok] = st.mean[j[ok]]

pr = read_window(chelsa.SOURCE["url_template"].format(n=12), BBOX)
cs = sample_cells_from_grid(pr.values, pr.lon, pr.lat, cells, DEPTH, pr.res_deg)

df = pd.DataFrame({"cell_id": cells.astype("uint64"), "burned_share_2024": fire.mean, "agb_2023_mg_ha": agb,
                   "rain_mm": cs.value})
df.attrs = {"grid": f"HEALPix nested, depth {DEPTH}, WGS84 ellipsoid", "healpix_connector": healpix_connector.__version__,
            "rain_support": str(cs.method)}
df.to_parquet(CLEAN / "beni_cells.parquet")
(CLEAN / "grid.json").write_text(json.dumps(df.attrs, indent=1))
df.describe()
