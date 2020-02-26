#!/usr/bin/bash

count_gms2=$(ls ../results/gms2_results/*.gff | xargs -I {} grep '^[0-9]' {} | wc -l | cut -d ' ' -f1 | paste -sd+ | bc)
count_prodigal=$(ls ../../gene_prediction/prodigal_output/*.gff | xargs -I {} grep '^[0-9]' {} | wc -l | cut -d ' ' -f1 | paste -sd+ | bc)
count_glimmer=$(ls ../../gene_prediction/Glimmerout/*.predict | xargs -I {} grep '^orf' {} | wc -l | cut -d ' ' -f1 | paste -sd+ | bc)
count_gms2_glimmer=$(ls ../results/overlaps/gms2_glimmer/*.gff | xargs -I {} wc -l {} | cut -d ' ' -f1 | paste -sd+ | bc)
count_gms2_prodigal=$(ls ../results/overlaps/gms2_prodigal/*.gff | xargs -I {} wc -l {} | cut -d ' ' -f1 | paste -sd+ | bc)
count_prodigal_glimmer=$(ls ../results/overlaps/prodigal_glimmer/*.gff | xargs -I {} wc -l {} | cut -d ' ' -f1 | paste -sd+ | bc)
count_gms2_prodigal_glimmer=$(ls ../results/overlaps/gms2_prodigal_glimmer/*.gff | xargs -I {} wc -l {} | cut -d ' ' -f1 | paste -sd+ | bc)

echo 'GMS2' $count_gms2
echo 'Prodigal' $count_prodigal
echo 'Glimmer' $count_glimmer
echo 'GMS2_Glimmer' $count_gms2_glimmer
echo 'GMS2_Prodigal' $count_gms2_prodigal
echo 'Prodigal_Glimmer' $count_prodigal_glimmer
echo 'GMS2_Prodigal_Glimmer' $count_gms2_prodigal_glimmer

