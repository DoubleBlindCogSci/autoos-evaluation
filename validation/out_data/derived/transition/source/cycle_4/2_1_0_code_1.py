from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gkonmr = Factor("gkonmr", ["feeesy","tojkq","rku","bkf","hcpsb","nzov","kgusl"])
def jngze(gkonmr):
    return gkonmr[0] == "feeesy" or gkonmr[-1] == "rku"
def ggo(gkonmr):
    return gkonmr[0] != "feeesy" and not (gkonmr[-1] == "rku")
bcznyu = DerivedLevel("jcsjia", Transition(jngze, [gkonmr]))
bmhhza = DerivedLevel("iglkje", Transition(ggo, [gkonmr]))
drhax = Factor("ove", [bcznyu, bmhhza])

### EXPERIMENT
design=[gkonmr,drhax]
crossing=[drhax]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END