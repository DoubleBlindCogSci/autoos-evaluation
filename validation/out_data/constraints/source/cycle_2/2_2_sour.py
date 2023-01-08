from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ybb = Factor("ybb", ["zlxvn","qnbiws","grsu", "xlbex"])
lhfi = Factor("lhfi", ["bus", "zcdpts"])
mlenz = Factor("mlenz", ["pvgv","ozx","flork", "mumnj"])
pqzau = Factor("pqzau", ["fhlk", "gkahpj"])

### EXPERIMENT
constraints=[AtMostKInARow(4,(ybb,"xlbex")),AtLeastKInARow(3,(lhfi,"zcdpts"))]
design=[ybb,lhfi,mlenz,pqzau]
crossing=[mlenz,pqzau]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0.csv"))
nr_constraints=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)