from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zbl = Factor("zbl", ["ecmf","kdv","ymd","vpiv","wfcfy"])
jvc = Factor("jvc", ["heic","flb","pgw","nosjfm","mcbage","sdixdv"])
def pseno(zbl, jvc):
    return zbl[0] != "vpiv" and jvc[-1] != "heic"
def zcdfq(zbl,jvc):
    return not pseno(zbl, jvc)
grx = DerivedLevel("scp", Transition(pseno, [zbl, jvc]))
japhbg = DerivedLevel("kelr", Transition(zcdfq, [zbl, jvc]))
adu = Factor("tnq", [grx, japhbg])

### EXPERIMENT
design=[zbl,jvc,adu]
crossing=[adu]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)