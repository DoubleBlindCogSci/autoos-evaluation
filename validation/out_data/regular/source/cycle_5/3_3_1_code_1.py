from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
A7Dv=["gmrmqdrbV",Level("iOWlqg$4Q",1),"d>fkJUcT"]
j34xPTo=Factor('F$n',A7Dv)
xi0n=Factor("FNqnN%jO4W",['NEBDXKo',"jUlB[lEE",'LJzRmosfFX'])
cmP_kR=['jo~|WwwoNpBiUF',"8hEFb",'GXNN4C1wi']
N7Yge=Factor('zaOMtPyNtYct',cmP_kR)

### EXPERIMENT
design=[j34xPTo,xi0n,N7Yge]
crossing=[j34xPTo,xi0n,N7Yge]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_1"))
### END