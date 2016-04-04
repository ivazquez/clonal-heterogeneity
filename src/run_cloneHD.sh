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
mixtureCNA="${data}/mixture.cna.txt"
mixtureSNV="${data}/mixture.snv.txt"
mixtureSNVjumps="${results}/mixture.snv.jumps.txt"
bulkProfile="${results}/bulk.snv.posterior-1.txt"
pre="${results}/mixture"
clones="${data}/clones.txt"
 

echo "*** cloneHD ***"
echo "True mass and cell fractions:" `cat $clones` 
echo
   
cmd="$bin/cloneHD --cna $mixtureCNA --snv $mixtureSNV --pre $pre --trials 5 --nmax 3 --force --max-tcn 2 --cna-jump 0 --snv-jumps $mixtureSNVjumps --min-jump 0.01 --restarts 10 --mass-gauging 1 --bulk-mean $bulkProfile --cna-pen-norm 0.9" 
echo $cmd
$cmd
echo
cat ${pre}.summary.txt
echo
