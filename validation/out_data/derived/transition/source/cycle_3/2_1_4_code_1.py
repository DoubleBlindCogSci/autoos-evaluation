from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xupuds = Factor("xupuds", ["zflxlt","vbwp","rrrc","nkfv","yijpy","hbqcw"])
def ddpmdw(xupuds):
    return xupuds[0] == "nkfv" and xupuds[-1] != "zflxlt"
def gekzjl(xupuds):
    return xupuds[0] != "nkfv" or not (xupuds[-1] != "zflxlt")
ajbovd = DerivedLevel("jpetbu", Transition(ddpmdw, [xupuds]))
gagik = DerivedLevel("ilpxk", Transition(gekzjl, [xupuds]))
blapn = Factor("tmxfqu", [ajbovd, gagik])

### EXPERIMENT
design=[xupuds,blapn]
crossing=[blapn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END