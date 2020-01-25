#!/usr/bin/bash
genome=$1
# create tmp folder where to save output 
tmp_dir=$(mktemp -d -t gms2XXXXXXXXXX --tmpdir=/home/apfennig3/Team1-GenePrediction/)
echo $tmp_dir
./gms2.pl --seq $genome --genome-type bacteria --output $tmp_dir
