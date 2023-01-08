from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vlzwOE4I=Factor("6SZW%qT Tzg",['xgUOpw','0Qom','iLHXiPoR',"JIxzytPjOqTuY","iYawESJhzUK",'wRSUcfICrWF',"LXAuu"])
AtXEUTZ=":qMBD"
ZUh6LY5eF=['ALVwPwmclY','QlKBf3$oQINl','PYvSbPnmN',AtXEUTZ,Level('w@FL',3),'gIoZ*dLozIZz','>vttJxPu)U',"fOmq"]
DLDa0jauV=Factor("dq!a9NaZ",ZUh6LY5eF)
AYElMPIv=["mx]<JLXwSr qi",'gNvQbD#yn',Level('F5PyCazprMncUr',1),"coIO vpDL",'JI<<bOrXx']
esBjPvZN=Factor('rWXFXyC',[Level("bvX_DNsdXVQF",4),"ZnpkjBJFFz Ae","b9MuBKmKOoB",AYElMPIv[2],'px5bt','M6OodBmiuMWg#R','yxB',"lND6}erUYKmK1"])
lsMJ76E=Factor('K7JkN6xowZko',['MiH','UkjGLPmv',"FGxdx]yZRV6qUf",'Nz0wrmt','hDAU>hBT42njB<',"cRsglN[*G",'rhja8T[?QD'])

### EXPERIMENT
design=[vlzwOE4I,DLDa0jauV,esBjPvZN,lsMJ76E]
crossing=[vlzwOE4I,DLDa0jauV,esBjPvZN,lsMJ76E]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_4_1_0.csv"))
nr_factors=4
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)