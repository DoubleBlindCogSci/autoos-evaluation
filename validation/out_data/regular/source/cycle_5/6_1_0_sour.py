from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
finB=Level("zvuocncr",1)
bd4HuCXn2o='DzwmD>o'
VhoqxpdmAzY=Factor('[Tq',[finB,'qcGjlkq','im8(l',Level("quiBMqJ)",1),"tucqET6x}9",bd4HuCXn2o,"IWLU",'!IB'])

### EXPERIMENT
design=[VhoqxpdmAzY]
crossing=[VhoqxpdmAzY]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_0_0.csv"))
nr_factors=1
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)