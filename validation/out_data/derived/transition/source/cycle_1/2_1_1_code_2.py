from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
exii= Factor("exii", ["fxb","ynmp","repr","znltjq","qsjul","irdbw"])
def is_ujsa_bsjhjv(exii):
    return exii[0] != "repr" and exii[0] != "irdbw"
def is_ujsa_yaqd(exii):
    return not is_ujsa_bsjhjv(exii)
ujsa= Factor("ujsa", [DerivedLevel("bsjhjv", Transition(is_ujsa_bsjhjv, [exii])), DerivedLevel("yaqd", Transition(is_ujsa_yaqd, [exii]))])

design=[exii,ujsa]
crossing=[ujsa]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
