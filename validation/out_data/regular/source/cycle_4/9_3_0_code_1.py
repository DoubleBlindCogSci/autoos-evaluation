from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_0"))
### END