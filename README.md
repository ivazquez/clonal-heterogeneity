# Clonal heterogeneity influences the fate of new adaptive mutations

This repository contains supporting material for the manuscript:

> "Clonal heterogeneity influences the fate of new adaptive mutations"
>
> Ignacio Vázquez-García, Francisco Salinas, Jing Li, Andrej Fischer, Benjamin Barré, Johan Hallin, Anders Bergström, Elisa Alonso-Pérez, Jonas Warringer, Ville Mustonen, Gianni Liti
>
> [Cell Reports 21, 732-744 (2017), doi: https://doi.org/10.1016/j.celrep.2017.09.046](https://doi.org/10.1016/j.celrep.2017.09.046)

To clone this repository, run the following command in a local directory:

    $ git clone --recursive https://github.com/ivazquez/clonal-heterogeneity.git

The `--recursive` flag is required in order to download the nested git submodule from an external repository.

<p align="center">
  <img src="https://github.com/ivazquez/clonal-heterogeneity/blob/master/manuscript/main/figures/graphical-abstract/graphical_abstract_publication.png?raw=true" width="60%" height="60%" alt="Graphical abstract"/>
</p>

## Source code

The source code contains iPython notebooks to reproduce the manuscript figures, which make use of numpy, scipy, the matplotlib plotting environment
and others. These are found in the `src/` directory. The repository also includes the cloneHD submodule, which is in C++ and requires g++ with the GSL library.

To install all Python dependencies inside a virtual environment and build the cloneHD executables into the `build/` directory, run:

    $ cd clonal-heterogeneity
    $ make

You can then browse and run the notebooks locally to reproduce all figures with:

    $ jupyter notebook

Alternatively, you can run the notebooks online using [Binder](http://mybinder.org/repo/ivazquez/clonal-heterogeneity).

| Figures | Notebook |
| ------- | -------- |
| Figure 1 | [Schematic of study design](src/figure1.ipynb) |
| Figures 2, S2 | [Driver-passenger dynamics](src/figure2.ipynb) |
| Figures 3, S3, S4, S9 | [Reconstruction of subclonal heterogeneity](src/figure3.ipynb) |
| Figures 4, S5 | [Pervasive selection for adaptive mutations and genome instability](src/figure4.ipynb) |
| Figure 5 | [Elevated rates of loss of heterozygosity](src/figure5.ipynb) |
| Figures 6, S10, S11, S12 | [Ensemble-averaged fitness effects of genetic background and de novo mutations](src/figure6.ipynb)|
| Figures S6, S7, S8 | [Engineered genetic constructs](src/supp_figure_pheno_constructs.ipynb)|

## Sequence data
Sequencing reads are available in BAM or CRAM format from the European Nucleotide Archive and the NCBI BioProject. Sequence data for the parental strains and the ancestral individuals were previously submitted to the SRA/ENA databases under study accession no. [ERP000780](http://www.ebi.ac.uk/ena/data/view/ERP000780) and the NCBI BioProject under accession no. [PRJEB2608](http://www.ncbi.nlm.nih.gov/bioproject/?term=PRJEB2608). Sequence data for the time-resolved populations and the evolved individuals have been submitted to the SRA/ENA databases under study accession no. [ERP003953](http://www.ebi.ac.uk/ena/data/view/ERP003953) and the NCBI BioProject under accession no. [PRJEB4645](http://www.ncbi.nlm.nih.gov/bioproject/?term=PRJEB4645). To download the files programmatically from the FTP server (156GB):

```sh
wget -i <(awk -F, '{gsub("#","%23",$NF); print $NF}' data/seq/sample_ids_unmerged.csv)
```

Sequences must be aligned to the *S. cerevisiae* reference genome [R64-1-1](http://downloads.yeastgenome.org/sequence/S288C_reference/genome_releases/S288C_reference_genome_R64-1-1_20110203.tgz).

Variant calls are available in VCF format with accession no. [PRJEB13491](http://www.ebi.ac.uk/ena/data/view/PRJEB13491) and can be browsed on the [European Variation Archive](http://www.ebi.ac.uk/eva/?eva-study=PRJEB13491). Each VCF file corresponds to one [sample](data/seq/sample\_ids\_merged\_dup.csv) and contains either pre-existing variants (`*.background.vcf.gz`) or *de novo* variants (`*.de_novo.vcf.gz`). They can be downloaded programmatically from the FTP (713MB):

```sh
wget -i <(awk -F, '{gsub(";","\n",$NF); print $NF;}' data/seq/sample_ids_merged_dup.csv)
```

Alternatively, variants can also be found in tab-separated format or serialized in Pickle format for Python in the `data/seq/` directory, annotated with Ensembl [Variant Effect Predictor](http://www.ensembl.org/info/docs/tools/vep/index.html).

With the sequence data we carry out subclonal decomposition using a probabilistic inference method named cloneHD, as shown in [Figure 3](src/figure3.ipynb) of the manuscript. The source code contains a minimal example to carry out subclonal decomposition in a simulated dataset. To test this method with simulated data:

```sh
src/subclonality_simulated.sh
```

Also, to test this on a representative time series dataset for one of the populations (as shown in [Figure 2](src/figure2.ipynb)):

```sh
src/subclonality_experiment.sh
```

The full documentation for [filterHD](https://github.com/ivazquez/cloneHD/blob/master/docs/README-filterHD.md) and [cloneHD](https://github.com/ivazquez/cloneHD/blob/master/docs/README-cloneHD.md) can be found in the cloneHD repository.

## Phenotype data
This dataset comprises phenotype measurements of intra-population heterogeneity, of engineered genetic constructs, and of a recombinant library of pre-existing and *de novo* mutations created by genetic crossing. Raw imaging data is available upon request (~250GB). Phenotype measurements are analysed using [scan-o-matic](https://github.com/local-minimum/scanomatic) and are available in comma-separated format. They can be found in the `data/pheno/` directory.

* Temporal changes to the phenotype distribution are summarised in this [dataset](data/pheno/populations/pheno_populations.csv) and are analysed in this [notebook](src/figure3.ipynb). The results are shown in [Figure 3](manuscript/main/figures/figure3/figure3_final.png) and [S9](manuscript/supp/figures/supp_figure_pheno_evolution/supp_figure_pheno_evolution_final.png).
* Phenotype measurements of the genetic cross are summarised in this dataset ([spores](data/pheno/genetic-cross/pheno_genetic_cross_spores.csv) and [hybrids](data/pheno/genetic-cross/pheno_genetic_cross_hybrids.csv)) and are analysed in this [notebook](src/figure4.ipynb). The results are shown in [Figure 6](manuscript/main/figures/figure6/figure6_final.png) and [Figures S10](manuscript/supp/figures/supp_figure_pheno_cross/supp_figure_pheno_cross_extended_final.png) and [S11](manuscript/supp/figures/supp_figure_pheno_cross/supp_figure_pheno_cross_reduced_final.png).
* Phenotype measurements of the genetic constructs are summarised in this [dataset](data/pheno/genetic-constructs/pheno_genetic_constructs.csv) and are analysed in this [notebook](src/supp_figure_pheno_constructs.ipynb).

Each measurement is indexed by experimental run, plate, row and column. All datasets report the growth rate and the doubling time. For each observable, the dataset reports absolute values and normalised values extracted after spatial normalisation. `NaN` is used to indicate missing data.

## Fluctuation assay data
Locus-specific measurements of the LOH rate using a Luria-Delbruck fluctuation test. This dataset reports the raw colony counts measured in the fluctuation assay and the estimated LOH rates.  They can be found in the `data/fluctuation/` directory.

* The raw counts contain the [number of colony-forming units](data/fluctuation/fluctuation_assay_counts.csv) (CFU) in YPD medium and in 5-FOA+ dropout medium. This provides the average number of cells per culture, `N`, the average number of LOH events per culture, `m`.
* For every background and environment, the [mean LOH rate](data/fluctuation/fluctuation_assay_rates.csv) and 5\%/95\% confidence intervals are estimated using the probability generating function of the Luria-Delbruck distribution defined by Hamon et al. (2012).