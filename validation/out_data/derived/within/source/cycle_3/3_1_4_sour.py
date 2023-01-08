from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
suhen = Factor("suhen", ["krpr","ufomf","nypxj","ezhsn","cjidu","jkpx","mhdkzw","bzj"])
def kammmt(suhen):
     return "ezhsn" == suhen
def yvo(suhen):
     return suhen == "cjidu"
def eydyd(suhen):
     return (not suhen == "ezhsn") and (suhen != "cjidu")
zfz = Factor("vuff", [DerivedLevel("pfj", WithinTrial(kammmt, [suhen])), DerivedLevel("wdgbc", WithinTrial(yvo, [suhen])),DerivedLevel("vnmvgi", WithinTrial(eydyd, [suhen]))])
### EXPERIMENT
design=[suhen,zfz]
crossing=[zfz]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)