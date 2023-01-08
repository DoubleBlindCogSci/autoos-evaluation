from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
exii = Factor("exii", ["fxb","ynmp","repr","znltjq","qsjul","irdbw"])
def pjri(exii):
    return exii[0] != "repr" and exii[-1] != "irdbw"
def ktv(exii):
    return not pjri(exii)
tbupwj = DerivedLevel("bsjhjv", Transition(pjri, [exii]))
hfuxyl = DerivedLevel("yaqd", Transition(ktv, [exii]))
jwjmf = Factor("ujsa", [tbupwj, hfuxyl])

### EXPERIMENT
design=[exii,jwjmf]
crossing=[jwjmf]
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