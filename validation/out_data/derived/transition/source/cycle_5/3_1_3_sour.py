from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tglvmx = Factor("tglvmx", ["tkon","nzbpe","eyjenc","fkjtmj","pulu","uls","hkfa"])
def eszjnf(tglvmx):
     return "pulu" == tglvmx[0] and not tglvmx[-1] == "tkon"
def ejrf(tglvmx):
     return (not "pulu" != tglvmx[0]) and  "tkon" == tglvmx[-1]
def cter(tglvmx):
     return (not eszjnf(tglvmx)) and (not ejrf(tglvmx))
evjw = Factor("brbmt", [DerivedLevel("prtnf", Transition(eszjnf, [tglvmx])), DerivedLevel("racrn", Transition(ejrf, [tglvmx])),DerivedLevel("olao", Transition(cter, [tglvmx]))])
### EXPERIMENT
design=[tglvmx,evjw]
crossing=[evjw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)