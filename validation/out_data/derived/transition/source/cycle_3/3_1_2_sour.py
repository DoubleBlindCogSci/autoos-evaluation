from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rlfgp = Factor("rlfgp", ["uwwu","nnviqh","adovs","lkq","ngeuv","fweki","zofa","nmu"])
def okoqlj(rlfgp):
     return "lkq" == rlfgp[0] and rlfgp[-1] != "fweki"
def iyheoe(rlfgp):
     return (not "lkq" != rlfgp[0]) and  "fweki" == rlfgp[-1]
def kew(rlfgp):
     return (not okoqlj(rlfgp)) and (rlfgp[-1] != "fweki")
qlx = Factor("lgjokh", [DerivedLevel("hhxn", Transition(okoqlj, [rlfgp])), DerivedLevel("nlh", Transition(iyheoe, [rlfgp])),DerivedLevel("tyuxva", Transition(kew, [rlfgp]))])
### EXPERIMENT
design=[rlfgp,qlx]
crossing=[qlx]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)