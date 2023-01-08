from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jlb = Factor("jlb", ["gyy","aklr","vsgh","vmokyj","rwhz","husnen"])
def pvjsxg(jlb):
    return jlb[-1] != "vmokyj" or jlb[0] == "aklr"
def lfw(jlb):
    return not pvjsxg(jlb)
lfxoom = Factor("cyt", [DerivedLevel("jklom", Window(pvjsxg, [jlb],2)), DerivedLevel("kkkge", Window(lfw, [jlb],2))])
### EXPERIMENT
design=[jlb,lfxoom]
crossing=[lfxoom]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)