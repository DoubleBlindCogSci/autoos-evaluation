from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gux = Factor("gux", ["mqb","bimndj","gwta","mgd","fttjig","fwe","hhn","juqlf"])
def qlces(gux):
     return gux[0] == "fwe" and gux[-1] != "gwta"
def qkyq(gux):
     return (gux[0] != "fwe") and  gux[-1] == "gwta"
def fktf(gux):
     return (not gux[0] == "fwe") and (not qkyq(gux))
jetni = Factor("uakm", [DerivedLevel("prbuti", Transition(qlces, [gux])), DerivedLevel("gstiro", Transition(qkyq, [gux])),DerivedLevel("wjb", Transition(fktf, [gux]))])
### EXPERIMENT
design=[gux,jetni]
crossing=[jetni]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)