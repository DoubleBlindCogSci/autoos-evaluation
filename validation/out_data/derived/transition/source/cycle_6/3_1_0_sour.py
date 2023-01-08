from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
coowtg = Factor("coowtg", ["fjqhlw","xxvpye","lduno","uszqsz","ssplw","vzr"])
def qqku(coowtg):
     return coowtg[0] == "vzr" and not coowtg[-1] == "ssplw"
def auj(coowtg):
     return (not "vzr" != coowtg[0]) and  "ssplw" == coowtg[-1]
def bkfa(coowtg):
     return (coowtg[0] != "vzr") and (coowtg[-1] != "ssplw")
xzmw = DerivedLevel("amqeea", Transition(qqku, [coowtg]))
boowgv = DerivedLevel("czmiqp", Transition(auj, [coowtg]))
mktkzw = DerivedLevel("cxhs", Transition(bkfa, [coowtg]))
kdzilh = Factor("takwli", [xzmw, boowgv, mktkzw])

### EXPERIMENT
design=[coowtg,kdzilh]
crossing=[kdzilh]
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