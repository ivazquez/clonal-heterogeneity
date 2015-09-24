# Transient dynamics of selection and adaptation in heterogeneous populations

This repository contains materials related to the manuscript in preparation:
Ignacio Vázquez-García, Francisco Salinas, Jing Li, Andrej Fischer, Benjamin Barré, Johan Hallin, Anders Bergström, Elisa Alonso-Pérez, Jonas Warringer, Ville Mustonen, Gianni Liti


## Source code

The source code contains a minimal example to carry out subclonal decomposition in a simulated dataset.

    `$ filterHD --data $bulkSNV --mode 1 --pre ${results}/bulk.snv --rnd 1e-8 --jump 0 --dist 1

    `$ filterHD --data $mixtureSNV --mode 1 --pre ${results}/mixture.snv --rnd 1e-8 --jumps 1

    `$ cloneHD --cna $mixtureCNA --snv $mixtureSNV --pre $pre --trials 5 --nmax 3 --force --max-tcn 2 --cna-jump 0 --snv-jumps $mixtureSNVjumps --min-jump 0.01 --restarts 10 --mass-gauging 1 --bulk-mean $bulkProfile --cna-pen-norm 0.9

## Sequence data

## Phenotype data
