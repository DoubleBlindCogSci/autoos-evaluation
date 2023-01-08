from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oCh1IwRb=Factor('$XkYk',[Level("XuaQS$gQZ",6),'Pz!prPZ*j po','uQ~WM}%poZCY',"2dAGZcyq]MX",Level("twP",4),'KUXy XBS',Level('aofcpBsALYE',3),'wiMOx7:'])
B7kgPkz2B='%YH'
ySJPc_Imh=Factor('BpAj',[Level('sBeOqqMlr}x',6),Level('~VoK',4),'YCW',Level('qynojic',4),B7kgPkz2B,"XAFx",'YiY{M;n_cZ',Level("BvMx hh$w_[",6),"dwczRb9"])

### EXPERIMENT
design=[oCh1IwRb,ySJPc_Imh]
crossing=[oCh1IwRb,ySJPc_Imh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_2_1_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)