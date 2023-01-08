from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
qwiy = Factor("qwiy", ["dgu","qvgr","yzrvv","gjiu","czhpzo","fthdvo"])
rnrlm = Factor("rnrlm", ["slu","icpjh","ihfoa","kszigq","vgrk","ehej","eqm","lyovq"])
def kseuvv(qwiy, rnrlm):
     return qwiy == "dgu"
def weh(qwiy, rnrlm):
     return "dgu" != qwiy and  rnrlm == "lyovq"
def tbvd(qwiy, rnrlm):
     return (not kseuvv(qwiy, rnrlm)) and (rnrlm != "lyovq")
mphwlt = DerivedLevel("yqcwc", WithinTrial(kseuvv, [qwiy, rnrlm]))
bvuk = DerivedLevel("gscts", WithinTrial(weh, [qwiy, rnrlm]))
tzdpiz = DerivedLevel("eqh", WithinTrial(tbvd, [qwiy, rnrlm]))
gani = Factor("koxrmj", [mphwlt, bvuk, tzdpiz])

### EXPERIMENT
design=[qwiy,rnrlm,gani]
crossing=[gani]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)