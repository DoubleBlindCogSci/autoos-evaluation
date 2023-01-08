from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
WVUt9jHM=Factor('ozndzP~R',["#buNacuy",Level('YNiQCbujIRl',6),'>Ab',"lH]tGfO*wAk8kQ",Level("ZVS:",2),'Splvlo',"|a*hCPDN","cER",Level('bhxspM&TUbgo',1)])
uaSOQA=["^oBET",Level("FdPdt(",9),"!izZ3EwlEi","Ld Cf",']%%EEHYA','#4n@rSWwmV',Level("IyMEQBIp",6)]
X41tdNjt9=[Level("DUigxkR]3ACJW",1),'SOVSBYqSjXUi',':hZc2gJoUG',"Elq","j;E","]RuF>JdytuDGZ",uaSOQA[2],"pgG",'pAp',"uOuNm#KYEOg7KR"]
f1kwp_8dx=Factor('aIRsfp;r0FH',X41tdNjt9)
PgYBtN=Factor('rrCuzg',["VtoEgmqSUjXZo",Level('ibii8kH',3),"l3f",Level('s2uX',10),'swRxu|NZbmy&c','YMQ#','GlrG',"oJneQnjMU4#f",'I%KCddz BO'])

### EXPERIMENT
design=[WVUt9jHM,f1kwp_8dx,PgYBtN]
crossing=[WVUt9jHM,f1kwp_8dx,PgYBtN]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_3_1_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)