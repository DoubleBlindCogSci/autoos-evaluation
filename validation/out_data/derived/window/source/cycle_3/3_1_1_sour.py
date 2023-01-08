from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
med = Factor("med", ["zjbe","enhw","zzeiq","ngeen","tyu","blz","khy","fbcolf"])
def owukbh(med):
     return med[-2] == "fbcolf" and not med[-1] == "fbcolf"
def rckxpt(med):
     return med[-2] != "fbcolf" and  med[-1] == "enhw"
def wnbb(med):
     return (med[-2] != "fbcolf") and (not rckxpt(med))
gfvg = Factor("bxt", [DerivedLevel("hurev", Window(owukbh, [med],3)), DerivedLevel("axe", Window(rckxpt, [med],3)),DerivedLevel("tuaxow", Window(wnbb, [med],3))])
### EXPERIMENT
design=[med,gfvg]
crossing=[gfvg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)