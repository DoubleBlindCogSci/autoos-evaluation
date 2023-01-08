from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kxqpc = Factor("kxqpc", ["tujrzb","lxbi","fmvgl","whid","nuck"])
def giug(kxqpc):
    return kxqpc[-1] != "lxbi" and kxqpc[-2] != "whid"
def hrizxg(kxqpc):
    return not giug(kxqpc)
nklk = Factor("cokbzu", [DerivedLevel("mzlm", Window(giug, [kxqpc],3,1)), DerivedLevel("sobrk", Window(hrizxg, [kxqpc],3,1))])
### EXPERIMENT
design=[kxqpc,nklk]
crossing=[nklk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END