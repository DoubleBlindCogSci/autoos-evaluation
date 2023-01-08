from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
C2CKDccyw="SoWBiQ&YTqQzcT"
KeXgoi1=[C2CKDccyw,Level("sfQt",7),"y6^Cq_",'EPLv:JMYYMK']
ySyqMZkV=Factor(">rY@eZI}Oc)",KeXgoi1)
xkZFH5W='mEWV^bB}WiGkl'
Jeo4=['fp{G',xkZFH5W,"1jI9QflgLp","PYtvC_ZbJlo"]
agDBde2=Factor('M3UTjqP0VUHvE',Jeo4)
pA2Rh=["eClU}ThYb","LpYI~oVWxscLTg","YlYn zR{gfVehn"]
N_nOYproc=Factor("dtD^MQkuKXy",pA2Rh)

### EXPERIMENT
design=[ySyqMZkV,agDBde2,N_nOYproc]
crossing=[ySyqMZkV,agDBde2,N_nOYproc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_3_1_0.csv"))
nr_factors=3
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)