from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CqEv6j=Factor("VMbHH",["yTsQ","EBZV&^OQU",Level("EEYubd;GPul8b",2),"xCN",'QDMR','@lC#OBcnWUD'])
R8Bdi4=Factor('Wcax',['LzEJdsI',"MK2WDcS",'hQWiXO5r','WicY',"pG9","coO]"])

### EXPERIMENT
design=[CqEv6j,R8Bdi4]
crossing=[CqEv6j,R8Bdi4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_0"))
### END