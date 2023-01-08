from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xqnghv = Factor("xqnghv", ["zsiic","lpza","jlz","mnkpeq","pbni","luu","dxops"])
def is_rttpm_svjq(xqnghv):
    return xqnghv[0] == "pbni" or xqnghv[-1] == "lpza"
def is_rttpm_ksmodn(xqnghv):
    return not is_rttpm_svjq(xqnghv)
rttpm = Factor("rttpm", [DerivedLevel("svjq", Transition(is_rttpm_svjq, [xqnghv])), DerivedLevel("ksmodn", Transition(is_rttpm_ksmodn, [xqnghv]))])

design=[xqnghv,rttpm]
crossing=[rttpm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END