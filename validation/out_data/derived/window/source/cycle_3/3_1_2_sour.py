from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
roi = Factor("roi", ["bgydaq","lgvbd","oyrlk","fdzye","pbyu","sdnyy","tcgzw","yvilsd"])
def jjbzm(roi):
     return "fdzye" == roi[0] and not roi[-3] == "fdzye"
def myfde(roi):
     return roi[0] != "fdzye" and  roi[-3] == "lgvbd"
def xhr(roi):
     return (roi[0] != "fdzye") and (not myfde(roi))
hmi = Factor("gfws", [DerivedLevel("unzl", Window(jjbzm, [roi],4)), DerivedLevel("wugp", Window(myfde, [roi],4)),DerivedLevel("quuxfe", Window(xhr, [roi],4))])
### EXPERIMENT
design=[roi,hmi]
crossing=[hmi]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)