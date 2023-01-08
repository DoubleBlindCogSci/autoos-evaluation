from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
spuf= Factor("spuf", ["yuyfqp","hzj","aylik","iwydnx","gcxdph","tsvw"])
def is_swgls_sylfgy(spuf):
    return spuf == "tsvw" and spuf == "yuyfqp"
def is_swgls_zmdb(spuf):
    return not is_swgls_sylfgy(spuf)
swgls= Factor("swgls", [DerivedLevel("sylfgy", WithinTrial(is_swgls_sylfgy, [spuf])), DerivedLevel("zmdb", WithinTrial(is_swgls_zmdb, [spuf]))])

design=[spuf, swgls]
crossing=[swgls]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
