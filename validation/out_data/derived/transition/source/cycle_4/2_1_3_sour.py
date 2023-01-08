from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jvd = Factor("jvd", ["qlov","feiuit","jsy","grr","eewt","ajb","ioroa"])
def mryd(jvd):
    return jvd[0] != "ajb" or jvd[-1] != "grr"
def vfynz(jvd):
    return not (jvd[0] != "ajb") and jvd[-1] == "grr"
yzrh = Factor("kxcewo", [DerivedLevel("occdnc", Transition(mryd, [jvd])), DerivedLevel("toqqq", Transition(vfynz, [jvd]))])
### EXPERIMENT
design=[jvd,yzrh]
crossing=[yzrh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)