from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cxzr = Factor("cxzr", ["xjxh", "xwjjzr"])
zoupa = Factor("zoupa", ["oneas", "brupr"])
bnqm = Factor("bnqm", ["eqzv", "axe"])
pgp = Factor("pgp", ["bwd","dxnkad", "trqmsl"])
yysq = Factor("yysq", ["ugivpp","tfjl", "tvzwjc"])

### EXPERIMENT
constraints=[ExactlyK(4,(cxzr,"xwjjzr")),ExactlyKInARow(4,(zoupa,"brupr")),MinimumTrials(39)]
design=[cxzr,zoupa,bnqm,pgp,yysq]
crossing=[pgp,yysq]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)