from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zpytsb = Factor("zpytsb", ["oithj","wed","gri","dyelw","hfui","blmdcz","dhjcm"])
def nwq(zpytsb):
    return zpytsb[0] != "hfui" or zpytsb[-1] == "gri"
def gbi(zpytsb):
    return not nwq(zpytsb)
fyox = Factor("kiv", [DerivedLevel("cals", Transition(nwq, [zpytsb])), DerivedLevel("ozjp", Transition(gbi, [zpytsb]))])
### EXPERIMENT
design=[zpytsb,fyox]
crossing=[fyox]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END