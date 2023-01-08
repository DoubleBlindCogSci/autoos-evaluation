from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ngavjj = Factor("ngavjj", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
umnwpc = Factor("umnwpc", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
kibvon = Factor("kibvon", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
def piwi(ngavjj, kibvon, umnwpc):
     return kibvon == ngavjj
def tbrv(ngavjj, kibvon, umnwpc):
     return kibvon != ngavjj and ngavjj == umnwpc
def bhoiqy(ngavjj, kibvon, umnwpc):
     return (not piwi(ngavjj, kibvon, umnwpc)) and (not tbrv(ngavjj, kibvon, umnwpc))
zfb = DerivedLevel("hysx", WithinTrial(piwi, [ngavjj, umnwpc, kibvon]))
axej = DerivedLevel("gmaul", WithinTrial(tbrv, [ngavjj, umnwpc, kibvon]))
fvpdcn = DerivedLevel("vipame", WithinTrial(bhoiqy, [ngavjj, umnwpc, kibvon]))
mnx = Factor("egudg", [zfb, axej, fvpdcn])

### EXPERIMENT
design=[ngavjj,umnwpc,kibvon,mnx]
crossing=[mnx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)