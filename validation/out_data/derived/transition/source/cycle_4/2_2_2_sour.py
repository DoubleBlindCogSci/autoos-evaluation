from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
shdi = Factor("shdi", ["yetkbx","qdkggy","zsrvfd","lsz","iomwsu","spxtfk"])
zbahnb = Factor("zbahnb", ["hzzgg","fttwj","gvlyd","dfhilo","oggzmn","acli","xfifs"])
def kjm(shdi, zbahnb):
    return shdi[0] != "zsrvfd" and zbahnb[-1] != "fttwj"
def adc(shdi,zbahnb):
    return not (shdi[0] != "zsrvfd") or zbahnb[-1] == "fttwj"
ccmh = DerivedLevel("xtnum", Transition(kjm, [shdi, zbahnb]))
mod = DerivedLevel("pop", Transition(adc, [shdi, zbahnb]))
zrhi = Factor("dpnj", [ccmh, mod])

### EXPERIMENT
design=[shdi,zbahnb,zrhi]
crossing=[zrhi]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)