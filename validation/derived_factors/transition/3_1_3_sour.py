from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iovk = Factor("iovk", ["myck","tok","jrlroa","rzjp","wbans","dvtuyz","kbikwr"])
def gmtnpb(iovk):
     return iovk[0] == "wbans" and not iovk[-1] == "kbikwr"
def hfvbz(iovk):
     return (iovk[0] != "wbans") and  "kbikwr" == iovk[-1]
def wjgwva(iovk):
     return (not iovk[0] == "wbans") and (not hfvbz(iovk))
aknpis = DerivedLevel("gza", Transition(gmtnpb, [iovk]))
rizi = DerivedLevel("hll", Transition(hfvbz, [iovk]))
dgk = DerivedLevel("ffmnii", Transition(wjgwva, [iovk]))
vfzxe = Factor("gli", [aknpis, rizi, dgk])

### EXPERIMENT
design=[iovk,vfzxe]
crossing=[vfzxe]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)