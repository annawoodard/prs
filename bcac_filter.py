import pandas as pd

finalGeno = None 
finalInfo = None

chunksize = 10000 #50000 

genotype = pd.read_csv('/gpfs/data/huo-lab/BCAC/Imputed_prob/haiman_503_african_oncoarray_imputed_probs_chr22.txt.gz', chunksize = chunksize, sep = " ", header = None)

infotype = pd.read_csv('/gpfs/data/huo-lab/BCAC/Imputed/onco_bcac_african_info_chr22_varid.txt', chunksize=chunksize, sep = " ", header = 0) #, compression = 'gzip') uncomment later for zipped files

for info in infotype:#for chunk in reader: 
        geno_chunk = genotype.get_chunk(chunksize)   
        filteredInfo = info[(info['type'] >= 0.7) & (info['certainty'] >= 0.005) & (info['certainty'] <= 0.995)]
        filteredGeno = geno_chunk[(info['type'] >= 0.7) & (info['certainty'] >= 0.005) & (info['certainty'] <= 0.995)]	

        if final is None:
                finalInfo = filteredInfo
                finalGeno = filteredGeno
        else:
                finalInfo = pd.concat([finalInfo, filteredInfo])
                finalGeno = pd.concat([finalGeno, filteredGeno])

finalInfo.to_csv(r'/gpfs/data/huo-lab/BCAC/DataCombined/BCAC/BCAC_Info7MAF005_Chr22Info.csv', header = 0, index = None, sep = ' ') #only works if final is not None
finalGeno.to_csv(r'/gpfs/data/huo-lab/BCAC/DataCombined/BCAC/BCAC_Info7MAF005_Chr22Geno.csv', header = None, index = None, sep = ' ')

#Remember, a few hours of trial and error could save you several minutes of looking at the documentation.
