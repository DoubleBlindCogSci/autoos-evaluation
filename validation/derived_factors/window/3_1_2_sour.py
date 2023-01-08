from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kwkk = Factor("kwkk", ["mcsefi","fhnn","jpyv","ayyi","gbg","jdj"])
def iqofzy(kwkk):
     return "gbg" == kwkk[-1] and not kwkk[0] == "gbg"
def wbhcm(kwkk):
     return not "gbg" == kwkk[-1] and  kwkk[0] == "jpyv"
def qavbns(kwkk):
     return (not iqofzy(kwkk)) and (kwkk[0] != "jpyv")
mgapxw = Factor("rdr", [DerivedLevel("mietsj", Window(iqofzy, [kwkk],2,1)), DerivedLevel("bevmb", Window(wbhcm, [kwkk],2,1)),DerivedLevel("mtl", Window(qavbns, [kwkk],2,1))])
### EXPERIMENT
design=[kwkk,mgapxw]
crossing=[mgapxw]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)