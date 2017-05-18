#!/bin/bash

# RUN filterHD & cloneHD FOR A REAL EXAMPLE DATA SET (Fig. 1B)

# set the number of threads
export OMP_NUM_THREADS=4;

# change this to your genetic-variation directory, or remove if
# you put filterHD and cloneHD into your system-wide path:
CWD=$(git rev-parse --show-toplevel)
BUILD_DIR=${CWD}/build

# input and output directories
data=${CWD}/data/seq/subclonality/experiment/WAxNA_F12_1_RM_1
results=${CWD}/data/seq/subclonality/experiment/WAxNA_F12_1_RM_1

bulkSNV="${data}/snv_T0.txt"
mixtureSNV="${data}/snv_T2_T32.txt"
mixtureSNVjumps="${results}/mixture.snv.jumps.txt"
bulkProfile="${results}/bulk.snv.posterior-1.txt"
pre="${results}/mixture"
clones="${data}/clones.txt"


### filterHD ###
echo "*** filterHD ***"
echo

cmd="${BUILD_DIR}/filterHD --data $bulkSNV --mode 1 --pre ${results}/bulk.snv --rnd 1e-8 --jump 0 --dist 1"
echo $cmd
$cmd

cmd="${BUILD_DIR}/filterHD --data $mixtureSNV --mode 1 --pre ${results}/mixture.snv --rnd 1e-8 --jumpi 1e-08 --sigmai 1.0e-4 --jumps 1"
echo $cmd
$cmd


### cloneHD ###
echo "*** cloneHD ***"
echo "True mass and cell fractions:" `cat $clones` 
   
cmd="${BUILD_DIR}/cloneHD --snv $mixtureSNV --pre $pre --trials 5 --nmax 3 --force --snv-rnd 1.0e-4 --snv-jump 0.001 --bulk-mean $bulkProfile"
echo $cmd
$cmd
echo
cat ${pre}.summary.txt
