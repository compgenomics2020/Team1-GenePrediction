#!/bin/bash
genome=$1
file_name=$(echo $genome | sed -e 's|.*\/||g' -e 's/.fasta//')
if [ ! -d ../results/rnammer/ ]
then
    mkdir -p ../results/rnammer/
fi
./rnammer-1-2/rnammer -S bac -m tsu,lsu,ssu -gff ../results/rnammer/${file_name}.gff $genome
