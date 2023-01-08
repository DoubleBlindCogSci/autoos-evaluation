from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mBMgkz0r=Factor('V_wC',['dreaJwR:',"aAzE","TTBhCQBnD",'FES',Level("^E%",1),'iXcBfN','Ann',"9FHNXzojhKn7("])
GyDP=Factor('rDac*T}psjF',[Level("C lPvRRSmE",2),'CqQOzlzkQvLa9',"1e9|:","G<GWMf","N5VpbuLmFS",Level('Pcq@zwY<F',4),"ufxTm","KVl0YFN"])
WE_E=Factor("YuXmIWj9]",["bpP8Gi3*3V",'cY~u?eU','tRvOFbSdEI;r','~3nN;*iC','XFc68ekc','Lv_k','ROaVqfW&yqsUbI',"Ai ET@k"])
xOijX='XH>Pn>j'
HwaMc=Factor('dgjWFM',['E4QVkD!Gn',"oZAEZFrCVSs","L^ee",'vquv','wO]hqOv&cAvAYo',"is*GNUE",'!vGVxnNeY','rQT',xOijX])

### EXPERIMENT
design=[mBMgkz0r,GyDP,WE_E,HwaMc]
crossing=[mBMgkz0r,GyDP,WE_E,HwaMc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_4_1_0.csv"))
nr_factors=4
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)