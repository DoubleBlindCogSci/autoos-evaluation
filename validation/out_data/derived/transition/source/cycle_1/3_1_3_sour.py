from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ghljns = Factor("ghljns", ["dgbxuu","wxfjh","tgxq","fqttg","bcgva","kwxwwg","sassnr","fpa"])
def pmm(ghljns):
     return "sassnr" == ghljns[0]
def bzwtlz(ghljns):
     return "tgxq" == ghljns[-1]
def qisax(ghljns):
     return (ghljns[0] != "sassnr") and (not ghljns[-1] == "tgxq")
jlwva = DerivedLevel("ery", Transition(pmm, [ghljns]))
oiji = DerivedLevel("ltxz", Transition(bzwtlz, [ghljns]))
uav = DerivedLevel("kybpzi", Transition(qisax, [ghljns]))
gva = Factor("youocf", [jlwva, oiji, uav])

### EXPERIMENT
design=[ghljns,gva]
crossing=[gva]
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