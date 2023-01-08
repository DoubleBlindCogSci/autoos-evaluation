from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tnrF='s^ryhRRE@v'
wsJ44aXInZ_=Factor('klWxvR',['isc2IlmXIX',"JLcUIfY","cDlenobc",Level(';Az',9),tnrF,'B~L@$',"f^Ty",Level("JcbwJCsZt",1),'@bMmDp!x',"SScdTo5n#Edad"])

### EXPERIMENT
design=[wsJ44aXInZ_]
crossing=[wsJ44aXInZ_]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/9_1_0_0.csv"))
nr_factors=1
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/9_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)