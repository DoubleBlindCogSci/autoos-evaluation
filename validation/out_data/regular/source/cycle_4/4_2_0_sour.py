from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ca2aioVc=Factor('mBCPXKa',['HSAu~','%yzX2{Wok',"TsplnW",'w;tTlmI{N'])
kcZdf=Factor("eMCNJAW",['eHvr@zz4','oZD',Level("cBUXvvi",1),"mclh3qMXRjkzoi"])

### EXPERIMENT
design=[ca2aioVc,kcZdf]
crossing=[ca2aioVc,kcZdf]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)