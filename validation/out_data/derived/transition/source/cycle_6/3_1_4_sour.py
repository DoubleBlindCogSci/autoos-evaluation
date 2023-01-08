from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
axxxy = Factor("axxxy", ["gwlfl","hgte","nms","norqt","vxrjpm","dpvh"])
def bolf(axxxy):
     return "vxrjpm" == axxxy[0] and not axxxy[-1] == "hgte"
def jmvcxp(axxxy):
     return (axxxy[0] != "vxrjpm") and  "hgte" == axxxy[-1]
def pox(axxxy):
     return (axxxy[0] != "vxrjpm") and (not jmvcxp(axxxy))
dzqjyv = Factor("dirfp", [DerivedLevel("ksw", Transition(bolf, [axxxy])), DerivedLevel("sjt", Transition(jmvcxp, [axxxy])),DerivedLevel("flwqk", Transition(pox, [axxxy]))])
### EXPERIMENT
design=[axxxy,dzqjyv]
crossing=[dzqjyv]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)