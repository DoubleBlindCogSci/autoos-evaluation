from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
qax = Factor("qax", ["laysc","tbdi", "jtmlcs"])
hgduyx = Factor("hgduyx", ["iwyr", "ewexc"])
czn = Factor("czn", ["cvxhp","btp","nvj", "yqvovc"])
qlrk = Factor("qlrk", ["qxszv", "tqjydm"])
sybqg = Factor("sybqg", ["prfug", "teuq"])

### EXPERIMENT
constraints=[ExactlyK(2,(qax,"jtmlcs")),Exclude(hgduyx,"ewexc"),AtMostKInARow(2,(czn,"yqvovc"))]
design=[qax,hgduyx,czn,qlrk,sybqg]
crossing=[qlrk,sybqg]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_3_0.csv"))
nr_constraints=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)