from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zlm = Factor("zlm", ["zsj","ppg","wmzkcc","rfzzdx","ckmar","tmvzzn","isjyzz","fmu"])
enchxy = Factor("enchxy", ["iyhq","eqdxln","pqrqji","blu","pjccrq","dfejzk","kgz"])
def oexpc(zlm, enchxy):
     return "ppg" == zlm
def dgthhw(zlm, enchxy):
     return zlm != "ppg" and  enchxy == "iyhq"
def qpufhh(zlm, enchxy):
     return (not oexpc(zlm, enchxy)) and (enchxy != "iyhq")
gllguo = Factor("qkc", [DerivedLevel("dok", WithinTrial(oexpc, [zlm, enchxy])), DerivedLevel("uyctch", WithinTrial(dgthhw, [zlm, enchxy])),DerivedLevel("ypuao", WithinTrial(qpufhh, [zlm, enchxy]))])
### EXPERIMENT
design=[zlm,enchxy,gllguo]
crossing=[gllguo]
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