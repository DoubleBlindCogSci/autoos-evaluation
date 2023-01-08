from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
o_gjYTxPb='<iwy}pnKP8'
DFFAFcAIrJ=['IHCmSJdC}zeC',Level('MA0YAZ 9ODft',2),Level("FAFAYrA1u|I",3),"ocwU!Twxuzfb",'wwTPgoo','Q]*zLlDSt',Level('a{bY%MZCIQpMDh',1),Level("GIHDEImSQxS",2)]
Ac26Xaf_QB=Factor("foBeAcVgYj2",['vjVFCEItOwt',"cDYFfFf",o_gjYTxPb,"mGf6Gxpv",'XNxbH',"Di6KYmIB","RjOE",'{GMlV3Dr','YYO?fvNTPWQ',Level('SVcgp)Nax',3),DFFAFcAIrJ[3]])
GP1ysx=Factor("PyzP",["mFDTa",'opoKtKkNvzhj',"JhDjc0_g","odIFPim}ZXvC",'Sqo<KujF}',"QG}HqG[ER7",'gergxGLBPT7IV','AXcg3E~yxM','Lttv'])

### EXPERIMENT
design=[Ac26Xaf_QB,GP1ysx]
crossing=[Ac26Xaf_QB,GP1ysx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_2_0_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)