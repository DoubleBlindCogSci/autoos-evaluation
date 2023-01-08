from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
u0lNpmVpH=Factor("mFqDNN!M;bv",[Level('zNetXJow',5),Level('DfMFe',1),"y_St",Level("WxWi",7),Level('kGiXa5<bdFP ',5)])
OHBDukXxa="KVkCfe"
yNsH=Factor('wR?XQip4',[OHBDukXxa,'X3xzKAD',"2xTlvaElNl",Level('HwqO',5),"Yjr",Level('Lo>UHI',1)])

### EXPERIMENT
design=[u0lNpmVpH,yNsH]
crossing=[u0lNpmVpH,yNsH]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_1_0.csv"))
nr_factors=2
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)