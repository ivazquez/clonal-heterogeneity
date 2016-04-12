#!/bin/bash

# RUN filterHD & cloneHD FOR A SIMULATED EXAMPLE DATA SET

# set the number of threads
export OMP_NUM_THREADS=4;

# change this to your population-dynamics directory, or remove if
# you put filterHD and cloneHD into your system-wide path:
CWD=$(git rev-parse --show-toplevel)
BUILD_DIR=${CWD}/build

# input and output directories
data=${CWD}/data/seq/subclonality/simulation
results=${CWD}/data/seq/subclonality/simulation

bulkSNV="${data}/bulk.snv.txt"
mixtureSNV="${data}/mixture.snv.txt"


### filterHD ###
echo "*** filterHD ***"
echo    

cmd="${BUILD_DIR}/filterHD --data $bulkSNV --mode 1 --pre ${results}/bulk.snv --rnd 1e-8 --jump 0 --dist 1"
echo $cmd
$cmd

cmd="${BUILD_DIR}/filterHD --data $mixtureSNV --mode 1 --pre ${results}/mixture.snv --rnd 1e-8 --jumps 1"
echo $cmd
$cmd
