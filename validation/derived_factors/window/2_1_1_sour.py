from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ess = Factor("ess", ["iowfse","qez","rir","nusbx","jfbht","adxuko","qxe"])
def rgynhn(ess):
    return ess[-1] != "qez" and ess[-2] != "iowfse"
def skwpvl(ess):
    return ess[-1] == "qez" or not (ess[-2] != "iowfse")
ozaha = DerivedLevel("llat", Window(rgynhn, [ess],3,1))
qfbkan = DerivedLevel("dksrk", Window(skwpvl, [ess],3,1))
hvyd = Factor("wfrxc", [ozaha, qfbkan])

### EXPERIMENT
design=[ess,hvyd]
crossing=[hvyd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)