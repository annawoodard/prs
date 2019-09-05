import pandas as pd

final = None

chunksize = 100000

with open('info.txt') as f:
    columns = f.readline().strip().split()

info_reader = pd.read_csv(open('info.txt'), chunksize=chunksize, sep=" ")
genotype_reader = pd.read_csv(open('genotype.txt') , chunksize=chunksize, sep=" ", names=columns)

for info, genotype in zip(info_reader, genotype_reader):
    filtered_info = info[(info['type'] >= 0.7) & (info['certainty'] >= 0.005) & (info['certainty'] <= 0.995)]
    filtered_genotype = genotype[(info['type'] >= 0.7) & (info['certainty'] >= 0.005) & (info['certainty'] <= 0.995)] # index the genotype entries by a filter on the info entries
    filtered_total = pd.concat([filtered_info, filtered_genotype], axis=1)  # specify the axis so that we are concatenating along columns instead of rows

    if final is None:
        final = filtered_total
    else:
        final = pd.concat([final, filtered_total])

final.to_pickle('final.pkl')
