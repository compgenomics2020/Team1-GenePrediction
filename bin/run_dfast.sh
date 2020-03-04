#!/usr/bin/bash
#activate environment
source activate geneprediction
v=0
g=0
r=0
while getopts ":hi:o:grv" opt
do
    case $opt in
       h )
         echo " -i <input of file> -o <path to output> -g <run GMS2 instead of prodigal> -r <run RNAmmer instead of barrnarp> -v <verbose> "
         ;;
       i )
         i=$OPTARG
         ;;
       o )
         o=$OPTARG
         ;;
       r )
         r=1
         ;;
       g )
         g=1
         ;;
       v )
         v=1
         ;;
     esac
done
genome=$i
output=$o
#get file name
genome_name=$( echo $genome | sed -e "s|.*\/||g" -e "s|.fasta||g" )

# create output directory if doesn't exist
if [ ! -d $output ]
then
    mkdir -p ${output}
fi

if [ "$v" -eq 1 ]
then
    echo Analyzing $genome_name
fi

# set CDS prediction tool
if [ "$g" -eq 1 ]
then
    cds_tool='--use_genemarks2 bact'
else
    cds_tool='--use_prodigal'
fi

# run dfast with or without RNAmmer
if [ "$r" -eq 1 ]
then
    ./dfast_core/dfast -g $genome -o tmp_dfast --organism Ecoli --minimum_length 120 $cds_tool --gcode 11 --cpu 8 --use_rnammer bact
else
    ./dfast_core/dfast -g $genome -o tmp_dfast --organism Ecoli --minimum_length 120 $cds_tool --gcode 11 --cpu 8
fi

# move files in final path and clean up
mv tmp_dfast/genome.gff ${output}${genome_name}.gff
mv tmp_dfast/protein.faa ${output}${genome_name}_protein.faa
mv tmp_dfast/cds.fna ${output}${genome_name}_cds.fna
mv tmp_dfast/rna.fna ${output}${genome_name}_rna.fna
rm -r tmp_dfast
