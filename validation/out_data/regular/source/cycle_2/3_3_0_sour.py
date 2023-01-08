from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gpvvC7ytisa=Factor("wP!lSU:Jo",[Level('DH0m',1),'HCmbqdwc','LDpdEOjb '])
Lkcc3o=Factor("JGAH",[Level("<lakDe ^]GVW",1),"ZG|yNqHHCj",Level('Ccj6hzwXo',10)])
uqGR=["QzCKug",Level('ausuT5',6),'zHC9vPvYw']
LzjNem9R=Factor("]jInqv9ochDhc",uqGR)

### EXPERIMENT
design=[gpvvC7ytisa,Lkcc3o,LzjNem9R]
crossing=[gpvvC7ytisa,Lkcc3o,LzjNem9R]
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