from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
imgt = Factor("imgt", ["auik","ykvp","cnzw","ynk","cuzq","fwhui","rcuu","cdjwaz"])
ffi = Factor("ffi", ["sqx","dzsh","vgg","qnoc","pwdesb","wpsnra","nmsxqv","mbn"])
def vtmur(imgt, ffi):
     return "rcuu" == imgt[-1] and not ffi[0] == "mbn"
def ylup(imgt, ffi):
     return imgt[-1] != "rcuu" and ffi[0] == "mbn"
def yvtq(imgt, ffi):
     return (imgt[-1] != "rcuu") and (not ffi[0] == "mbn")
ryor = Factor("sfhdj", [DerivedLevel("kssc", Transition(vtmur, [imgt, ffi])), DerivedLevel("zaui", Transition(ylup, [imgt, ffi])),DerivedLevel("nqwa", Transition(yvtq, [imgt, ffi]))])
### EXPERIMENT
design=[imgt,ffi,ryor]
crossing=[ryor]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)