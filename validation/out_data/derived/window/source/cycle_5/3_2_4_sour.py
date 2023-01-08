from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rxerxr = Factor("rxerxr", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
begh = Factor("begh", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
jwacc = Factor("jwacc", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
def uoks(rxerxr, begh, jwacc):
     return begh[-2] == rxerxr[0] and rxerxr[-2] != jwacc[0]
def cvq(rxerxr, begh, jwacc):
     return begh[-2] != rxerxr[0] and rxerxr[-2] == jwacc[0]
def pfmwt(rxerxr, begh, jwacc):
     return (not rxerxr[0] == begh[-2]) and (rxerxr[-2] != jwacc[0])
oidv = DerivedLevel("woyerc", Window(uoks, [rxerxr, begh, jwacc],3))
ljy = DerivedLevel("xpt", Window(cvq, [rxerxr, begh, jwacc],3))
uqvamn = DerivedLevel("vblwpg", Window(pfmwt, [rxerxr, begh, jwacc],3))
zss = Factor("dhaal", [oidv, ljy, uqvamn])

### EXPERIMENT
design=[rxerxr,begh,jwacc,zss]
crossing=[zss]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)