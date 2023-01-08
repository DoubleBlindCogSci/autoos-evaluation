from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mfkaxd = Factor("mfkaxd", ["bzoi","gfuv","uxog","icyubf","hahmv","uwon","pqrz"])
def tfbjvk(mfkaxd):
     return "bzoi" == mfkaxd
def oigiql(mfkaxd):
     return mfkaxd == "gfuv"
def xzojg(mfkaxd):
     return (mfkaxd != "bzoi") and (mfkaxd != "gfuv")
simnd = DerivedLevel("mrgo", WithinTrial(tfbjvk, [mfkaxd]))
uoqu = DerivedLevel("xbs", WithinTrial(oigiql, [mfkaxd]))
tbtdl = DerivedLevel("kndaqf", WithinTrial(xzojg, [mfkaxd]))
acshw = Factor("pebbqo", [simnd, uoqu, tbtdl])

### EXPERIMENT
design=[mfkaxd,acshw]
crossing=[acshw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)