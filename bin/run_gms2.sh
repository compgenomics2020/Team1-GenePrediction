#!/usr/bin/bash
genome=$1
file_name=$(echo $genome | sed -e 's|.*\/||g' -e 's/.fasta//') 
# create tmp folder where to save output 
#tmp_dir=$(mktemp -d -t gms2XXXXXXXXXX --tmpdir=/home/projects/group-a/Team1-GenePrediction/)
#echo $tmp_dir
echo $file_name
if [ ! -d /home/projects/group-a/Team1-GenePrediction/results/gms2_results/ ]
then
    mkdir -p /home/projects/group-a/Team1-GenePrediction/results/gms2_results/
fi
/home/projects/group-a/bin/gms2.pl --seq $genome --genome-type bacteria --output /home/projects/group-a/Team1-GenePrediction/gms2_results/${file_name}.gff --species E.coli --format gff --fnn /home/projects/group-a/Team1-GenePrediction/gms2_results/${file_name}.fasta
