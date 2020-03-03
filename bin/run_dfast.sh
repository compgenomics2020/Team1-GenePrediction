#!/usr/bin/bash
source activate geneprediction
genome=$1
output=$2
genome_name=$( echo $genome | sed -e "s|..\/..\/Team1-GenomeAssembly\/assembled_output\/||g" -e "s|.fasta||g" )
../../dfast_core/dfast -g $genome -o $output --organism Ecoli --minimum_length 120 --use_prodigal --gcode 11 --cpu 8 --force  #--use_rnammer bact
mv ${output}genome.gff ${output}${genome_name}.gff
mv ${output}protein.faa ${output}${genome_name}_protein.faa
mv ${output}cds.fna ${output}${genome_name}_cds.fna
mv ${output}rna.fna ${output}${genome_name}_rna.fna
rm ${output}application.log
