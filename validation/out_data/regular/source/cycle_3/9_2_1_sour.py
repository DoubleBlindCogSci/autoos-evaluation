from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bJvPc=Level('DBv6tnuw',10)
Wglr=Factor('Ncp',['u%whc','NAhQ2 &waGA','puZz4teJMKJ',"vmlShuSG_h","juX3RSd8qJ",Level('wIY4vATHmeHn',10),Level('~i)HFQmcpRH',5),"lg%9szyeLPs",Level('I3cUKG',6),bJvPc])
CiHCx0YwN=Factor('gD!MZ[US',['QRvUD*fo','b&gSEeGoXmkW',"bmqI~wVl{GDGra","KNo D8",Level("gI2YFl]syX",3),'LtAgghskcb&',Level('yGK',7),"OFkXIpQ>",Level("CiGQ^LCZiZGsUt",4)])

### EXPERIMENT
design=[Wglr,CiHCx0YwN]
crossing=[Wglr,CiHCx0YwN]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_2_1_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)