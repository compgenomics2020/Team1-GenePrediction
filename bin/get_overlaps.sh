#!/usr/bin/bash
path_a='../results/gms2_results/'
path_b='../../gene_prediction/prodigal_output/'
path_c='../../gene_prediction/Glimmerout/'
path_d='../results/overlaps/prodigal_glimmer/'

mkdir -p ../results/overlaps/gms2_prodigal/
mkdir -p ../results/overlaps/gms2_glimmer/
mkdir -p ../results/overlaps/prodigal_glimmer/
mkdir -p ../results/overlaps/gms2_prodigal_glimmer/

# GSM2 vs Prodigal
for file in $(ls ${path_a}*.gff)
do
    sample=$( echo $file | sed -e "s|$path_a||g" -e "s|.gff||g" )
    echo $sample
    ../../bin/compp -a $file -b ${path_b}${sample}.gff -v -F | grep '^[0-9]' > ../results/overlaps/gms2_prodigal/${sample}.gff
done

# GSM2 vs Glimmer
for file in $(ls ${path_a}*.gff)
do
    sample=$( echo $file | sed -e "s|$path_a||g" -e "s|.gff||g" )
    echo $sample
    ../../bin/compp -a $file -b ${path_c}${sample}.predict -v -F | grep '^[0-9]' > ../results/overlaps/gms2_glimmer/${sample}.gff
done

# Prodigal vs Glimmer
for file in $(ls ${path_b}*.gff)
do
    sample=$( echo $file | sed -e "s|$path_b||g" -e "s|.gff||g" )
    echo $sample
    ../../bin/compp -a $file -b ${path_c}${sample}.predict -v -F | grep '^[0-9]' > ../results/overlaps/prodigal_glimmer/${sample}.gff
done

# GSM2 vs Prodigal vsGlimmer
for file in $(ls ${path_a}*.gff)
do
    sample=$( echo $file | sed -e "s|$path_a||g" -e "s|.gff||g" )
    echo $sample
    ../../bin/compp -a $file -b ${path_d}${sample}.gff -v -F | grep '^[0-9]' > ../results/overlaps/gms2_prodigal_glimmer/${sample}.gff
done
