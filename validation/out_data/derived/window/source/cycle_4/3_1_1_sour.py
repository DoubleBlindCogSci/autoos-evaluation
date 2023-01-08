from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pqdejc = Factor("pqdejc", ["yhvz","vumfbe","tavubn","okanp","hoaem","edsktp"])
def rlaxgv(pqdejc):
     return "okanp" == pqdejc[0] and not pqdejc[-2] == "okanp"
def bejfjg(pqdejc):
     return not "okanp" == pqdejc[0] and  "edsktp" == pqdejc[-2]
def lrqw(pqdejc):
     return (not pqdejc[0] == "okanp") and (not bejfjg(pqdejc))
qaift = DerivedLevel("ksm", Window(rlaxgv, [pqdejc],3))
sywlo = DerivedLevel("njg", Window(bejfjg, [pqdejc],3))
uxgs = DerivedLevel("dbkie", Window(lrqw, [pqdejc],3))
davyh = Factor("piqz", [qaift, sywlo, uxgs])

### EXPERIMENT
design=[pqdejc,davyh]
crossing=[davyh]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)