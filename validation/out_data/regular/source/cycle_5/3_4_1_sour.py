from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GVR3c9Glyc=Factor("}FzSMyl",["m LrDFvap",'wtF<LZFluJ','*qnh(M'])
VA1LOfkJm=Factor("BIwkduEvUm",['~Gq',"LrLs","MstFu~dL4fyrCY"])
Kcztts7_=Factor("pc|AbZlUc",["hhwdX&Y<@","E~ZwGxz","L<YDO"])
TeYpDyHCr_S="0x&gWPPs"
MkdGw21=['qdBmj%qSq4_xfa','jKYT)7ci',TeYpDyHCr_S,'c|!hF:ooQ>ie']
NRkeM=Factor("Qrw?CIO",MkdGw21)

### EXPERIMENT
design=[GVR3c9Glyc,VA1LOfkJm,Kcztts7_,NRkeM]
crossing=[GVR3c9Glyc,VA1LOfkJm,Kcztts7_,NRkeM]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_4_1_0.csv"))
nr_factors=4
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)