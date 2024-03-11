from itertools import combinations
from Bio import SeqIO
import gzip
import pandas as pd
import sys
import re
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('path', help= "Path to file list")
args = parser.parse_args()

path = f"/home/projects/animalia_mito/data/{args.path}/{args.path}_rota_new.fa.gz"

with gzip.open(path, "rt") as file:
    sequences = SeqIO.parse(file, "fasta")
    name = []
    for i in sequences:
        name.append(i.id)

df = pd.DataFrame(columns = name, index = name)
sim = pd.DataFrame(columns = name, index = name)
iden = pd.DataFrame(columns = name, index = name)
gap = pd.DataFrame(columns = name, index = name)

dup_samp = []
with gzip.open(path, "rt") as file:
    multi = combinations(SeqIO.parse(file, "fasta"), 2)
    for pair in multi:
        seq1 = pair[0].seq
        seq2 = pair[1].seq
        f = open (f"/home/projects/animalia_mito/data/{args.path}/{args.path}_{pair[0].id}_{pair[1].id}.txt", "r")
        f = f.read().split('\n')
        for line in f:
           if re.search("Score", line):
               l = float(line[9:])
               df.at[pair[0].id,pair[1].id] = l
               df.at[pair[1].id,pair[0].id] = l
           if re.search("Identity", line):
               d = float(line[27:31])
               iden.at[pair[0].id,pair[1].id] = d
               iden.at[pair[1].id,pair[0].id] = d
               if d > 99.0:
                   dup_samp.append(pair[1].id)
           if re.search("Similarity", line):
               s = float(line[27:31])
               sim.at[pair[0].id,pair[1].id] = s
               sim.at[pair[1].id,pair[0].id] = s
           if re.search("Gaps", line):
               g = float(line[27:31])
               gap.at[pair[0].id,pair[1].id] = g
               gap.at[pair[1].id,pair[0].id] = g



def get_average(name, df):
    x = []
    for i in range(len(name)):

        x1 = df[name[i]].sum()
        x2 = x1/len(name)
        x.append(x2)

    return x
print(name)
print(df)
score = get_average(name, df)
print(score)
simila = get_average(name, sim)
gaps = get_average(name, gap)
mx = max(score)
print(mx)

per = []
for j in score:
    p = (mx - j) / mx
    if p > 0.5:
        dex = score.index(j)
        per.append(dex)
    else:
        pass

similarity = []
for m in simila:
    if m < 49.9:
        dex = simila.index(m)
        similarity.append(dex)
    else:
        pass

g = []
for n in gaps:
    if n > 15.0:
        dex = gaps.index(n)
        g.append(dex)
    else:
        pass


all_exclude = []
if len(dup_samp) != 0:
    all_exclude.append(dup_samp)
    print("The following sample will be excluded as it is a duplicate sample:" + ' '.join(dup_samp), file = sys.stdout)
else:
    pass
if len(per) != 0:
    res_list = [name[i] for i in per]
    all_exclude.append(res_list)
    print("The following samples will be excluded due to a low pairwise score:" + ' '.join(res_list), file = sys.stdout)
else:
    pass
if len(similarity) != 0:
    res_list3 = [name[i] for i in similarity]
    all_exclude.append(res_list3)
    print("The following samples will be excluded due to a low similarity score:" + ' '.join(res_list3), file = sys.stdout)
else:
    pass
if len(g) != 0:
    res_list4 = [name[i] for i in g]
    all_exclude.append(res_list4)
    print("The following samples will be excluded due to a high gap score:" + ' '.join(res_list4), file = sys.stdout)
else:
    pass

all_ex = [item for sublist in all_exclude for item in sublist]
print(all_ex)
kept = []
with gzip.open(path, "rt") as rm_file:
    all = SeqIO.parse(rm_file, "fasta")
    for record in all:
        if record.id not in all_ex:
            kept.append(record)
        else:
            print(f"Sequence {record.id}'s pairwise alignment was too different. Sequence will be excluded", file = sys.stdout)

    with gzip.open(f"/home/projects/animalia_mito/data/{args.path}/{args.path}_for_msa.fa.gz", "wt") as final:
        SeqIO.write(kept, final, "fasta")

    with gzip.open(f"/home/projects/animalia_mito/data/{args.path}/{args.path}_for_msa.fa.gz", "rt") as file:
        multi = combinations(SeqIO.parse(file, "fasta"), 2)
        for pair in multi:
            seq1 = pair[0].seq
            seq2 = pair[1].seq
            f = open (f"/home/projects/animalia_mito/data/{args.path}/{args.path}_{pair[0].id}_{pair[1].id}.txt", "r")
            f = f.read().split('\n')
            for line in f:
               if re.search("Score", line):
                   l = float(line[9:])
                   df.at[pair[1].id,pair[0].id] = l
                   df.at[pair[0].id,pair[1].id] = l
               
    x = []
    for i in range(len(name)):

        x1 = df[name[i]].sum()
        x.append(x1)

    plt.figure(figsize=(20,10))
    plt.bar(name, x)
    plt.title(f"Pairwise alignment score sums for {args.path}")
    plt.xticks(rotation='vertical')

    plt.savefig(f"/home/projects/animalia_mito/data/{args.path}/{args.path}_pairwise_sum_clean.png")

