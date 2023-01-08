from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Ocvb=Factor("6nMFHmg",['U RPg',Level('U>eAy',9),Level('nMBLBD',6),'TFPr7Azswr','deEUu',"hqp",'%ZoTnVTIe&',"M:z]GH"])
gg0KkMEO4=[Level('lqAK4QobG_zBVR',2),Level("isRd",5),Level("PNm",2),'BMMmNTpyMD','}dzpC8',"i$Nm",Level("BMPhQNUw",8),"DGIUu}"]
YD_3=Factor('RryaCHD<QG',gg0KkMEO4)

### EXPERIMENT
design=[Ocvb,YD_3]
crossing=[Ocvb,YD_3]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_0"))
### END