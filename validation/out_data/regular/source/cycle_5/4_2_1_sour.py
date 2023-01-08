from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
o5TUnA=Factor('jrBPlmfLSpWsF',[Level("se?IrKzJrDI",3),"i1X","K5OVr>{:~b|>k","eFC"])
bQbC9w0riF=Factor('FXN',["K>bb7Z7B","JzEhZ",'ZyGndX~hiq',Level('!eTCyRRlSjR4d',3)])

### EXPERIMENT
design=[o5TUnA,bQbC9w0riF]
crossing=[o5TUnA,bQbC9w0riF]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_1_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)