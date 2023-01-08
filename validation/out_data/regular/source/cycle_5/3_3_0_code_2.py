from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EBsKQ_ = Factor("EBsKQ2", ["WFBYVeYkJhs&", "gSe0BywImue;#", "!OhR6?fz"])
Oo_OBMm = Factor("Oo2OBMm", [">Tovw[Uew", "SIpw", "PNlzeIYhY>X"])
qdKXKQT_ = Factor("qdKXKQT7", ["gNkhqL;tr!G", "wmAo", "XrwFO&Z;tDg"])

design=[EBsKQ_,Oo_OBMm,qdKXKQT_]
crossing=[EBsKQ_,Oo_OBMm,qdKXKQT_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_0"))

### END
