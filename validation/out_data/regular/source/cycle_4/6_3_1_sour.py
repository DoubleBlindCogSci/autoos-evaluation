from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
luANK7R=['mlAZbtzOD','nKr*#Y','B&~T9GDSZ',"B0xjrSIfn",'1AAewslQoHsdI','sxxrZ1aFrEGi']
RfXR=Factor('jic',luANK7R)
wjt3jxV=['ENJX~vDmHu',"uz~wzT a","rwi%jIzEJ"]
jsRv6fSbe=Factor('vtg:aXID',[wjt3jxV[0],"VyoHmOmf","QmEkjZRr z^dE",'DpKtQyJNUiyDIY',"OoV7f~l<",'DIFSplJ9ptR',"AcebDObN"])
JHuq9vtmZTG=['mwlk','fExcH','rxtl',"LItp&Zb7R",Level("tSLOOQGs5 ",4),"^sHgd"]
o2hL8qRVB=Factor('a&fUekLOWtD',[JHuq9vtmZTG[4],'KoZ',"#dM1Eo7EPc","elgmRMLGeY!kw@",' owJn',Level("osHHgtGdGLbG",1),Level('JLMygcjPqDTz',2)])

### EXPERIMENT
design=[RfXR,jsRv6fSbe,o2hL8qRVB]
crossing=[RfXR,jsRv6fSbe,o2hL8qRVB]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_3_1_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)