from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
ara = Factor("ara", ["zfixf","hky","diow", "rexvr"])
qvzmh = Factor("qvzmh", ["hywxxi","ymyrth","zliw", "edphtg"])
clyjhw = Factor("clyjhw", ["rfb","cpyux", "szkhcv"])

### EXPERIMENT
constraints=[ExactlyKInARow(3,(ara,"rexvr")),AtMostKInARow(2,(qvzmh,"edphtg"))]
design=[ara,qvzmh,clyjhw]
crossing=[clyjhw]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_0.csv"))
nr_constraints=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)