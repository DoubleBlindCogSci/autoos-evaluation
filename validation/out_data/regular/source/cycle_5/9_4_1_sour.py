from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JAmxrd=Factor('Tj(dqKuDai',["mvVxuGpSSy:vp","J2TqQMdGeghh"," )}F(VaIy"," hn0eWdieS",'xZ1d{','VPWkyEw',"WYXSe?dG","pOPgX9#aGRX_k",'yeXm '])
LNRY7SnZJ1=Factor(')HZFDkQEKcx',['b[SIBy|VQQyjD',"L@DYJX",'HBbX[1xgf',"wiedIudnsBT&Xd","Tov<gm2nQx",":1v","xdsdZgjq0Gsw","DMHM","eTSkZuwq;"])
qpvlJkZMj=Factor('1?W',['{FsKTamx',Level('Hk!FI*fF',3),Level("[sWQAwcVu|ovk",2),'NO)M6','EGxDU@3SVqdzJu',"psBQMfCk","}xpxITnxbft",'HqgyfKXq;v','DWGQocI'])
Z6R3DR=Factor('gYm}dH:(',["eLSs<",')BAnfERE','*_2kFQ','iXa',"YNE]mlvZ",'pLK',Level("e[ibcwsjfzBpj",3),"sfX",'IuIbQm#Spsz{yM'])

### EXPERIMENT
design=[JAmxrd,LNRY7SnZJ1,qpvlJkZMj,Z6R3DR]
crossing=[JAmxrd,LNRY7SnZJ1,qpvlJkZMj,Z6R3DR]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_4_1_0.csv"))
nr_factors=4
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)