from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
R9k3X=Factor("emnMyZcbxQ",["MrtiTMs(aSeyvu","Vg$[ChLt(E ",'jrUWLycz b7W%','oyRv',"jgZAGcLgxblY","MPM",'I5aAsle','x~g:oNl]'])
C_CgHF=Factor('He2~  qjh',['La)SsIQczx','GpaG'," ko","V5are8AHhv",'nWMpcCrXv{K',"qtQUS",'3tsd<',"NQsByAwBdy"])

### EXPERIMENT
design=[R9k3X,C_CgHF]
crossing=[R9k3X,C_CgHF]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_2_1_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)