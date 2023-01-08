from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
X23o='T$8z%QZiu7['
VqsX=[';Sn$P0(OjN&u7!',Level('JngTJvF[Q<w',2),X23o]
DdZhrBJgo=Factor("kj8bFlzzZxBUWN",VqsX)
cPi2CmmPC=Factor("&eKIIcWPARN%",["E&XhX}ucj;",'{trZJ(zWTu'])
lWrn1=Factor("iDRw",['aoLSwy_mvY0HAg','MAQD[8hhm'])

### EXPERIMENT
design=[DdZhrBJgo,cPi2CmmPC,lWrn1]
crossing=[DdZhrBJgo,cPi2CmmPC,lWrn1]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_1_0.csv"))
nr_factors=3
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)