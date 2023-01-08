from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EjMnRIlyZSV=Level('YIoWsLN',6)
b89AVX=Factor("V)rCn:i",["mi&bhLRWS_oq",'M0w$eOVYzN','VNcDo:','teELYLSUURC','opcmuQk!DQ4qfy','aDVr','YanpeBDa',EjMnRIlyZSV])
S1p4zPbBYsA=Factor("PHfFDjTYNlH",["_WteHj",'MnE<WDU',"rQgD?WwvdIdM;",'SURrRd]cbI',Level('VVdSAjDlrWE|',1),"LBMxX{W>H",Level('YhR_pthuX7Q',10)])

### EXPERIMENT
design=[b89AVX,S1p4zPbBYsA]
crossing=[b89AVX,S1p4zPbBYsA]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_2_0_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)