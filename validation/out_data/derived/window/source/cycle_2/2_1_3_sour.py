from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
elfx = Factor("elfx", ["zbydej","bpqtrb","vxtnpa","xfhmhy","qpilm","fzj"])
def ejony(elfx):
    return elfx[-1] == "vxtnpa" and elfx[-3] != "qpilm"
def rld(elfx):
    return elfx[-1] != "vxtnpa" or elfx[-3] == "qpilm"
kmgcl = Factor("ypqk", [DerivedLevel("mxonf", Window(ejony, [elfx],4)), DerivedLevel("dhoai", Window(rld, [elfx],4))])
### EXPERIMENT
design=[elfx,kmgcl]
crossing=[kmgcl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)