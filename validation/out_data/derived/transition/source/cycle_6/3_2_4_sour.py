from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wnjfo = Factor("wnjfo", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
ydczl = Factor("ydczl", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
ezw = Factor("ezw", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
def aun(wnjfo, ydczl, ezw):
     return ydczl[-1] == wnjfo[0] and wnjfo[-1] != ezw[0]
def ulh(wnjfo, ydczl, ezw):
     return ydczl[-1] != wnjfo[0] and wnjfo[-1] == ezw[0]
def gqi(wnjfo, ydczl, ezw):
     return (not wnjfo[0] == ydczl[-1]) and (wnjfo[-1] != ezw[0])
vahh = Factor("gaovt", [DerivedLevel("wpyds", Transition(aun, [wnjfo, ydczl, ezw])), DerivedLevel("hjm", Transition(ulh, [wnjfo, ydczl, ezw])),DerivedLevel("iiyv", Transition(gqi, [wnjfo, ydczl, ezw]))])
### EXPERIMENT
design=[wnjfo,ydczl,ezw,vahh]
crossing=[vahh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)