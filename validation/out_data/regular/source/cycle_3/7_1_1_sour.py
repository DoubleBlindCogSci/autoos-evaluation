from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dhOffUy3nl5=[Level("MhCRjDd^B",6),'NaojDFgbY',"f<jFIjM<T:infl"," vfv0b9eIBJ","y3yFXXOdqBN",Level('UqNCR[U',6),'<HK']
BykfIP8d5GH=Factor("HkRppP#AZ",dhOffUy3nl5)

### EXPERIMENT
design=[BykfIP8d5GH]
crossing=[BykfIP8d5GH]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)