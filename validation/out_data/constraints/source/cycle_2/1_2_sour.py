from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
woa = Factor("woa", ["jjbf","tmxd", "jmo"])
ssvhq = Factor("ssvhq", ["swxqp","vkorxn", "jegphi"])
hcmjtm = Factor("hcmjtm", ["avg", "whmy"])

### EXPERIMENT
constraints=[AtLeastKInARow(4,(woa,"jmo"))]
design=[woa,ssvhq,hcmjtm]
crossing=[ssvhq,hcmjtm]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/1_2_0.csv"))
nr_constraints=1
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)