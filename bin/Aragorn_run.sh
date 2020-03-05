#!/usr/bin/bash

cd /home/projects/group-a/Team1-GenomeAssembly/assembled_output/$i;
for i in *.fasta; do /home/projects/group-a/Tools/aragorn1.2.38/./aragorn  /home/projects/group-a/Team1-GenomeAssembly/assembled_output/$i -seq -w -o /home/projects/group-a/Team1-GenePrediction/results/Aragornresults/$i;
cd /home/projects/group-a/Team1-GenePrediction/Aragornresults/; rename -v _trim_assembled.fasta _Aragorn_predicted *_trim_assembled.fasta; done                   
