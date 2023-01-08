from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dw1oyxKvJO=['N<ZXJenQog5tU','JTjIEeCPzihX','dZoO$8Z]uxw[eF',"Ia5kE8BG","q7xqINi",Level('Q5UpubySot4',4),Level('AuBb',2)]
CkHutR=[Level("kTgCBo",3),dw1oyxKvJO[2],"utXNld?AdXwG","kg4JqTq%Yt",'PjfbyGLBPRltWg']
rGK8=Factor("xvY",CkHutR)
kP0ksR9P1G=Factor("IVH",["fG^swtQYm","mgUjZ?",';gJBl:P',Level("UWneV",2)])
sx0Dn=Factor('bC3DNg',[Level("lpPrq",1),"BYDwlOTzPr","]czuP",'z4wIcQE'])
nqJXyEXI=Factor('UKGjSSoVt',["Buzg",'aj^p:e','cZFN','jCG;fMVo'])

### EXPERIMENT
design=[rGK8,kP0ksR9P1G,sx0Dn,nqJXyEXI]
crossing=[rGK8,kP0ksR9P1G,sx0Dn,nqJXyEXI]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_4_1_0.csv"))
nr_factors=4
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)