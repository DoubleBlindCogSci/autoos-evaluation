from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jvsf = Factor("jvsf", ["kivh","kqagto","zqksk","xae","twyc","epq","rtxaw"])
def set(jvsf):
     return "xae" == jvsf[0] and jvsf[-1] != "rtxaw"
def hpgt(jvsf):
     return (jvsf[0] != "xae") and  jvsf[-1] == "rtxaw"
def qai(jvsf):
     return (not jvsf[0] == "xae") and (not jvsf[-1] == "rtxaw")
jguq = DerivedLevel("tngyia", Transition(set, [jvsf]))
gweb = DerivedLevel("gemffy", Transition(hpgt, [jvsf]))
cbqulv = DerivedLevel("sspc", Transition(qai, [jvsf]))
wvqnfc = Factor("nfx", [jguq, gweb, cbqulv])

### EXPERIMENT
design=[jvsf,wvqnfc]
crossing=[wvqnfc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)