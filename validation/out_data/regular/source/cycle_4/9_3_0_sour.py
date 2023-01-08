from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wBPdECv2="en5M*Z"
p89EDRF=['mwPrApHC','eRGDxwwQvQm',wBPdECv2,"tlgofwqzft",Level('E}heUMKsJY',1),"kf!^",'P8;B:DeExt',"adiGESg","kbdpZW&VkEn",'bPd7zslvhbpnf']
ZZEmyJ=Factor("yCDHuUKKXJHlmw",p89EDRF)
kbbtKgA=Factor("pNTQUQ xZYN",["jjjru","LSxy",")UyqDWjyKp~qZ","Qdi!bsTMzuE","OybdpZ",'GmR','Fdh',"ROgzVknx","eYatjGpkNdQv"])
rjVLO2_AeSx=Factor("m*sldpo<",["oacC8VzGFCuwhU",'|oeEvjIxpCdiL',"pfOd","#Uj~PkG",'SzZbjAT}Fd',"m(x<drnKo",'bFSRxDVXBbhnp',"M^Gs",'ADiFE~'])

### EXPERIMENT
design=[ZZEmyJ,kbbtKgA,rjVLO2_AeSx]
crossing=[ZZEmyJ,kbbtKgA,rjVLO2_AeSx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_3_0_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)