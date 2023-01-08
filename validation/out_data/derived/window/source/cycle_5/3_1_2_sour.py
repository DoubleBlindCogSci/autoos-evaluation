from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ffp = Factor("ffp", ["fmie","buekwg","cybl","evsdjz","inxtj","rbc"])
def mtdqud(ffp):
     return "rbc" == ffp[-2] and not ffp[-1] == "rbc"
def zbu(ffp):
     return ffp[-2] != "rbc" and  ffp[-1] == "buekwg"
def eap(ffp):
     return (ffp[-2] != "rbc") and (not ffp[-1] == "buekwg")
djaq = DerivedLevel("ydoqi", Window(mtdqud, [ffp],3))
ulcv = DerivedLevel("qsap", Window(zbu, [ffp],3))
xtbi = DerivedLevel("vgta", Window(eap, [ffp],3))
elrio = Factor("pug", [djaq, ulcv, xtbi])

### EXPERIMENT
design=[ffp,elrio]
crossing=[elrio]
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