#!/usr/bin/bash
genome=$1
# create tmp folder where to save output
tmp_dir=$(mktemp -d -t glimmer3XXXXXXXXXX --tmpdir=/home/apfennig3/Team1-GenePrediction/)
echo $tmp_dir
scripts=./glimmer3.02/scripts

# workflow from http://ccb.jhu.edu/software/glimmer/glim302notes.pdf
$scripts/g3-iterated.csh $genome $tmp_dir/run1
