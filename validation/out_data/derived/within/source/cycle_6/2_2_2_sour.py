from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fcq = Factor("fcq", ["dkah","igk","nreq","ryc","szko"])
czust = Factor("czust", ["yddp","rdu","eiolg","ekwa","rkq"])
def host(fcq, czust):
    return fcq != "igk" or czust == "rdu"
def rqed(fcq,czust):
    return not (fcq != "igk") and not (czust == "rdu")
ychtqz = Factor("dvzlc", [DerivedLevel("rnqt", WithinTrial(host, [fcq, czust])), DerivedLevel("cijg", WithinTrial(rqed, [fcq, czust]))])
### EXPERIMENT
design=[fcq,czust,ychtqz]
crossing=[ychtqz]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)