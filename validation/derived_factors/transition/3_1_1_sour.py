from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bid = Factor("bid", ["bmwjyr","ophcsg","vltrhp","nmsmxy","ttssnv","nqhf","jxebnk"])
def onqpm(bid):
     return "ttssnv" == bid[0] and not bid[-1] == "nqhf"
def hfx(bid):
     return (not "ttssnv" != bid[0]) and  "nqhf" == bid[-1]
def tvqpn(bid):
     return (not onqpm(bid)) and (not bid[-1] == "nqhf")
dycye = DerivedLevel("cbnphq", Transition(onqpm, [bid]))
nohcz = DerivedLevel("xbl", Transition(hfx, [bid]))
cutn = DerivedLevel("oftp", Transition(tvqpn, [bid]))
jkak = Factor("abmuxe", [dycye, nohcz, cutn])

### EXPERIMENT
design=[bid,jkak]
crossing=[jkak]
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