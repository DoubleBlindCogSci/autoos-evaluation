from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zdbxi = Factor("zdbxi", ["hcj","pnqr","edln","jtizo","kueg","vid","wzchdg"])
def plwzsb(zdbxi):
     return "pnqr" == zdbxi[-1] and not zdbxi[0] == "pnqr"
def pad(zdbxi):
     return zdbxi[-1] != "pnqr" and  zdbxi[0] == "edln"
def pjbx(zdbxi):
     return (not zdbxi[-1] == "pnqr") and (not pad(zdbxi))
inf = Factor("mfnjeh", [DerivedLevel("nud", Window(plwzsb, [zdbxi],2)), DerivedLevel("uah", Window(pad, [zdbxi],2)),DerivedLevel("ugi", Window(pjbx, [zdbxi],2))])
### EXPERIMENT
design=[zdbxi,inf]
crossing=[inf]
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