from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vsro = Factor("vsro", ["gloon","eqoo","vuu","kquio","wun","afivz"])
def dlf(vsro):
     return "kquio" == vsro
def addpu(vsro):
     return "wun" == vsro
def izxzxt(vsro):
     return (not dlf(vsro)) and (not vsro == "wun")
ysab = DerivedLevel("gjctkf", WithinTrial(dlf, [vsro]))
wvzpq = DerivedLevel("jshfbz", WithinTrial(addpu, [vsro]))
jyadpw = DerivedLevel("jhcmef", WithinTrial(izxzxt, [vsro]))
xvfcd = Factor("giq", [ysab, wvzpq, jyadpw])

### EXPERIMENT
design=[vsro,xvfcd]
crossing=[xvfcd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)