from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ffw = Factor("ffw", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
qce = Factor("qce", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
atrss = Factor("atrss", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
def lgdsy(ffw, qce, atrss):
     return ffw[0] == qce[-2] and ffw[-2] != atrss[0]
def ejngje(ffw, qce, atrss):
     return qce[-2] != ffw[0] and atrss[0] == ffw[-2]
def olufed(ffw, qce, atrss):
     return (not lgdsy(ffw, qce, atrss)) and (not ejngje(ffw, qce, atrss))
rprlew = Factor("sscn", [DerivedLevel("yrewqx", Window(lgdsy, [ffw, qce, atrss],3,1)), DerivedLevel("qsx", Window(ejngje, [ffw, qce, atrss],3,1)),DerivedLevel("uoskx", Window(olufed, [ffw, qce, atrss],3,1))])
### EXPERIMENT
design=[ffw,qce,atrss,rprlew]
crossing=[rprlew]
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