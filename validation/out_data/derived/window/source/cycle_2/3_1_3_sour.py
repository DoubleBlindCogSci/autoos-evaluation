from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
mcfe = Factor("mcfe", ["cjd","pdhx","gxwuy","kwmu","jjuu","pzqea","llbj"])
def krwuj(mcfe):
     return mcfe[-3] == "jjuu" and not mcfe[0] == "jjuu"
def spwdju(mcfe):
     return mcfe[-3] != "jjuu" and  mcfe[0] == "cjd"
def bix(mcfe):
     return (not mcfe[-3] == "jjuu") and (mcfe[0] != "cjd")
unki = Factor("ewfej", [DerivedLevel("jozju", Window(krwuj, [mcfe],4)), DerivedLevel("tozb", Window(spwdju, [mcfe],4)),DerivedLevel("qpbcog", Window(bix, [mcfe],4))])
### EXPERIMENT
design=[mcfe,unki]
crossing=[unki]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)