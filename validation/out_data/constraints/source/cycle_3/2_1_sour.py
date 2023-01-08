from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pjc = Factor("pjc", ["hsh","ddh", "nspchy"])
jjptqo = Factor("jjptqo", ["smhs", "cnhxtr"])
ned = Factor("ned", ["rzc","dgvq","isrwm", "pgl"])

### EXPERIMENT
constraints=[AtMostKInARow(3,(pjc,"nspchy")),AtLeastKInARow(4,(jjptqo,"cnhxtr"))]
design=[pjc,jjptqo,ned]
crossing=[ned]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_0.csv"))
nr_constraints=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)