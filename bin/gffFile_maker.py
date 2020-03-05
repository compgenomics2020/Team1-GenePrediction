#!/usr/bin/python
# Team 1 - Gene Prediction
###
import subprocess
###

'''
Converts file to a GFF file (GFF version 2)

The function (aragornBatchToGFF) converts the 
results of Aragorn which are in a batch file, into a GFF file.
'''

def aragornBatchToGFF():
    batchPath = '/home/projects/group-a/Team1-GenePrediction/results/tRNAscan-SE_results/aragornBatch/'
    aragornGFFpath = '/home/projects/group-a/Team1-GenePrediction/results/tRNAscan-SE_results/aragornGFF/'
    isolateDict = {} # where isolate id (CGT###) is the key
    tRNAscan_SE_results_path = '/home/projects/group-a/Team1-GenePrediction/results/tRNAscan-SE_results/'
    command1 = "ls " + tRNAscan_SE_results_path + " | cut -f1 -d'_' | cut -f1 -d'.' | sort | uniq"
    isolateIDList = subprocess.check_output(command1, shell=True)
    isolateIDList = isolateIDList.split('\n') ## capturing command one produces a list of the isolate IDs
    for isolateID in isolateIDList:
        if isolateID != '' and 'CGT' in isolateID: # just in case another file name was captured in the command
            scaffoldNumber = 0 # initializing the scaffold variable
            scaffoldDict = {} # the key will be the scaffold number, and the value will be a list of genes
            batchHandle = open(batchPath + isolateID + '_Aragorn_batchfile','r')
            for line in batchHandle:
                line = line.strip()
                if line[0] == '>': # then the line is a header for the scaffold
                    line = line.split(' ') # [">346","length=234","depth=0.90x"]
                    scaffoldNumber = line[0] # >346
                    scaffoldNumber = scaffoldNumber[1:] # 346
                    scaffoldDict[scaffoldNumber] = [] # initializes the scaffold key value pair
                elif line == '0 genes found':
                    'nothing happends'
                    "don't need to include this in our gff file"
                elif line != '0 genes found' and 'genes found' in line:
                    # this line identifies the number of genes in the scaffold, if they are not zero genes
                    line = line.split(' ')
                    genesFound = line[0]
                elif 'tRNA-' in line and '[' in line and ']' in line:
                    # this is where the information for the gene is
                    line = line.split(' ')
                    listo = []
                    for x in line:
                        if x != '': # removes white space
                            listo.append(x) # listo contains the values in the line, without the white space
                    coordinates = listo[2] # identifies where the stop and start positions are
                    coordinates = coordinates.split('\t') # removes white space
                    coordinates = coordinates[0] # removes white space
                    if coordinates[0] == 'c': # some coordinates have a 'c' character in front of them
                        coordinates = coordinates[1:] # removes 'c' character
                    coordinates = coordinates.split(',') # splits start and stop positions
                    start = coordinates[0][1:] 
                    stop = coordinates[1][0:len(coordinates[1])-1]
                    scaffoldDict[scaffoldNumber].append([start,stop]) # adds the list containing the start and stop positions for 1 gene into the scaffold number's list
            isolateDict[isolateID] = scaffoldDict # after all the genes for the scaffold have gone through, the scaffold dict is added to the isolate dict
            batchHandle.close()
    for isolateID in isolateDict: # now writing a gff for every isolate
        gffHandle = open(aragornGFFpath + isolateID + '.gff','w')
        gffHandle.write('##gff-version 2\n') # first line
        scaffoldDict = isolateDict[isolateID]
        for scaffoldNumber in range(0,1000): # just so i can add the scaffolds numerically in order
            scaffoldNumber = str(scaffoldNumber)
            if scaffoldNumber in scaffoldDict.keys():
                if scaffoldDict[scaffoldNumber] == '[]': # this occurs if the scaffold has no genes
                    'nothing'
                else:
                    genes = scaffoldDict[scaffoldNumber] # pulls the list of genes out
                    for gene in genes:
                        start = gene[0]
                        stop = gene[1]
                        score = '.' # not available in batch file
                        leadLag = '.' # not available in batch file
                        phae = '.' # not available in batch file
                        gffHandle.write(scaffoldNumber +'\t'+ 'aragorn' +'\t'+ 'tRNA' +'\t'+ start +'\t'+ stop +'\t'+ score +'\t'+ leadLag +'\t'+ phae +'\t'+ isolateID + '\n')
                        # writes the information to the file
        gffHandle.close()
    return
    
aragornBatchToGFF()