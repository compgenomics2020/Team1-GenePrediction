# Team 1 Gene Prediction
For more information refer to our [Wiki](https://compgenomics2020.biosci.gatech.edu/Team_I_Gene_Prediction_Group)<br/>

## Run tools for valdiation purposes
### GeneMarkS2
- run GMS2, will create a folder for output in /home/apfennig3/Team1-GenePrediction/results/gms2<br/>
```
    ./run_gms2.sh <path_to_genome>
```
### Glimmer3 
- run Glimmer3, will create a folder for output in /home/apfennig3/Team1-GenePrediction/<br/>
```
    ./run_glimmer3.sh <path_to_genome> 
```

### Compare predictions of ab-initio CDS predicting tools
#### BLAST validation
- Create database for DIAMOND<br/>
```
./make_diamond_db.sh
```
- Run DIAMOND<br/>
```
./run_diamond.sh
```
- Plot ratio of predicted genes with BLAST support after filtering on coverage > 70% and plot bar plot of number of predicted genes per sample.<br/>
```
./plot_comparision_blast_ab_intio.py
```

#### Overlaps
- Compare predictions pairwise and finally all 3<br/>
```
./get_overlaps.sh
```
- Get the number of genes of overlaps<br/>
```
./get_gene_counts.sh
```
- Visualize overlaps as Venn diagram<br/>
```
./plot_venn_diagramm.py
```


### RNAmmer
- run RNAmmer, will create a folder for output in /home/apfennig3/Team1-GenePrediction/results/rnammer<br/>
```
    ./run_glimmer3.sh <path_to_genome>
```

## Run final pipeline
The pipeline uses the DFAST framework to run the tools in a parallel manner. Thus, allows to analyze a complete E.coli genome within approximately 26 seconds.<br/>
By default the pipeline executes Prodigal the CDS prediction, Aragorn for tRNA prediction, barrnarp for rRNA prediction and for CRISPR prediction. However, optionally GeneMarkS2 can applied for the CDS prediction instead of Prodigal and RNAmmer for the rRNA prediction instead of barrnarp. These tools produce equivalent results but run significantly slower.<br/>

### Usage:
```
./run_dfast.sh -h <help>
     -i path to input genome (FASTA format) 
     -o output directory
     [-g] run GeneMarkS2 instead of PRodigal for CDS prediction
     [-r] run RNAmmer instead of barrnarp for rRNA prediction 
     [-v] verbosity
```

### Output:
The output will be four files:
* File with gene predictions in .gff format
* File with protein sequences of predicted genes in FASTA format (*_protein.faa)
* File with nucleotide sequences of predicted coding genes in FASTA format (*_cds.fna)
* File with nucleotide sequences of predicted RNA genes in FASTA format (*_rna.fna)
 
