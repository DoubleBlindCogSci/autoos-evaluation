from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
jux = Factor("jux", ["jvpa","oxp","vgfogi","swxoq","xwmy","rceiym","szd"])
def nbz(jux):
    return jux[-3] != "oxp" or jux[-1] != "jvpa"
def sng(jux):
    return not nbz(jux)
fde = DerivedLevel("nct", Window(nbz, [jux],4))
hizs = DerivedLevel("xfgem", Window(sng, [jux],4))
cyh = Factor("koux", [fde, hizs])

### EXPERIMENT
design=[jux,cyh]
crossing=[cyh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0,"levels":False}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)