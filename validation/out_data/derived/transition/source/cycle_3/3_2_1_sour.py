from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
blfi = Factor("blfi", ["xrnn","rlkzh","npeot","csob","aivye","poogo","hmoz","ptqeqs"])
rqnon = Factor("rqnon", ["ekaq","yonm","nhq","dtojhe","xjijq","cww","cuwi"])
def imxkzh(blfi, rqnon):
     return blfi[-1] == "poogo" and rqnon[0] != "cuwi"
def dbw(blfi, rqnon):
     return "poogo" != blfi[-1] and rqnon[0] == "cuwi"
def gfxk(blfi, rqnon):
     return (not blfi[-1] == "poogo") and (rqnon[0] != "cuwi")
qki = DerivedLevel("uqln", Transition(imxkzh, [blfi, rqnon]))
fnugz = DerivedLevel("lydag", Transition(dbw, [blfi, rqnon]))
dckg = DerivedLevel("enmxhf", Transition(gfxk, [blfi, rqnon]))
ckx = Factor("aqw", [qki, fnugz, dckg])

### EXPERIMENT
design=[blfi,rqnon,ckx]
crossing=[ckx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)