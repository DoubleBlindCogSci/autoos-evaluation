from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
tyi = Factor("tyi", ["oiz","gqm","tdh","jjlisq","etae"])
def fmmk(tyi):
    return tyi[0] == "gqm" or tyi[-3] != "tdh"
def cbkgab(tyi):
    return tyi[0] != "gqm" and not (tyi[-3] != "tdh")
kdaiwk = Factor("qjd", [DerivedLevel("ydytym", Window(fmmk, [tyi],4)), DerivedLevel("sehsfj", Window(cbkgab, [tyi],4))])
### EXPERIMENT
design=[tyi,kdaiwk]
crossing=[kdaiwk]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/2_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/2_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)