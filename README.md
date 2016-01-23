# Background-dependent selection of genetic variation in heterogeneous populations

This repository contains supporting material for the manuscript in preparation:
> "Background-dependent selection of genetic variation in heterogeneous populations"
Ignacio Vázquez-García, Francisco Salinas, Jing Li, Andrej Fischer, Benjamin Barré, Johan Hallin, Anders Bergström, Elisa Alonso-Pérez, Jonas Warringer, Ville Mustonen, Gianni Liti

To clone this repository, run the following command in a local directory:

    `$ git clone https://github.com/ivazquez/population-dynamics.git

## Source code

The source code contains notebooks to reproduce the manuscript figures.

We carry out subclonal decomposition using a probabilistic inference method named cloneHD, as shown in [Figure 3](https://github.com/ivazquez/population-dynamics/blob/master/src/figure3.ipynb) of the manuscript. The source code contains a minimal example to carry out subclonal decomposition in a simulated dataset. Documentation for [filterHD](https://github.com/andrej-fischer/cloneHD/blob/master/docs/README-filterHD.md) and [cloneHD](https://github.com/andrej-fischer/cloneHD/blob/master/docs/README-cloneHD.md). To test this method with simulated data:

    `$ filterHD --data $bulkSNV --mode 1 --pre ${results}/bulk.snv --rnd 1e-8 --jump 0 --dist 1

    `$ filterHD --data $mixtureSNV --mode 1 --pre ${results}/mixture.snv --rnd 1e-8 --jumps 1

    `$ cloneHD --cna $mixtureCNA --snv $mixtureSNV --pre $pre --trials 5 --nmax 3 --force --max-tcn 2 --cna-jump 0 --snv-jumps $mixtureSNVjumps --min-jump 0.01 --restarts 10 --mass-gauging 1 --bulk-mean $bulkProfile --cna-pen-norm 0.9

## Sequence data
Sequencing reads are available in BAM format from the European Nucleotide Archive and the NCBI (~1TB).

    `$ cloneHD --cna $mixtureCNA --snv $mixtureSNV --pre $pre --trials 5 --nmax 3 --force --max-tcn 2 --cna-jump 0 --snv-jumps $mixtureSNVjumps --min-jump 0.01 --restarts 10 --mass-gauging 1 --bulk-mean $bulkProfile --cna-pen-norm 0.9

Variant calls are available in VCF format.

## Phenotype data
Phenotype data are available under `data/pheno/`, in comma-separated format or in Pickle format for Python. 'NA' is used to indicate missing data or NaN.

Raw imaging data can be provided (~1TB).
