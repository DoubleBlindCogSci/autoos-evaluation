from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MoghVZR=Factor('dPsIbBsXpE',['pPRUvEyTvE',"jxlzg}LvS$QelF",'CtG6z5qtQ0GPK','YE*aR','M4qy&Lm6x',"ZJVQThen",'QFD WY}bgsolVL','SfM;p'])
KlPDz=["i|YL7bJytpW","BxwMlgclUw"," wl","vASM~cpB",Level("1znnBJir#k:anj",2)]
vdNqzfTr0L=['D;vqqfmDlaG8',"QdO*m9DVjw",'LT}w^F2(','{3egwQj','0pB?G','zzn',"YBzuuR",KlPDz[1],'NycuKWQGvd']
IyUad=Factor("&pWH",vdNqzfTr0L)

### EXPERIMENT
design=[MoghVZR,IyUad]
crossing=[MoghVZR,IyUad]
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