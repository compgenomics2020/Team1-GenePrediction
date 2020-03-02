#!/home/apfennig3/anaconda3/envs/geneprediction/bin/python3.8
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import numpy as np
import os
from matplotlib.lines import Line2D

def read_predicted_genes(path):
    gene_ids = []
    with open(path, 'r') as f:
        for line in f:
            if not line.startswith('#') and not len(line.strip()) ==0 and 'Glimmer' not in path:
                if 'gms2' in path:    
                    gene_ids.append(int(line.split('\t')[-1].split(';')[0].split('gene_id ')[1]))
                elif 'prodigal' in path:
                    gene_ids.append(line.split('\t')[-1].split(';')[0].split('ID=')[1])
            elif 'Glimmer' in path and not line.startswith('>'):
                gene_ids.append(line.split(' ')[0])
    return np.array(gene_ids)     

def read_diamond_results(path):
    columns = ['sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore', 'slen', 'qlen', 'qcovhsp']
    hits = pd.read_csv(path, header=None, sep='\t', names=columns)
    # filter out hits with an e-value greater than 0.001
    #hits = hits.iloc[np.where(hits.loc[:, 'evalue'].values < 0.001)[0]]
    #hits = hits.iloc[np.where(hits.loc[:, 'pident'].values > 50)[0]]
    hits = hits.iloc[np.where(hits.loc[:, 'qcovhsp'].values > 70)[0]]
    #hits = hits.iloc[np.where(hits.loc[:, 'bitscore'].values >= 50)[0]]

    return hits.iloc[:, 0].values

def plot_pred_vs_blast(pred_ids_gms2, hit_ids_gms2, pred_ids_glimmer, hits_glimmer, pred_ids_prodigalm, hit_ids_prodigal, samples):
    fig, ax = plt.subplots()
    handles = [Line2D([0], [0], marker='x', color='r'), Line2D([0], [0], marker='o', color='b'), Line2D([0], [0], marker='s', color='g')]
    labels = ['GMS2', 'Glimmer', 'Prodigal']
    for i, p_gms2, h_gms2, p_glimmer, h_glimmer, p_prodigal, h_prodigal in zip(np.arange(50), pred_ids_gms2, hit_ids_gms2, pred_ids_glimmer, hits_glimmer, pred_ids_prodigalm, hit_ids_prodigal):
        ax.plot(i * 1.5, h_gms2.shape[0] / p_gms2.shape[0], marker='x', c='r')
        ax.plot(i * 1.5, h_glimmer.shape[0] / p_glimmer.shape[0], marker='o', c='b')
        ax.plot(i * 1.5, h_prodigal.shape[0] / p_prodigal.shape[0], marker='s', c='g')
    #ax.set_ylim([3800, 5200])
    #ax.set_xlim([3800, 5200])
    #ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
    ax.axhline(1.0, ls='--')
    ax.set_ylim([0.0, 1.1])
    ax.set_xticks(np.arange(50) * 1.5)
    ax.set_xticklabels(samples, rotation=90, fontsize=8)
    ax.set_xlabel('Sample')
    ax.set_ylabel('Number of genes with BLAST hit/total number of genes')
    ax.set_title('Number of genes with BLAST support vs.\ntotal number of predicted genes')
    ax.legend(handles, labels, bbox_to_anchor=(0.5, -0.35), loc='lower center', ncol=3)
    fig.savefig('genes_with_blast_support.png', bbox_inches='tight')
    plt.close('all')

def plot_number_of_genes_per_sample(pred_gms2, pred_glimmer, pred_prodigal, samples):
    fig, ax = plt.subplots(3, 1, sharex=True, sharey=False)
    fig.tight_layout(pad=3.0)
    handles = [Line2D([0], [0], color='r'), Line2D([0], [0], color='b'), Line2D([0], [0], color='g')]
    labels = ['GMS2', 'Glimmer', 'Prodigal']
    #for i, p_gms2, p_glimmer, p_prodigal in zip(np.arange(50), pred_gms2, pred_glimmer, pred_prodigal):
    p_gms2 = [x.shape[0] for x in pred_gms2]
    p_prodigal = [x.shape[0] for x in pred_prodigal]
    p_glimmer = [x.shape[0] for x in pred_glimmer]
    #import pdb; pdb.set_trace()
    ax[0].bar(np.arange(50) * 1.5, p_gms2, color='r')
    ax[2].bar(np.arange(50) * 1.5, p_glimmer, color='b')
    ax[1].bar(np.arange(50) * 1.5, p_prodigal, color='g')
    ax[2].set_xticks(np.arange(50) * 1.5)
    ax[2].set_xticklabels(samples, rotation=90, fontsize=8)
    ax[2].set_xlabel('Sample')
    ax[0].set_ylim([0, 5200])
    ax[0].set_yticks([0, 1000, 2000, 3000, 4000, 5000])
    ax[1].set_ylim([0, 5200])
    ax[1].set_yticks([0, 1000, 2000, 3000, 4000, 5000])
    ax[2].set_ylim([0, 5200])
    ax[2].set_yticks([0, 1000, 2000, 3000, 4000, 5000])

    ax[1].set_ylabel('Number of predicted genes')
    ax[2].set_title('Glimmer')
    ax[1].set_title('Prodigal')
    ax[0].set_title('GMS2')
    fig.savefig('number_predicted_genes.png', bbox_inches='tight')
    plt.close('all')


if __name__ == "__main__":
    list_of_samples = os.listdir("../results/gms2_results/")
    unique_list = set([x.split('.')[0] for x in list_of_samples])
    pred_ids_gms2 = []
    pred_ids_prodigal = []
    pred_ids_glimmer = []
    hit_ids_gms2 = []
    hit_ids_prodigal = []
    hit_ids_glimmer = []
    for sample in unique_list:
        pred_ids_gms2.append(read_predicted_genes(f"../results/gms2_results/{sample}.gff"))
        pred_ids_glimmer.append(read_predicted_genes(f"../../gene_prediction/Glimmerout/{sample}.predict"))
        pred_ids_prodigal.append(read_predicted_genes(f"../../gene_prediction/prodigal_output/{sample}.gff"))
        hit_ids_gms2.append(read_diamond_results(f"../results/diamond/gms2/{sample}.tbl"))
        hit_ids_glimmer.append(read_diamond_results(f"../results/diamond/Glimmer3/{sample}.tbl"))
        hit_ids_prodigal.append(read_diamond_results(f"../results/diamond/prodigal/{sample}.tbl"))
    samples = [x.split('_')[0] for x in unique_list]
    plot_number_of_genes_per_sample(pred_ids_gms2, pred_ids_glimmer, pred_ids_prodigal, samples)
    plot_pred_vs_blast(pred_ids_gms2, hit_ids_gms2, pred_ids_glimmer, hit_ids_glimmer, pred_ids_prodigal, hit_ids_prodigal, samples)
 
