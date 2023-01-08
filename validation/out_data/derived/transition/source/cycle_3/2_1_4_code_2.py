from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xupuds = Factor("xupuds", ["zflxlt","vbwp","rrrc","nkfv","yijpy","hbqcw"])
def is_tmxfqu_jpetbu(xupuds):
    return xupuds[0] == "nkfv" and xupuds[-1] != "zflxlt"
def is_tmxfqu_ilpxk(xupuds):
    return not is_tmxfqu_jpetbu(xupuds)
tmxfqu= Factor("tmxfqu", [DerivedLevel("jpetbu", Transition(is_tmxfqu_jpetbu, [xupuds])), DerivedLevel("ilpxk", Transition(is_tmxfqu_ilpxk, [xupuds]))])

design=[xupuds,tmxfqu]
crossing=[tmxfqu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
