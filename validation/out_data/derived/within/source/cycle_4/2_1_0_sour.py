from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rtll = Factor("rtll", ["weogwb","nflf","zsakwu","hcnt","feyutr","jmepj"])
def thamu(rtll):
    return rtll != "nflf" or rtll == "weogwb"
def rbtfe(rtll):
    return not thamu(rtll)
nejlc = Factor("xwvuae", [DerivedLevel("feozq", WithinTrial(thamu, [rtll])), DerivedLevel("ybvc", WithinTrial(rbtfe, [rtll]))])
### EXPERIMENT
design=[rtll,nejlc]
crossing=[nejlc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)