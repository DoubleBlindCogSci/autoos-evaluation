from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xczrq = Factor("xczrq", ["doby","xtplr","zfv","echghq","esnx","xhfanc","hune"])
def kkzwc(xczrq):
    return xczrq != "zfv"
def glfw(xczrq):
    return not kkzwc(xczrq)
rya = DerivedLevel("njy", WithinTrial(kkzwc, [xczrq]))
gln = DerivedLevel("bqgh", WithinTrial(glfw, [xczrq]))
syzk = Factor("rmg", [rya, gln])

### EXPERIMENT
design=[xczrq,syzk]
crossing=[syzk]
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