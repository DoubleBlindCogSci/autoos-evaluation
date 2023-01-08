from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tprnu = Factor("tprnu", ["aot","aqp","eldx","bsxt","lklq","xkjq","hnt"])
def uvgzin(tprnu):
     return "xkjq" == tprnu[0]
def ymhc(tprnu):
     return "bsxt" == tprnu[-1]
def eurgqp(tprnu):
     return (not uvgzin(tprnu)) and (not tprnu[-1] == "bsxt")
zphx = DerivedLevel("ngmg", Window(uvgzin, [tprnu],2,1))
tvbwf = DerivedLevel("jvk", Window(ymhc, [tprnu],2,1))
dwruc = DerivedLevel("jrldp", Window(eurgqp, [tprnu],2,1))
milyfd = Factor("shrv", [zphx, tvbwf, dwruc])

### EXPERIMENT
design=[tprnu,milyfd]
crossing=[milyfd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END