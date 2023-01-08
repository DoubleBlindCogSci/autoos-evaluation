from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xqnghv = Factor("xqnghv", ["zsiic","lpza","jlz","mnkpeq","pbni","luu","dxops"])
def cdqjs(xqnghv):
    return xqnghv[0] == "pbni" or xqnghv[-1] == "lpza"
def zqzygv(xqnghv):
    return not (xqnghv[0] == "pbni") and not (xqnghv[0] == "lpza")
mxlou = Factor("rttpm", [DerivedLevel("svjq", Transition(cdqjs, [xqnghv])), DerivedLevel("ksmodn", Transition(zqzygv, [xqnghv]))])
### EXPERIMENT
design=[xqnghv,mxlou]
crossing=[mxlou]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END