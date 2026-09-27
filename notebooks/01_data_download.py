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
# # 01 — Data download
#
# Region: the Beni lowlands, Bolivia (bbox lon −67.5 to −64.5, lat −15.5 to −12.5), a savanna–forest mosaic.
#
# | Dataset | Role | Access |
# |---|---|---|
# | ESA CCI Biomass v7.0, 2023, tile S10W070 (100 m) | pre-fire above-ground biomass (AGB) | downloaded here |
# | ESA Fire_cci SYN burned area pixel v1.1, 2024, monthly JD + CL (300 m) | burned area | downloaded here |
# | CHELSA v2.1 bio12, 1981–2010 | mean annual precipitation | read by window in `02` (global file, ~GB) |
#
# No credentials are needed. Every file is recorded in `data/raw/sources.json` with its DOI, licence,
# access date and SHA-256.

# %%
import hashlib
import json
from datetime import date
from pathlib import Path

import requests

RAW_DIR = Path("../data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

CCI = "https://dap.ceda.ac.uk/neodc/esacci/biomass/data/agb/maps/v7.0/geotiff/2023/S10W070_ESACCI-BIOMASS-L4-AGB-MERGED-100m-2023-fv7.0.tif"
FIRE = ("https://dap.ceda.ac.uk/neodc/esacci/fire/data/burned_area/Sentinel3_SYN/pixel/v1.1/uncompressed/"
        "2024/{m:02d}/2024{m:02d}01-ESACCI-L3S_FIRE-BA-SYN-AREA_2-fv1.1-{v}.tif")
CHELSA = "https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/1981-2010/bio/CHELSA_bio12_1981-2010_V.2.1.tif"

files = [("cci_biomass", CCI, "S10W070_AGB_2023_v7.tif")]
files += [("fire_cci", FIRE.format(m=m, v=v), f"fire_2024{m:02d}_{v}.tif") for m in range(1, 13) for v in ("JD", "CL")]


def fetch(url: str, dest: Path) -> str:
    if not dest.exists():
        with requests.get(url, stream=True, timeout=600) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
    h = hashlib.sha256()
    with open(dest, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


records = []
for kind, url, name in files:
    sha = fetch(url, RAW_DIR / name)
    records.append({"file": name, "url": url, "sha256": sha, "dataset": kind})
    print(name, sha[:12])

# %%
SOURCES = {
    "accessed_on": date.today().isoformat(),
    "datasets": {
        "cci_biomass": {"name": "ESA Biomass CCI v7.0 above-ground biomass, 2023", "doi": "10.5285/6429d1aafe1e43b9b414e4a5a7f8b903",
                        "license": "ESA CCI data policy: free use, acknowledge ESA CCI and cite the DOI"},
        "fire_cci": {"name": "ESA Fire_cci SYN burned area pixel product v1.1, 2024", "doi": "10.5285/d441079fc77f49fabeb41330612b252f",
                     "license": "ESA CCI data policy: free use, acknowledge ESA CCI and cite the DOI"},
        "chelsa_bio12": {"name": "CHELSA v2.1 bio12 (annual precipitation), 1981–2010", "doi": "10.16904/envidat.228",
                         "license": "CC0-1.0", "url": CHELSA, "access": "window read in 02_data_clean (not stored)"},
    },
    "files": records,
}
(RAW_DIR / "sources.json").write_text(json.dumps(SOURCES, indent=1))
print(len(records), "files recorded")
