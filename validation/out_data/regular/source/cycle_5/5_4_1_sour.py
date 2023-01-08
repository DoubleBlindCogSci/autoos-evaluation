from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
F0ah=Factor("bxJb",[";PVCO$aWcbz",'ylo6Y}V',"BdY#FTkBv","rKo",'pZIl'])
ZsIFsAwet=Factor("VlJ",["AqzS}Bf",Level("r?Tjbj!MM",3),"T DkVkh^hG9","UuftnN ",'~eXNL5nuuW'])
czgH92ikH=["TpZUe",'FaJq8okZsp<','FpBVsTuVHl(:pE','Z$p','?gvaU']
t1Jit7t5F=Factor('MhQr',czgH92ikH)
rFei8IPkvLW=Factor('fPimoTeuEI{',['M$[LlIlc&0qii','4GK:qMKh','uvyeANtA','Tec*DFIour',"fiVqrMgCrZfq"])

### EXPERIMENT
design=[F0ah,ZsIFsAwet,t1Jit7t5F,rFei8IPkvLW]
crossing=[F0ah,ZsIFsAwet,t1Jit7t5F,rFei8IPkvLW]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_4_1_0.csv"))
nr_factors=4
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)