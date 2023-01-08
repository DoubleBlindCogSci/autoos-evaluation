from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
LDHmI=Level('wdggRlqel',6)
MrhL37mFUy=Factor("Uybr",["ATLpPSw",LDHmI,"Qyrg","hWjSp",Level("O_ROUCgFYDZ",10),'dowiczkYJJkj(l',Level('t#R',9)])
VFjA5p=Factor("rTwGA",[Level("]&TGB5mxRSCB",4),Level('Dyavv|3C',7),Level("bRuwGpkMq",7),Level("eIkREvKl|Dvr",6),'u><HLRg7ISu',"Kfx}VMlifM"])

### EXPERIMENT
design=[MrhL37mFUy,VFjA5p]
crossing=[MrhL37mFUy,VFjA5p]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_1_0.csv"))
nr_factors=2
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)