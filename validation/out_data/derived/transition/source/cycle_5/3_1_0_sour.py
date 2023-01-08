from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hibrnw = Factor("hibrnw", ["ggih","hdhoy","blomac","waxo","zjy","yijm","jphvzw","ouebqa"])
def aamy(hibrnw):
     return hibrnw[0] == "blomac" and not hibrnw[-1] == "hdhoy"
def mmn(hibrnw):
     return (not "blomac" != hibrnw[0]) and  hibrnw[-1] == "hdhoy"
def ibf(hibrnw):
     return (hibrnw[0] != "blomac") and (not mmn(hibrnw))
nndtn = Factor("norzp", [DerivedLevel("ysu", Transition(aamy, [hibrnw])), DerivedLevel("ovfnl", Transition(mmn, [hibrnw])),DerivedLevel("nfyhcz", Transition(ibf, [hibrnw]))])
### EXPERIMENT
design=[hibrnw,nndtn]
crossing=[nndtn]
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