from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tlahu = Factor("tlahu", ["pgb","xzptv","juvf","kmsmbb","pvas","lbmeii"])
cmjg = Factor("cmjg", ["zxv","nppzc","spwnx","dxqe","uvaiu","cpdcp"])
def urtpsq(tlahu, cmjg):
     return "juvf" == tlahu
def shctx(tlahu, cmjg):
     return tlahu != "juvf" and  cmjg == "nppzc"
def qfeap(tlahu, cmjg):
     return (not tlahu == "juvf") and (cmjg != "nppzc")
qzzovl = Factor("zgmb", [DerivedLevel("punz", WithinTrial(urtpsq, [tlahu, cmjg])), DerivedLevel("ufp", WithinTrial(shctx, [tlahu, cmjg])),DerivedLevel("hzs", WithinTrial(qfeap, [tlahu, cmjg]))])
### EXPERIMENT
design=[tlahu,cmjg,qzzovl]
crossing=[qzzovl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)