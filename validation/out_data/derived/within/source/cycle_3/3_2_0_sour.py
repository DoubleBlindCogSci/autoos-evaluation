from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
johhmd = Factor("johhmd", ["yohuh","cyvo","tyagv","onjrj","srbbj","trip","bjozvy"])
uujh = Factor("uujh", ["klxyf","jppce","tayjhy","awitqq","hyvn","sgbw","ejtfc"])
def eplv(johhmd, uujh):
     return johhmd == "srbbj"
def akkgpb(johhmd, uujh):
     return "srbbj" != johhmd and  uujh == "hyvn"
def tmaoj(johhmd, uujh):
     return (not eplv(johhmd, uujh)) and (not uujh == "hyvn")
fzl = Factor("pttdar", [DerivedLevel("yvu", WithinTrial(eplv, [johhmd, uujh])), DerivedLevel("wnxvg", WithinTrial(akkgpb, [johhmd, uujh])),DerivedLevel("wevh", WithinTrial(tmaoj, [johhmd, uujh]))])
### EXPERIMENT
design=[johhmd,uujh,fzl]
crossing=[fzl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)