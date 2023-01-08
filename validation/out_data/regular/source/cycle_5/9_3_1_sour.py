from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RAqI=Factor("ScY",[Level('kvzBaS9p',2),"2xNBOUjVPlN","pkZPC<hdr",'?BpoR','LBiAoA$fZbCv',"nDKyhot","s_ofo",'haD0euQ',"uNwxfRC"])
vQp6Wb=Level('oJf#N',1)
wdx9OoQVc=[vQp6Wb,"GY2AXx[*",'^uQ}gRj','YmTZuAu',"0voYsEWkjXCB",'bXB%GKCW',"QiyzS6",'p4izJliG',"B65",'iehc']
zsEB=Factor("EOOJTns5VdPxM",wdx9OoQVc)
TbdVKaXml=Level("rifENTgudZ",1)
Je67HtX5=['srHT','GHyUECmTKDKN','rN pex',"4BEbAVO",'Bn@wDLlZA','GDO','qc2KMQkxL7',Level("0qnEZKMkJ",4),TbdVKaXml,'r2KTgU']
YoQBeyJ=Factor("d9u",Je67HtX5)

### EXPERIMENT
design=[RAqI,zsEB,YoQBeyJ]
crossing=[RAqI,zsEB,YoQBeyJ]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)