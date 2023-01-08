from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
oxw = Factor("oxw", ["gim","hdxee","lyfjip", "xncbds"])
aaspho = Factor("aaspho", ["pawt","hbr", "btkh"])
wxndnx = Factor("wxndnx", ["ktg", "oxvwfe"])
xgcgk = Factor("xgcgk", ["gixwlb", "zxx"])

### EXPERIMENT
constraints=[ExactlyK(3,(oxw,"xncbds")),MinimumTrials(40)]
design=[oxw,aaspho,wxndnx,xgcgk]
crossing=[wxndnx,xgcgk]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_0_0.csv"))
nr_constraints=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)