from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
E6fSw=Factor("m&PHyvQ",[Level('i#D)yTu3P',5),Level('lvIY:P?MB',6),Level('DZsh',1)])
e5xtj=['PFYD5','FtU<PsDEEGvBN<',Level("*RO6qw$lFxs",4)]
XUBHar4zpyg=Factor('vVp b',e5xtj)
Di1NB=Factor("pzr[XuysBLwLxh",[Level('VxaIv:XbDfJ',1),'sAfRl',Level('#8zqe',10)])

### EXPERIMENT
design=[E6fSw,XUBHar4zpyg,Di1NB]
crossing=[E6fSw,XUBHar4zpyg,Di1NB]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_3_0_0.csv"))
nr_factors=3
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)