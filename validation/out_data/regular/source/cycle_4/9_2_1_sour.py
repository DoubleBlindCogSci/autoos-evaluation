from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HyBOCX6kp1B=['}GN^j{leK','R#U',Level("NWNYcy",2),"IHWk("]
o4MnidhDxx='vt;'
fa7c8ukdS=Factor('ZkX}tIBFirTJ',['gxuEEmGPjd','kg_YYOZ',"OQB",Level("#NHeid",3),'WJACKaffc<G',o4MnidhDxx,"E7QCPK","MTM","s>EN8htD",'yjoF^dSse',HyBOCX6kp1B[1]])
zOit3m=["XRkx5$JmVx",Level('TDpwahS#TACXo',1),'mWUEB[oovwzi','Q3F6I2a6tb5TF(',"jGa>L^3~r","OY$",'1fq<E(6 &JxBG','%a6UN)zmz_!a4',"fIIDMx^{iX46w["]
Z_bW=Factor('ayQBYUg%',zOit3m)

### EXPERIMENT
design=[fa7c8ukdS,Z_bW]
crossing=[fa7c8ukdS,Z_bW]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)