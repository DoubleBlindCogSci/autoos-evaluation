from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nzl = Factor("nzl", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
xmiax = Factor("xmiax", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
vtzuv = Factor("vtzuv", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
def eosems(nzl, vtzuv, xmiax):
    return nzl[0] != vtzuv[-1] or nzl[-1] != xmiax[0]
def wjm(nzl, vtzuv, xmiax):
    return not (nzl[0] != vtzuv[-1]) and nzl[-1] == xmiax[0]
ynazla = Factor("sealv", [DerivedLevel("hpwaa", Transition(eosems, [nzl, xmiax, vtzuv])), DerivedLevel("sryzex", Transition(wjm, [nzl, xmiax, vtzuv]))])
### EXPERIMENT
design=[nzl,xmiax,vtzuv,ynazla]
crossing=[ynazla]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)