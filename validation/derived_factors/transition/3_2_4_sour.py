from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
blorw = Factor("blorw", ["xkag","hyvlqh","vjh","txlvm","pexht","qef"])
aqsrs = Factor("aqsrs", ["dhil","wvzi","xsgh","sosn","cmyn","dhjkgj"])
def htau(blorw, aqsrs):
     return "vjh" == blorw[-1] and not aqsrs[0] == "xsgh"
def sjajnv(blorw, aqsrs):
     return blorw[-1] != "vjh" and aqsrs[0] == "xsgh"
def yzxb(blorw, aqsrs):
     return (not blorw[-1] == "vjh") and (not aqsrs[0] == "xsgh")
gln = Factor("uih", [DerivedLevel("mpk", Transition(htau, [blorw, aqsrs])), DerivedLevel("ihdfm", Transition(sjajnv, [blorw, aqsrs])),DerivedLevel("rjozpb", Transition(yzxb, [blorw, aqsrs]))])
### EXPERIMENT
design=[blorw,aqsrs,gln]
crossing=[gln]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)