from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Ak6TKQz1wz=Factor('aFFrDTJF~',["NCeyfqWILr5RzI",Level("YH%njwHgJe",5),'pPr08Ddvqy','DM?fq Bzq',"DpD|IK Boe"])
UjhTMAufZVB=Factor("KJgiTHr7lW",['}LY',Level('chk>mOUZsDPlO',3),Level(']~@FmCBJsA',8),Level('RUDwvZ?',8),'AQ}RRYJf2)<Uje'])

### EXPERIMENT
design=[Ak6TKQz1wz,UjhTMAufZVB]
crossing=[Ak6TKQz1wz,UjhTMAufZVB]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_2_0_0.csv"))
nr_factors=2
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)