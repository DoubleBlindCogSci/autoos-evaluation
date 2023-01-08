from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
osey = Factor("osey", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
ndkbz = Factor("ndkbz", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
dwwn = Factor("dwwn", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
def ixy(osey, ndkbz, dwwn):
    return osey[0] != ndkbz[-1]
def kuyyd(osey, ndkbz, dwwn):
    return not ixy(osey, ndkbz, dwwn)
hfrr = DerivedLevel("gubi", Transition(ixy, [osey, ndkbz, dwwn]))
attvch = DerivedLevel("cdps", Transition(kuyyd, [osey, ndkbz, dwwn]))
xsu = Factor("pktwz", [hfrr, attvch])

### EXPERIMENT
design=[osey,ndkbz,dwwn,xsu]
crossing=[xsu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END