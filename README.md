# Background-dependent selection of genetic variation in heterogeneous populations

This repository contains supporting material for the manuscript in preparation:

> "Background-dependent selection of genetic variation in heterogeneous populations"

> Ignacio Vázquez-García, Francisco Salinas, Jing Li, Andrej Fischer, Benjamin Barré, Johan Hallin, Anders Bergström, Elisa Alonso-Pérez, Jonas Warringer, Ville Mustonen, Gianni Liti

To clone this repository, run the following command in a local directory:

    $ git clone https://github.com/ivazquez/population-dynamics.git

## Source code

The source code contains notebooks to reproduce the manuscript figures.

    $ pip install -r requirements.txt
	$ jupyter notebook

We carry out subclonal decomposition using a probabilistic inference method named cloneHD, as shown in [Figure 2](https://github.com/ivazquez/population-dynamics/blob/master/src/figure2.ipynb) of the manuscript. The source code contains a minimal example to carry out subclonal decomposition in a simulated dataset. Documentation for [filterHD](https://github.com/andrej-fischer/cloneHD/blob/master/docs/README-filterHD.md) and [cloneHD](https://github.com/andrej-fischer/cloneHD/blob/master/docs/README-cloneHD.md). To test this method with simulated data:

    $ filterHD --data $bulkSNV --mode 1 --pre ${results}/bulk.snv --rnd 1e-8 --jump 0 --dist 1

    $ filterHD --data $mixtureSNV --mode 1 --pre ${results}/mixture.snv --rnd 1e-8 --jumps 1

    $ cloneHD --cna $mixtureCNA --snv $mixtureSNV --pre $pre --trials 5 --nmax 3 --force --max-tcn 2 --cna-jump 0 --snv-jumps $mixtureSNVjumps --min-jump 0.01 --restarts 10 --mass-gauging 1 --bulk-mean $bulkProfile --cna-pen-norm 0.9

## Sequence data
Sequencing reads are available in BAM format from the European Nucleotide Archive and the NCBI. The sequence data for the parental strains and the ancestral individuals were previously submitted to the NCBI BioProject under accession no. [PRJEB2299](http://www.ncbi.nlm.nih.gov/bioproject/?term=PRJEB2299) and the SRA/ENA databases under study accession no. [ERP000361](http://www.ebi.ac.uk/ena/data/view/ERP000361), as part of the Saccharomyces Genome Resequencing Project. The sequence data for the time-resolved populations and the evolved individuals, have been submitted to NCBI BioProject under accession no. [PRJEB2608](http://www.ncbi.nlm.nih.gov/bioproject/?term=PRJEB2608), and the SRA/ENA databases under study accession no. [ERP000780](http://www.ebi.ac.uk/ena/data/view/ERP000780).

Variant calls are available in VCF format in the `data/seq/` directory. annotated with Ensembl [Variant Effect Predictor](http://www.ensembl.org/info/docs/tools/vep/index.html). 

## Phenotype data
Raw imaging data is available upon request (~1TB). Phenotype measurements are analysed using [scan-o-matic](https://github.com/local-minimum/scanomatic) and are available under `data/pheno/`, in comma-separated format or in Pickle format for Python. 'NA' is used to indicate missing data or NaN.

Temporal changes to the phenotype distribution are analysed in this [notebook](https://github.com/ivazquez/population-dynamics/blob/master/src/figure2.ipynb). The results are shown in [Figure 2](https://github.com/ivazquez/population-dynamics/tree/master/manuscript/main/figures/figure2/figure2_submission.png) and [Figure S9](https://github.com/ivazquez/population-dynamics/tree/master/manuscript/supp/figures/figureSX_pheno_evolution/figureSX_pheno_evolution_submission.png). Phenotype measurements of the genetic cross are analysed in this [notebook](https://github.com/ivazquez/population-dynamics/blob/master/src/figure4.ipynb). The results are shown in [Figure 4](https://github.com/ivazquez/population-dynamics/tree/master/manuscript/main/figures/figure4/figure4_submission.png) and [Figures S12](https://github.com/ivazquez/population-dynamics/tree/master/manuscript/supp/figures/figureSX_pheno_cross/figureSX_pheno_cross_extended_submission.png) and [S13](https://github.com/ivazquez/population-dynamics/tree/master/manuscript/supp/figures/figureSX_pheno_cross/figureSX_pheno_cross_reduced_submission.png). Phenotype measurements of the genetic constructs are analysed in this [notebook](https://github.com/ivazquez/population-dynamics/blob/master/src/figureSX_pheno_constructs.ipynb).