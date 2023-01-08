from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
swpbw = Factor("swpbw", ["gxqviy","kouncc","ywgbc","tellq","pglh","gbxc"])
def is_xjf_cvw(swpbw):
    return swpbw == "ywgbc"
def is_xjf_dbh(swpbw):
    return swpbw == "kouncc"
def is_xjf_ycnqcv(swpbw):
    return not (is_xjf_cvw(swpbw) or is_xjf_dbh(swpbw))
xjf = Factor("xjf", [DerivedLevel("cvw", WithinTrial(is_xjf_cvw, [swpbw])), DerivedLevel("dbh", WithinTrial(is_xjf_dbh, [swpbw])), DerivedLevel("ycnqcv", WithinTrial(is_xjf_ycnqcv, [swpbw]))])

design=[swpbw,xjf]
crossing=[xjf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END