from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EXBCuSOt6Po=["!kNySyZU","rkZJb#}TZ)I",'nLI*YFg',"VABI",'IbD']
CJQ0X=Factor('ATt',['hON',"gSvq_",'ijm}CjTDpBompc',EXBCuSOt6Po[2],'ZkQHyJN(j~ ','$ZzoKDfJOb|','dcfxkQnOR6r','NwPbastQN',"eI setsNY","FesW]S",'IyxCxQQHV'])
OR37=Factor('W7AzyZw~?MSK',['lseRor!cqHCa','T}fikaFghFlNYz',"pk<b LuZ^oGY","bLs","rrnjycxVCiROM","ktBGy$","hGVKFWCd0F","wSou_ejp",'2wQ','#rithj(Zxe'])

### EXPERIMENT
design=[CJQ0X,OR37]
crossing=[CJQ0X,OR37]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/10_2_0_0.csv"))
nr_factors=2
nr_levels=10
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/10_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)