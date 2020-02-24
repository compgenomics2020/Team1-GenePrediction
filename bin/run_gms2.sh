#!/usr/bin/bash
genome=$1
file_name=$(echo $genome | sed -e 's/\/home\/projects\/group-a\/Team1-GenomeAssembly\/assembled_output\///') 
# create tmp folder where to save output 
#tmp_dir=$(mktemp -d -t gms2XXXXXXXXXX --tmpdir=/home/projects/group-a/Team1-GenePrediction/)
#echo $tmp_dir
#echo $file_name
mkdir -p /home/projects/group-a/Team1-GenePrediction/gms2_results/
/home/projects/group-a/bin/gms2.pl --seq $genome --genome-type bacteria --output /home/projects/group-a/Team1-GenePrediction/gms2_results/output.gff --species E.coli --format gff --fnn /home/projects/group-a/Team1-GenePrediction/gms2_results/$file_name
