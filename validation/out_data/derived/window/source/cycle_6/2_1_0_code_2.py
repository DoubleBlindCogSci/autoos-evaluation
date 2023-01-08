from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kxqpc = Factor("kxqpc", ["tujrzb","lxbi","fmvgl","whid","nuck"])
def is_cokbzu_mzlm(kxqpc):
    return kxqpc[-1] != "lxbi" and kxqpc[-2] != "whid"
def is_cokbzu_sobrk(kxqpc):
    return not is_cokbzu_mzlm(kxqpc)
cokbzu = Factor("cokbzu", [DerivedLevel("mzlm", Window(is_cokbzu_mzlm, [kxqpc], 3, 1)), DerivedLevel("sobrk", Window(is_cokbzu_sobrk, [kxqpc], 3, 1))])

design=[kxqpc,cokbzu]
crossing=[cokbzu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END