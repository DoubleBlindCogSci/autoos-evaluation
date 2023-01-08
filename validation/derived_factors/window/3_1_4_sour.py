from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sgy = Factor("sgy", ["duftv","uao","elyd","nuvgkv","jdfnj","otnfn","bvjut","xdk"])
def vjyezz(sgy):
     return sgy[-2] == "elyd" and not sgy[0] == "elyd"
def poa(sgy):
     return not "elyd" == sgy[-2] and  "xdk" == sgy[0]
def mmw(sgy):
     return (sgy[-2] != "elyd") and (not sgy[0] == "xdk")
mhino = Factor("lav", [DerivedLevel("kllu", Window(vjyezz, [sgy],3,1)), DerivedLevel("ebjemp", Window(poa, [sgy],3,1)),DerivedLevel("dzrxzk", Window(mmw, [sgy],3,1))])
### EXPERIMENT
design=[sgy,mhino]
crossing=[mhino]
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