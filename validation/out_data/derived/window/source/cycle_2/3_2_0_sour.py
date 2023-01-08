from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
tjqjy = Factor("tjqjy", ["ezrg","lxhb","spwqj","nigrt","hhzjy","eocn"])
tclqkw = Factor("tclqkw", ["scals","ndjw","rxa","hig","qwlv","svyx","ogwjy"])
def jyu(tjqjy, tclqkw):
     return tjqjy[-1] == "lxhb" and tclqkw[-2] != "scals"
def xbf(tjqjy, tclqkw):
     return tjqjy[-1] != "lxhb" and  tclqkw[-2] == "scals"
def lmxyos(tjqjy, tclqkw):
     return (not jyu(tjqjy, tclqkw)) and (not xbf(tjqjy, tclqkw))
svxuq = DerivedLevel("dkytkh", Window(jyu, [tjqjy, tclqkw],3))
jwvj = DerivedLevel("vfz", Window(xbf, [tjqjy, tclqkw],3))
jncp = DerivedLevel("hizcf", Window(lmxyos, [tjqjy, tclqkw],3))
dxgiew = Factor("otzpw", [svxuq, jwvj, jncp])

### EXPERIMENT
design=[tjqjy,tclqkw,dxgiew]
crossing=[dxgiew]
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