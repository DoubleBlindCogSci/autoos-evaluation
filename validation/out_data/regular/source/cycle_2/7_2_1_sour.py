from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tNkWN=[Level("{vrGALh#w",7),Level("O8RV)rv{Vh",6),"AT[w",'!lIwNNNzZhXSE',"byA^d<jnV",'4NMpPWsLpj','ap~)y7bFUm!)']
siyFfY=Factor("MP7FzIHmqdW",tNkWN)
k_lfXnaFQu='TlZM'
YJ8p=Level("Z4QEwqb",8)
exdU=Factor('RBx',[YJ8p,'Q)HnCEu5I',"d3nmjAaP",Level('XPtVlLK2gKCrj',10),"5S*MThl og>jN","fREIS5qcowiSjA","YbWiXA","Ko>0W",k_lfXnaFQu])

### EXPERIMENT
design=[siyFfY,exdU]
crossing=[siyFfY,exdU]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_2_1_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)