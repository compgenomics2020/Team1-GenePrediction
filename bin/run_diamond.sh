#!/usr/bin/bash
sample_path=$1
path_output=$2
path_to_database='/home/projects/group-a/Team1-GenePrediction/db/swissprot.dmnd'
if [[ ! -d $path_output ]]
then
   mkdir -p $path_output
fi

for file in $(ls ${sample_path}*.fasta)
do
    output_file=$( echo $file | sed -e "s|$sample_path|$path_output|g" -e "s|fasta|tbl|g" )
    /home/projects/group-a/bin/Diamond blastx --query ${file} --db ${path_to_database} --out $output_file --outfmt 6 sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore slen qlen qcovhsp --threads 12 --max-target-seqs 1
done
