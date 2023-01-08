from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ogbl = Factor("ogbl", ["etudac","wxt", "jkb"])
teyclb = Factor("teyclb", ["bxfpd", "kuu"])
bxxl = Factor("bxxl", ["awfv", "hmbn"])
xzh = Factor("xzh", ["cxys","aqh","dlfx", "wlohoa"])
mant = Factor("mant", ["hwx", "iodnw"])
ugyl = Factor("ugyl", ["fpneis","hbnb", "swvspa"])

### EXPERIMENT
constraints=[ExactlyKInARow(2,(ogbl,"jkb")),Exclude(teyclb,"kuu"),ExactlyK(3,(bxxl,"hmbn"))]
design=[ogbl,teyclb,bxxl,xzh,mant,ugyl]
crossing=[xzh,mant,ugyl]
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