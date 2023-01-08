from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
LIWHc=['jBDsrvIjoVG*','XtwXq','PY6onUGzvvwa1',"n:ToaW]ZWIBqo",'ylg']
kZD60SZv="Ck]}Lx%"
k3wwvA0HUy=Factor("ina!z",["MgiwJtHl16WH y","CtN",'ZVX5ijZl',kZD60SZv,Level("JqBc",1),"MwUVB_KmleA",'YWLYkELPQ',"UDTBv","ljfsd",LIWHc[2]])
TiBMzFytH=Factor('VNq6bN',['oVz(n2K',"XtqayL","wVenwPv7X","zsckkezrOxyZ","E}X4nI","nnHxEuVTcFyBJ",'K#wBYpO[',">OEUYMCauvi"])
rN2PQK9qjp="NOQJ"
JWo1xoGHtE=Factor("LqJaK",['$|WaBb',rN2PQK9qjp,"hGWzmbCiCbiiCB",'OE0&JVkrJ','KGQTvUU^g~m',"HNM8",'ETy?','!h5qxOb)JHp','IISWoRM'])

### EXPERIMENT
design=[k3wwvA0HUy,TiBMzFytH,JWo1xoGHtE]
crossing=[k3wwvA0HUy,TiBMzFytH,JWo1xoGHtE]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_3_1_0.csv"))
nr_factors=3
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)