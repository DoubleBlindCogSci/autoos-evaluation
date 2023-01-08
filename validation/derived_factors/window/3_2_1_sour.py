from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hmi = Factor("hmi", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
pkyoho = Factor("pkyoho", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
efzpc = Factor("efzpc", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
def fjpq(hmi, pkyoho, efzpc):
     return pkyoho[0] == hmi[-1] and hmi[0] != efzpc[-1]
def bfx(hmi, pkyoho, efzpc):
     return pkyoho[0] != hmi[-1] and efzpc[-1] == hmi[0]
def cqsitt(hmi, pkyoho, efzpc):
     return (not hmi[-1] == pkyoho[0]) and (not bfx(hmi, pkyoho, efzpc))
nclfg = Factor("abobi", [DerivedLevel("zebmpm", Window(fjpq, [hmi, pkyoho, efzpc],2,1)), DerivedLevel("ury", Window(bfx, [hmi, pkyoho, efzpc],2,1)),DerivedLevel("ljy", Window(cqsitt, [hmi, pkyoho, efzpc],2,1))])
### EXPERIMENT
design=[hmi,pkyoho,efzpc,nclfg]
crossing=[nclfg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)