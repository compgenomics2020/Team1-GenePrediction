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
    ./run_rnammer.sh <path_to_genome>
```
### tRNAscan-SE
- runs tRNAscan-SE on the isolates, it will place the results in /home/projects/group-a/Team1-GenePrediction/results/tRNAscan-SE_results<br/>
- it runs tRNAscan-SE with the following options:
-       -B for bacteria
-       -L for legacy mode (the standard mode) (tRNAscan, EufindtRNA, and COVE)
-       -H shows the breakdown of the primary structure componenets to covariance model bit scores
-       -o output file
-       -f file with structural visualization
-       -m run stats file
-       -b bed file
-       -a fasta file
- The command is: 
```
    ./tRNAscan_tool.py
```
### Aragorn
-runs Aragorn on isolates, it will place the results in /home/projects/group-a/Team1-GenePrediction/results/Aragorn_results<br/>
-runs Aragorn with the following options:
    -w for batch output (batch is easily converted to gff)
    -seq displays the sequence of predicted tRNAs
    -o output file

## Run final pipeline
The pipeline uses the DFAST framework to run the tools in a parallel manner. Thus, allows to analyze a complete E.coli genome within approximately 26 seconds.<br/>
By default the pipeline executes Prodigal the CDS prediction, Aragorn for tRNA prediction, barrnarp for rRNA prediction and for CRISPR prediction. However, optionally GeneMarkS2 can applied for the CDS prediction instead of Prodigal, RNAmmer for the rRNA prediction instead of barrnarp and tRNAscan-SE for the tRNA prediction instead of Aragorn. These tools produce equivalent results but run significantly slower.<br/>

### Usage:
```
./run_dfast.sh -h <help>
     -i path to input genome (FASTA format) 
     -o output directory
     [-g] run GeneMarkS2 instead of Prodigal for CDS prediction
     [-r] run RNAmmer instead of barrnarp for rRNA prediction 
     [-t] run tRNAscan-SE instead of Aragorn for tRNA prediction
     [-v] verbosity
```

### Output:
The output will be four files:
* File with gene predictions in .gff format
* File with protein sequences of predicted genes in FASTA format (*_protein.faa)
* File with nucleotide sequences of predicted coding genes in FASTA format (*_cds.fna)
* File with nucleotide sequences of predicted RNA genes in FASTA format (*_rna.fna)

### Citations
* stand-alone version (DFAST-core)
DFAST: a flexible prokaryotic genome annotation pipeline for faster genome publication.
Bioinformatics; 2018; 34(6): 1037–1039.
Yasuhiro TANIZAWA, Takatomo FUJISAWA, Yasukazu NAKAMURA
[https://academic.oup.com/bioinformatics/article/34/6/1037/4587587](https://academic.oup.com/bioinformatics/article/34/6/1037/4587587)
* Lomsadze, A., Gemayel, K., Tang, S., & Borodovsky, M. (2018). Modeling leaderless transcription and atypical genes results in more accurate gene prediction in prokaryotes. Genome research, 28(7), 1079–1089. https://doi.org/10.1101/gr.230615.117
* A.L. Delcher, K.A. Bratke, E.C. Powers, and S.L. Salzberg. Identifying bacterial genes and endosymbiont DNA with Glimmer, Bioinformatics 23:6 (2007), 673-679.
* Lagesen, K., Hallin, P., Rødland, E. A., Staerfeldt, H. H., Rognes, T., & Ussery, D. W. (2007). RNAmmer: consistent and rapid annotation of ribosomal RNA genes. Nucleic acids research, 35(9), 3100–3108. https://doi.org/10.1093/nar/gkm160
* Buchfink B, Xie C, Huson DH. Fast and sensitive protein alignment using DIAMOND. Nat Methods. 2015;12(1):59–60. doi:10.1038/nmeth.3176
