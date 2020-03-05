#! /usr/bin/python
# Team 1 - Gene Prediction
import subprocess

'''
Runs tRNAscan-SE on the isolates 


options explained for tRNAscan-SE:
-B for bacteria
-L for legacy mode (the standard mode) (tRNAscan, EufindtRNA, and COVE)
-H shows the breakdown of the primary structure componenets to covariance model bit scores

-o output file
-f file with structural visualization
-m run stats file
-b bed file
-a fasta file
'''

def main(): # runs the tRNA command for all 50 isolate files
    pathToIsolates = '/home/projects/group-a/Team1-GenomeAssembly/assembled_output/' # this is the path to the isolates
    command = 'ls ' + pathToIsolates 
    allIsolateFiles = subprocess.check_output(command,shell=True)
    allIsolateFiles = allIsolateFiles.split('\n')
    print(allIsolateFiles)
    for fileName in allIsolateFiles:
        if fileName != '':
            fileID = fileName.split('_')
            fileID = fileID[0]
            command = '/home/mahmad42/bin/tRNAscan-SE-2.0/tRNAscan-SE -B -L -H ' \
            '-o /home/mahmad42/results_tRNAscan-SE/'+fileID+'.out ' \
            '-f /home/mahmad42/results_tRNAscan-SE/'+fileID+'_tRNA_struc.out ' \
            '-m /home/mahmad42/results_tRNAscan-SE/'+fileID+'_stats.out ' \
            '-b /home/mahmad42/results_tRNAscan-SE/'+fileID+'.bed ' \
            '-a /home/mahmad42/results_tRNAscan-SE/'+fileID+'.fasta' \
            '' + pathToIsolates + fileName
            action = subprocess.call(command,shell=True)


main()