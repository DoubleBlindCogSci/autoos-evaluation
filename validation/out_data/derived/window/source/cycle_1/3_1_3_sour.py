from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
tqywwe = Factor("tqywwe", ["jep","givaf","dshe","hvdbkc","antde","mqan","ceb"])
def uhmcb(tqywwe):
     return "dshe" == tqywwe[-1]
def jeop(tqywwe):
     return "givaf" == tqywwe[-2]
def mko(tqywwe):
     return (not tqywwe[-1] == "dshe") and (not tqywwe[-2] == "givaf")
kay = Factor("xcic", [DerivedLevel("lfli", Window(uhmcb, [tqywwe],3)), DerivedLevel("fovsd", Window(jeop, [tqywwe],3)),DerivedLevel("sfo", Window(mko, [tqywwe],3))])
### EXPERIMENT
design=[tqywwe,kay]
crossing=[kay]
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
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)