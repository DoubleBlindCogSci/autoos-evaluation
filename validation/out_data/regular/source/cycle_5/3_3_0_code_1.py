from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OgO_n=['WFBYVeYkJhs&','gSe0BywImue;#',"!OhR6?fz"]
xG11xwGAke8=Factor('EBsKQ2',OgO_n)
EkOt0=['>Tovw[Uew',"SIpw","PNlzeIYhY>X"]
Ei2U6nTGzIm=Factor("Oo2OBMm",EkOt0)
Kc9momshHDO=Factor("qdKXKQT7",["gNkhqL;tr!G",'wmAo','XrwFO&Z;tDg'])

### EXPERIMENT
design=[xG11xwGAke8,Ei2U6nTGzIm,Kc9momshHDO]
crossing=[xG11xwGAke8,Ei2U6nTGzIm,Kc9momshHDO]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_0"))
### END