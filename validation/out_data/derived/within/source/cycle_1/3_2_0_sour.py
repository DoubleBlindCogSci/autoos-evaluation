from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
tghaa = Factor("tghaa", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
bbxa = Factor("bbxa", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
yzpsqo = Factor("yzpsqo", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
def zyv(tghaa, yzpsqo, bbxa):
     return yzpsqo == tghaa
def ukg(tghaa, yzpsqo, bbxa):
     return yzpsqo != tghaa and bbxa == tghaa
def oscft(tghaa, yzpsqo, bbxa):
     return (tghaa != yzpsqo) and (not tghaa == bbxa)
oigxjk = Factor("yemznk", [DerivedLevel("bjpwk", WithinTrial(zyv, [tghaa, bbxa, yzpsqo])), DerivedLevel("nzvgd", WithinTrial(ukg, [tghaa, bbxa, yzpsqo])),DerivedLevel("pnkcuy", WithinTrial(oscft, [tghaa, bbxa, yzpsqo]))])
### EXPERIMENT
design=[tghaa,bbxa,yzpsqo,oigxjk]
crossing=[oigxjk]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)