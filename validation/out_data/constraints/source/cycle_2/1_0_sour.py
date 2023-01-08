from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
epf = Factor("epf", ["aae","pfezr", "dge"])
clfx = Factor("clfx", ["smak","dfvmwf","qhftpk", "gcxzn"])
xbhpdm = Factor("xbhpdm", ["jpbyaz", "cxkhi"])

### EXPERIMENT
constraints=[ExactlyK(4,(epf,"dge"))]
design=[epf,clfx,xbhpdm]
crossing=[clfx,xbhpdm]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/1_0_0.csv"))
nr_constraints=1
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)