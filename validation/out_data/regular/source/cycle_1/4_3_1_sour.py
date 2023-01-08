from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eEdlu=[Level("iZEiP",4),';it',Level('ez[RDJxx',4),Level("giO",3)]
h2WU=Factor("xY0YmMZJTM",eEdlu)
ImiLA3j=[Level("kYRAC",5),"byE","nrdAgsrbp","ZgS"]
UiHYnXHUL8=Factor('ijn&HvqnYiIX6*',ImiLA3j)
ADrcBefC=['GBBDPF{','1qrc}SDy','WwjzBxQ:LoX>*',Level('MDgDiSdRJAJcMW',2)]
jsGfZlD3U4=Factor("CgcZmD&XulWR",ADrcBefC)

### EXPERIMENT
design=[h2WU,UiHYnXHUL8,jsGfZlD3U4]
crossing=[h2WU,UiHYnXHUL8,jsGfZlD3U4]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_3_1_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)