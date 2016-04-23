# Background-dependent selection of genetic variation in heterogeneous populations

This repository contains supporting material for the manuscript in preparation:

> "Background-dependent selection of genetic variation in heterogeneous populations"

> Ignacio Vázquez-García, Francisco Salinas, Jing Li, Andrej Fischer, Benjamin Barré, Johan Hallin, Anders Bergström, Elisa Alonso-Pérez, Jonas Warringer, Ville Mustonen, Gianni Liti

To clone this repository, run the following command in a local directory:

    $ git clone --recursive https://github.com/ivazquez/population-dynamics.git

The `--recursive` flag is required in order to download the nested git submodule from an external repository.

## Source code

The source code contains iPython notebooks to reproduce the manuscript figures, which make use of numpy, scipy, the matplotlib plotting environment
and others. These are found in the `src/` directory. The repository also includes the cloneHD submodule, which is in C++ and requires g++ with the GSL library.

To install all Python dependencies inside a virtual environment and build the cloneHD executables into the `build/` directory, run:

    $ make

You can then browse and run the notebooks locally to reproduce all figures with:

	$ jupyter notebook

## Sequence data
Sequencing reads are available in BAM or CRAM format from the European Nucleotide Archive and the NCBI BioProject. Sequence data for the parental strains and the ancestral individuals were previously submitted to the SRA/ENA databases under study accession no. [ERP000780](http://www.ebi.ac.uk/ena/data/view/ERP000780) and the NCBI BioProject under accession no. [PRJEB2608](http://www.ncbi.nlm.nih.gov/bioproject/?term=PRJEB2608). Sequence data for the time-resolved populations and the evolved individuals have been submitted to the SRA/ENA databases under study accession no. [ERP003953](http://www.ebi.ac.uk/ena/data/view/ERP003953) and the NCBI BioProject under accession no. [PRJEB4645](http://www.ncbi.nlm.nih.gov/bioproject/?term=PRJEB4645). To download the files programmatically from the FTP server (156GB):

	$ wget -i <(awk -F, '{sub("#","%23",$NF); print $NF}' data/seq/sample_ids_unmerged.csv)

Sequences must be aligned to the *S. cerevisiae* reference genome [R64-1-1](http://downloads.yeastgenome.org/sequence/S288C_reference/genome_releases/S288C_reference_genome_R64-1-1_20110203.tgz).

Variant calls are available in VCF format with accession no. [PRJEB13491](http://www.ebi.ac.uk/eva/?eva-study=PRJEB13491). They will also become available for browsing on the [European Variation Archive](http://www.ebi.ac.uk/eva/?eva-study=PRJEB13491) upon publication. Each VCF file corresponds to one [sample](data/seq/sample\_ids\_merged\_dup.csv) and contains either pre-existing variants (`*.background.vcf.gz`) or *de novo* variants (`*.de_novo.vcf.gz`). They can be downloaded programmatically from the FTP (713MB):

	$ wget -i <(awk -F, '{print $NF;}' data/seq/sample_ids_merged_dup.csv)

Alternatively, variants can also be found in tab-separated format or serialized in Pickle format for Python in the `data/seq/` directory, annotated with Ensembl [Variant Effect Predictor](http://www.ensembl.org/info/docs/tools/vep/index.html).

With the sequence data we carry out subclonal decomposition using a probabilistic inference method named cloneHD, as shown in [Figure 2](src/figure2.ipynb) of the manuscript. The source code contains a minimal example to carry out subclonal decomposition in a simulated dataset. To test this method with simulated data:

    $ src/run_filterHD.sh
	$ src/run_cloneHD.sh

The full documentation for [filterHD](cloneHD/docs/README-filterHD.md) and [cloneHD](cloneHD/docs/README-cloneHD.md) can be found in the cloneHD repository.

## Phenotype data
Raw imaging data is available upon request (~250GB). Phenotype measurements are analysed using [scan-o-matic](https://github.com/local-minimum/scanomatic) and are available in tab-separated format or serialized in Pickle format for Python. They can be found in the `data/pheno/` directory. 'NA' is used to indicate missing data or NaN.

Temporal changes to the phenotype distribution are analysed in this [notebook](src/figure2.ipynb). The results are shown in [Figure 2](manuscript/main/figures/figure2/figure2_submission.png) and [Figure S9](manuscript/supp/figures/supp_figure_pheno_evolution/supp_figure_pheno_evolution_submission.png). Phenotype measurements of the genetic cross are analysed in this [notebook](src/figure4.ipynb). The results are shown in [Figure 4](manuscript/main/figures/figure4/figure4_submission.png) and [Figures S12](manuscript/supp/figures/supp_figure_pheno_cross/supp_figure_pheno_cross_extended_submission.png) and [S13](manuscript/supp/figures/supp_figure_pheno_cross/supp_figure_pheno_cross_reduced_submission.png). Phenotype measurements of the genetic constructs are analysed in this [notebook](src/supp_figure_pheno_constructs.ipynb).