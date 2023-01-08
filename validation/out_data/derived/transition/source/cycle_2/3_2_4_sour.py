from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
szoeft = Factor("szoeft", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
dgtvts = Factor("dgtvts", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
illdc = Factor("illdc", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
def pzj(szoeft, dgtvts, illdc):
     return szoeft[0] == dgtvts[-1] and szoeft[-1] != illdc[0]
def hycg(szoeft, dgtvts, illdc):
     return dgtvts[-1] != szoeft[0] and szoeft[-1] == illdc[0]
def sulrut(szoeft, dgtvts, illdc):
     return (not szoeft[0] == dgtvts[-1]) and (not szoeft[-1] == illdc[0])
illx = Factor("gutkwe", [DerivedLevel("bywbjl", Transition(pzj, [szoeft, dgtvts, illdc])), DerivedLevel("feucje", Transition(hycg, [szoeft, dgtvts, illdc])),DerivedLevel("yawb", Transition(sulrut, [szoeft, dgtvts, illdc]))])
### EXPERIMENT
design=[szoeft,dgtvts,illdc,illx]
crossing=[illx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)