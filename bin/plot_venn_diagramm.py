#!/home/apfennig3/anaconda3/envs/geneprediction/bin/python3.8
from matplotlib_venn import venn3_unweighted
import matplotlib.pyplot as plt

def read_gene_counts():
    tool_counts_dict = {}
    with open('/home/projects/group-a/Team1-GenePrediction/bin/gene_counts.txt', 'r') as f:
        for line in f:
            line = line.strip().split(' ')
            tool_counts_dict[line[0]] = int(line[1])
    return tool_counts_dict

def infer_actual_numbers(counts):
    all = counts['GMS2_Prodigal_Glimmer']
    counts['GMS2_Prodigal'] -= all
    counts['GMS2_Glimmer'] -= all
    counts['Prodigal_Glimmer'] -= all
    counts['GMS2'] -= (all + counts['GMS2_Prodigal'] + counts['GMS2_Glimmer']) 
    counts['Prodigal'] -= (all + counts['GMS2_Prodigal'] + counts['Prodigal_Glimmer'])
    counts['Glimmer'] -= (all + counts['Prodigal_Glimmer'] + counts['GMS2_Glimmer'])
    return counts

def plot_venn_diagram(counts):
    fig, ax = plt.subplots()
    v = venn3_unweighted(subsets=(counts['GMS2'], counts['Prodigal'], counts['GMS2_Prodigal'],
                       counts['Glimmer'], counts['GMS2_Glimmer'], counts['Prodigal_Glimmer'],
                       counts['GMS2_Prodigal_Glimmer']),
              set_labels=('GMS2', 'Prodigal', 'Glimmer'))
    # ax.title('Venn diagram of predicted genes')
    fig.savefig('venn_unweighted.png', bbox_inches='tight')

if __name__ == '__main__':
    counts = read_gene_counts()
    counts = infer_actual_numbers(counts)
    plot_venn_diagram(counts)
