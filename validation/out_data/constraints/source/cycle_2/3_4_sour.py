from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
apzs = Factor("apzs", ["sjnzhf","pydes","avo", "gooen"])
rzcr = Factor("rzcr", ["ffgfn","fqw", "kpgbi"])
cfycbu = Factor("cfycbu", ["fqnxz","ynqh", "jcfdy"])
eptgp = Factor("eptgp", ["ftbfhn","vxkf", "qtxj"])

### EXPERIMENT
constraints=[Exclude(apzs,"gooen"),AtLeastKInARow(4,(rzcr,"kpgbi")),AtMostKInARow(2,(cfycbu,"jcfdy"))]
design=[apzs,rzcr,cfycbu,eptgp]
crossing=[eptgp]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_4_0.csv"))
nr_constraints=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)