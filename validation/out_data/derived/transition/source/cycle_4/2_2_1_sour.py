from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yjvend = Factor("yjvend", ["daxgeh","ptvxz","fhkxo","orc","xdufc"])
wlhhi = Factor("wlhhi", ["zhg","vfvhl","nlidm","pudexk","krbx"])
def neoul(yjvend, wlhhi):
    return yjvend[0] == "orc" and wlhhi[-1] == "krbx"
def rdr(yjvend,wlhhi):
    return not (yjvend[0] == "orc") or wlhhi[-1] != "krbx"
jth = DerivedLevel("uic", Transition(neoul, [yjvend, wlhhi]))
fjrfea = DerivedLevel("hsiyw", Transition(rdr, [yjvend, wlhhi]))
feuktd = Factor("yzdw", [jth, fjrfea])

### EXPERIMENT
design=[yjvend,wlhhi,feuktd]
crossing=[feuktd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)