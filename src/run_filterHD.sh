#!/bin/bash

# RUN filterHD & cloneHD FOR A SIMULATED EXAMPLE DATA SET
if [ $# -ne 2 ];
then
    echo "Usage: $0 [indir] [outdir]"
    exit
fi

# set the number of threads
export OMP_NUM_THREADS=4;

# change this to your population-dynamics directory, or remove if
# you put filterHD and cloneHD into your system-wide path:
bin="/Users/ivg/projects/population-dynamics/bin/"

# input data
data=$1
results=$2

bulkSNV="${data}/bulk.snv.txt"
mixtureSNV="${data}/mixture.snv.txt"


### filterHD ###
echo "*** filterHD ***"
echo    

cmd="$bin/filterHD --data $bulkSNV --mode 1 --pre ${results}/bulk.snv --rnd 1e-8 --jump 0 --dist 1"
echo $cmd
$cmd
echo

cmd="$bin/filterHD --data $mixtureSNV --mode 1 --pre ${results}/mixture.snv --rnd 1e-8 --jumps 1"
echo $cmd
$cmd
echo
