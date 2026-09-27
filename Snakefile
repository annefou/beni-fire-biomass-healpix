# Snakefile — the Beni fire × biomass × rainfall replication, end to end.
#   pixi run snakemake --cores 1        (or: pixi run run)

NOTEBOOKS = "notebooks"


rule all:
    input:
        "figures/main_result.png",
        "results/headline.json",


rule data_download:
    output:
        "data/raw/sources.json",
    log:
        "results/logs/01_data_download.log",
    shell:
        "cd notebooks && jupytext --to notebook --execute 01_data_download.py > ../{log} 2>&1"


rule data_clean:
    input:
        "data/raw/sources.json",
    output:
        "data/clean/beni_cells.parquet",
    log:
        "results/logs/02_data_clean.log",
    shell:
        "cd notebooks && jupytext --to notebook --execute 02_data_clean.py > ../{log} 2>&1"


rule analysis:
    input:
        "data/clean/beni_cells.parquet",
    output:
        "results/headline.json",
        "results/summary.csv",
    log:
        "results/logs/03_analysis.log",
    shell:
        "cd notebooks && jupytext --to notebook --execute 03_analysis.py > ../{log} 2>&1"


rule figures:
    input:
        "data/clean/beni_cells.parquet",
        "results/headline.json",
        "results/summary.csv",
    output:
        "figures/main_result.png",
    log:
        "results/logs/04_figures.log",
    shell:
        "cd notebooks && jupytext --to notebook --execute 04_figures.py > ../{log} 2>&1"
