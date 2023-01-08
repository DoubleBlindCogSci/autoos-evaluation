from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vsxv = Factor("vsxv", ["drgme","mkvx","lgzcfj","bmgf","fnoe","fzsngf","thvsaa"])
def zyj(vsxv):
    return vsxv[0] != "mkvx" or vsxv[-1] == "drgme"
def fmec(vsxv):
    return not (vsxv[0] != "mkvx") and not (vsxv[0] == "drgme")
ywuu = DerivedLevel("gtz", Transition(zyj, [vsxv]))
fwis = DerivedLevel("xdnx", Transition(fmec, [vsxv]))
gyikro = Factor("yasz", [ywuu, fwis])

### EXPERIMENT
design=[vsxv,gyikro]
crossing=[gyikro]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)