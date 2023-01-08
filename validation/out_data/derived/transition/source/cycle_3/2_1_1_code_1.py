from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
apgpx = Factor("apgpx", ["yjpav","hjyr","bfn","yvhm","hdfrzu","oyg"])
def letko(apgpx):
    return apgpx[0] == "hdfrzu" or apgpx[-1] == "yvhm"
def rhse(apgpx):
    return not letko(apgpx)
dhxk = Factor("ltb", [DerivedLevel("euacj", Transition(letko, [apgpx])), DerivedLevel("ctra", Transition(rhse, [apgpx]))])
### EXPERIMENT
design=[apgpx,dhxk]
crossing=[dhxk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END