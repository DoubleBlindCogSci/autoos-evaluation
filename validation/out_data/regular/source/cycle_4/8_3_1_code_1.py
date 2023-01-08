from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_1"))
### END