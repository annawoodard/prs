
import pandas as pd

finalGeno = None 
finalInfo = None

chunksize = 35000 

genotype = pd.read_csv('/gpfs/data/huo-lab/BCAC/DataCombined/AABC/AABC_chr1.gen.gz', chunksize = chunksize, sep = " ", header = None)

infotype = pd.read_csv('/gpfs/data/huo-lab/BCAC/DataCombined/AABC/AABC_Info.chr1.txt', chunksize=chunksize, sep = "\t", header = None) 

for info in infotype:
  geno_chunk = genotype.get_chunk(chunksize)   

filteredInfo = info[(info[7] >= 0.7) & (info[5] >= 0.005) & (info[5] <= 0.995)]
filteredGeno = geno_chunk[(info[7] >= 0.7) & (info[5] >= 0.005) & (info[5] <= 0.995)]	


if final is None:
    finalInfo = filteredInfo
    finalGeno = filteredGeno
else:
    finalInfo = pd.concat([finalInfo, filteredInfo])
    finalGeno = pd.concat([finalGeno, filteredGeno])

finalInfo.to_csv(r'/gpfs/data/huo-lab/BCAC/DataCombined/AABC/AABC_MAF005Info7_chr1.Info.txt', header = None, index = None, sep = " ") #only works if final is not None
finalGeno.to_csv(r'/gpfs/data/huo-lab/BCAC/DataCombined/AABC/AABC_MAF005Info7_chr1.gen.gz', header = None, index = None, sep = " ", compression = "gzip")

#Remember, a few hours of trial and error could save you several minutes of looking at the documentation.



  
