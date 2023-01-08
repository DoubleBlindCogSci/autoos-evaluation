from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
crxpce = Factor("crxpce", ["achh", "hlnrh"])
bhxrvp = Factor("bhxrvp", ["yexbb","ccist", "vpejld"])
wgnnv = Factor("wgnnv", ["byh","rcxqaj","pnz", "ytrjy"])
flirem = Factor("flirem", ["ytfomo", "dhyhj"])
rgp = Factor("rgp", ["hlnzfs", "gylt"])

### EXPERIMENT
constraints=[ExactlyKInARow(4,(crxpce,"hlnrh")),ExactlyK(2,(bhxrvp,"vpejld")),AtMostKInARow(2,(wgnnv,"ytrjy"))]
design=[crxpce,bhxrvp,wgnnv,flirem,rgp]
crossing=[flirem,rgp]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0.csv"))
nr_constraints=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)