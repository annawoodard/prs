import pandas as pd

final = None
chunksize = 100000

with open('info.txt') as f:
    columns = f.readline().strip().split()

info_reader = pd.read_csv(open('info.txt'), chunksize=chunksize, sep=" ")
genotype_reader = pd.read_csv(open('genotype.txt'), chunksize=chunksize, sep=" ", names=columns)

for info, genotype in zip(info_reader, genotype_reader):
    filtered_info = info[(info['type'] >= 0.7) & (info['certainty'] >= 0.005) & (info['certainty'] <= 0.995)]
    filtered_genotype = genotype[(info['type'] >= 0.7) & (info['certainty'] >= 0.005) & (info['certainty'] <= 0.995)]
    filtered_genotype['chr_index'] = filtered_info['chr_index']

    if final is None:
        final = filtered_genotype
    else:
        final = pd.concat([final, filtered_genotype])

final.to_pickle('final.pkl')
