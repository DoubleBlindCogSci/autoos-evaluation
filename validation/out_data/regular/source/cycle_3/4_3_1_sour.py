from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
znID=['guNcQia',Level("LCtiqhYJV",4),'RZKSouN&WZRt',"_EVgwS~BlrZ7p"]
qUNIUnsCPv=Factor(";ng",znID)
n0VCxbyyVmL=["~ujp*e","sczrjY$",")vAWn","zk}"]
mgEBdJLjSKd=Factor('cyX4srlXM_E',n0VCxbyyVmL)
oOp234=Factor("~Yw;u]PnGNb",['aOgLJ IhKxK','SThkrc',Level('ivYEax @Lnd{O6',3),"OcU>MhhCK4lod"])

### EXPERIMENT
design=[qUNIUnsCPv,mgEBdJLjSKd,oOp234]
crossing=[qUNIUnsCPv,mgEBdJLjSKd,oOp234]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_1_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)