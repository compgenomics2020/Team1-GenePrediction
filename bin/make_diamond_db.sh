#!/usr/bin/bash
# create diamon database from nr db using taxdmp and accession2taxid to filter by taxid
#requires nr db from ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nr.gz
#acession to taxid mapping from ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/prot.accession2taxid.gz
#and nodesdmp from within ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdmp.zip
# filter the db for Enterobacteriaceae by taxon id 543
path_to_db="/home/projects/group-a/Team1-GenePrediction/db"

/home/projects/group-a/bin/Diamond makedb --in ${path_to_db}/nr/nr.gz -d ${path_to_db}/nr_enterobacteriaceae --taxonmap ${path_to_db}/prot.accession2taxid.gz --taxonnodes ${path_to_db}/taxdmp/nodes.dmp --threads 8 --taxonlist 543
