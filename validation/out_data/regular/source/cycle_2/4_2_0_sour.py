from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
v8_Vi9K9J=[Level('fDXuCKKYVuuP',6),"cJeCRLrkOBQ",Level("kklWkLVtdB:Qt4",7),"OABn",'cyg','bfibrrA']
wROZ_uw=Factor('W4MTKU~&WBN',[Level('WoGI;cWf',7),'cybb',v8_Vi9K9J[1],Level("tmsC4J;S",2),'Yiv3rpTs[nX@Ay'])
ffZJ0=['tsNCPlUL?',Level("bBQHegf",6),"%KvACU",'lYOcU']
J1OIjp=Factor('NvR?6@FrEbD',ffZJ0)

### EXPERIMENT
design=[wROZ_uw,J1OIjp]
crossing=[wROZ_uw,J1OIjp]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)