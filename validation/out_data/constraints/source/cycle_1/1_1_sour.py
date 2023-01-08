from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
zrjr = Factor("zrjr", ["aoyis","hmmcrq", "jfyiwu"])
vjaiwl = Factor("vjaiwl", ["giotq","bwj", "fvt"])
midsd = Factor("midsd", ["sgmu", "xnvn"])

### EXPERIMENT
constraints=[AtMostKInARow(2,(zrjr,"jfyiwu"))]
design=[zrjr,vjaiwl,midsd]
crossing=[vjaiwl,midsd]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/1_1_0.csv"))
nr_constraints=1
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)