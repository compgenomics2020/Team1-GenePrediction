#!/home/apfennig3/anaconda3/envs/geneprediction/bin/python3.8
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import numpy as np
import os
from matplotlib.lines import Line2D

def read_predicted_genes(path):
    """
    Reads in predicted genes from GFF file
    path: directory to gff file
    return: list of gene ids
    """
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
    """
    Reads in DIAMOND results and filters them by coverage
    path: path to blast results
    return: array with ids of hits
    """
    columns = ['sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore', 'slen', 'qlen', 'qcovhsp']
    hits = pd.read_csv(path, header=None, sep='\t', names=columns)
    # filter out hits with an e-value greater than 0.001
    #hits = hits.iloc[np.where(hits.loc[:, 'evalue'].values < 0.001)[0]]
    #hits = hits.iloc[np.where(hits.loc[:, 'pident'].values > 50)[0]]
    hits = hits.iloc[np.where(hits.loc[:, 'qcovhsp'].values > 70)[0]]
    #hits = hits.iloc[np.where(hits.loc[:, 'bitscore'].values >= 50)[0]]

    return hits.iloc[:, 0].values

def plot_pred_vs_blast(pred_ids_gms2, hit_ids_gms2, pred_ids_glimmer, hits_glimmer, pred_ids_prodigalm, hit_ids_prodigal, samples):
    """ 
    Plots ratio of predicted genes with BLAST support for each of the 50 samples
    """
    fig, ax = plt.subplots()
    # intitialize legend
    handles = [Line2D([0], [0], marker='x', color='r'), Line2D([0], [0], marker='o', color='b'), Line2D([0], [0], marker='s', color='g')]
    labels = ['GMS2', 'Glimmer', 'Prodigal']
    # plot each samples
    for i, p_gms2, h_gms2, p_glimmer, h_glimmer, p_prodigal, h_prodigal in zip(np.arange(50), pred_ids_gms2, hit_ids_gms2, pred_ids_glimmer, hits_glimmer, pred_ids_prodigalm, hit_ids_prodigal):
        ax.plot(i * 1.5, h_gms2.shape[0] / p_gms2.shape[0], marker='x', c='r')
        ax.plot(i * 1.5, h_glimmer.shape[0] / p_glimmer.shape[0], marker='o', c='b')
        ax.plot(i * 1.5, h_prodigal.shape[0] / p_prodigal.shape[0], marker='s', c='g')
    #ax.set_ylim([3800, 5200])
    #ax.set_xlim([3800, 5200])
    #ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
    # do formatting
    ax.axhline(1.0, ls='--')
    ax.set_ylim([0.0, 1.1])
    ax.set_xticks(np.arange(50) * 1.5)
    ax.set_xticklabels(samples, rotation=90, fontsize=8)
    ax.set_xlabel('Sample')
    ax.set_ylabel('Number of genes with BLAST hit/total number of genes')
    ax.set_title('Number of genes with BLAST support vs.\ntotal number of predicted genes')
    ax.legend(handles, labels, bbox_to_anchor=(0.5, -0.35), loc='lower center', ncol=3)
    # save
    fig.savefig('genes_with_blast_support.png', bbox_inches='tight')
    plt.close('all')

def plot_number_of_genes_per_sample(pred_gms2, pred_glimmer, pred_prodigal, samples):
    """
    Plots the number of predicted coding genes in each of the 50 samples as a bar plot
    """
    # initiaize plots
    fig_0, ax_0 = plt.subplots()
    fig_1, ax_1 = plt.subplots()
    fig_2, ax_2 = plt.subplots()
    #get number of predicted genes
    p_gms2 = [x.shape[0] for x in pred_gms2]
    p_prodigal = [x.shape[0] for x in pred_prodigal]
    p_glimmer = [x.shape[0] for x in pred_glimmer]
    # plot GMS2
    ax_0.bar(np.arange(50) * 1.5, p_gms2, color='r')
    # plot Glimmer
    ax_1.bar(np.arange(50) * 1.5, p_glimmer, color='b')
    # plot Prodigal
    ax_2.bar(np.arange(50) * 1.5, p_prodigal, color='g')
    # do formatting
    ax_2.set_xticks(np.arange(50) * 1.5)
    ax_2.set_xticklabels(samples, rotation=90, fontsize=8)
    ax_2.set_xlabel('Sample')
    ax_1.set_xticks(np.arange(50) * 1.5)
    ax_1.set_xticklabels(samples, rotation=90, fontsize=8)
    ax_1.set_xlabel('Sample')
    ax_0.set_xticks(np.arange(50) * 1.5)
    ax_0.set_xticklabels(samples, rotation=90, fontsize=8)
    ax_0.set_xlabel('Sample')

    ax_0.set_ylim([0, 5200])
    ax_0.set_yticks([0, 1000, 2000, 3000, 4000, 5000])
    ax_1.set_ylim([0, 5200])
    ax_1.set_yticks([0, 1000, 2000, 3000, 4000, 5000])
    ax_2.set_ylim([0, 5200])
    ax_2.set_yticks([0, 1000, 2000, 3000, 4000, 5000])

    ax_2.set_ylabel('Number of predicted genes')
    ax_1.set_ylabel('Number of predicted genes')
    ax_0.set_ylabel('Number of predicted genes')
    ax_2.set_title('Prodigal')
    ax_1.set_title('Glimmer')
    ax_0.set_title('GMS2')

    fig_0.savefig('number_predicted_genes_gms2.png', bbox_inches='tight')
    fig_1.savefig('number_predicted_genes_glimmer.png', bbox_inches='tight')
    fig_2.savefig('number_predicted_genes_prodigal.png', bbox_inches='tight')
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
    # read results of all samples
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
 
