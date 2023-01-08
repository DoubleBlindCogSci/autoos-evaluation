from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ukoef = Factor("ukoef", ["cbm","sfqaa","yzki","aylq","fda","mawft","wte","acy"])
def is_ietmq_gxnngf(ukoef):
    return ukoef == "sfqaa"
def is_ietmq_bvmj(ukoef):
    return ukoef == "yzki"
def is_ietmq_dzvt(ukoef):
    return not (is_ietmq_gxnngf(ukoef) or is_ietmq_bvmj(ukoef))
ietmq = Factor("ietmq", [DerivedLevel("gxnngf", WithinTrial(is_ietmq_gxnngf, [ukoef])), DerivedLevel("bvmj", WithinTrial(is_ietmq_bvmj, [ukoef])), DerivedLevel("dzvt", WithinTrial(is_ietmq_dzvt, [ukoef]))])

design=[ukoef,ietmq]
crossing=[ietmq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END