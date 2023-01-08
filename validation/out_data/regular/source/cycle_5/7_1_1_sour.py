from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iQjl3t=["IhYsmgLiYfpC",'57H7fsSJAd',"qlQfUqJ{G","iXbtgrA","dTyqjFcmcBE>L","C8VeWdMnu1dwni"]
J0IdyRQha=[iQjl3t[2],'LTv',"ScqNV_","PGEgKoJep","f:ngJai5?j^s",Level('R<f',3),"g#OlCG",'Zw6h']
B3zq7YHA9=Factor('>#J5D7CHMhfZqE',J0IdyRQha)

### EXPERIMENT
design=[B3zq7YHA9]
crossing=[B3zq7YHA9]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_1_1_0.csv"))
nr_factors=1
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)