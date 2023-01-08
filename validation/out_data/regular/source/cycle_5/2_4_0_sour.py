from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tWkjSJp=['*vEdLnSHq&?MNu',Level('2kFa',1)]
zJuHAHCW=Factor('Lwp(nnRMKq',tWkjSJp)
dyBbr=Factor('GY!',['L9WVAMPvBvuaZ','wy5vkP(aiXm'])
y4Z9AFc=Factor('RrT(Oh',['cuqHR)Z6E2@J',"Dtum4"])
n_0VCm5=Factor('yDe>f',["T^#*bHSDYj",Level('RQ3Qj',1)])

### EXPERIMENT
design=[zJuHAHCW,dyBbr,y4Z9AFc,n_0VCm5]
crossing=[zJuHAHCW,dyBbr,y4Z9AFc,n_0VCm5]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_4_0_0.csv"))
nr_factors=4
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)