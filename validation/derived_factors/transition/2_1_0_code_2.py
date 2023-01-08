from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fgcn = Factor("fgcn", ["pdxnwx","wjq","jdrx","ezi","ncau","cuqrnk","irycp"])
def is_ypeh_jznqr(fgcn):
    return fgcn[0] == "cuqrnk" and fgcn[-1] == "ncau"
def is_ypeh_ylnb(fgcn):
    return not is_ypeh_jznqr(fgcn)
ypeh = Factor("ypeh", [DerivedLevel("jznqr", Transition(is_ypeh_jznqr, [fgcn])), DerivedLevel("ylnb", Transition(is_ypeh_ylnb, [fgcn]))])

design=[fgcn,ypeh]
crossing=[ypeh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END