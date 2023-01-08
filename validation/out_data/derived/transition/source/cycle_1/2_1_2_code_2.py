from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zpytsb= Factor("zpytsb", ["oithj","wed","gri","dyelw","hfui","blmdcz","dhjcm"])
def is_kiv_cals(zpytsb):
    return zpytsb[0] != "hfui" or zpytsb[0] == "gri"
def is_kiv_ozjp(zpytsb):
    return not is_kiv_cals(zpytsb)
kiv= Factor("kiv", [DerivedLevel("cals", Transition(is_kiv_cals, [zpytsb])), DerivedLevel("ozjp", Transition(is_kiv_ozjp, [zpytsb]))])

design=[zpytsb,kiv]
crossing=[kiv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
