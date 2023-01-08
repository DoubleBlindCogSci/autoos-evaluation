from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
tprnu = Factor("tprnu", ["aot","aqp","eldx","bsxt","lklq","xkjq","hnt"])
def uvgzin(tprnu):
     return "xkjq" == tprnu[0]
def ymhc(tprnu):
     return "bsxt" == tprnu[-1]
def eurgqp(tprnu):
     return (not uvgzin(tprnu)) and (not tprnu[-1] == "bsxt")
zphx = DerivedLevel("ngmg", Window(uvgzin, [tprnu],2))
tvbwf = DerivedLevel("jvk", Window(ymhc, [tprnu],2))
dwruc = DerivedLevel("jrldp", Window(eurgqp, [tprnu],2))
milyfd = Factor("shrv", [zphx, tvbwf, dwruc])

### EXPERIMENT
design=[tprnu,milyfd]
crossing=[milyfd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)