from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ykmc = Factor("ykmc", ["vyle","yuvder","xxf","loup","hyh","fjptm","cgrl"])
okg = Factor("okg", ["lthe","oeru","pjzss","xtdg","mvmk","afop","pxg"])
def lee(ykmc, okg):
     return ykmc == "cgrl"
def mpk(ykmc, okg):
     return ykmc != "cgrl" and  okg == "lthe"
def tpxxht(ykmc, okg):
     return (not ykmc == "cgrl") and (okg != "lthe")
upfgtt = DerivedLevel("pxocro", WithinTrial(lee, [ykmc, okg]))
fsgc = DerivedLevel("xoqhut", WithinTrial(mpk, [ykmc, okg]))
hsezs = DerivedLevel("jgz", WithinTrial(tpxxht, [ykmc, okg]))
jghal = Factor("ncv", [upfgtt, fsgc, hsezs])

### EXPERIMENT
design=[ykmc,okg,jghal]
crossing=[jghal]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)