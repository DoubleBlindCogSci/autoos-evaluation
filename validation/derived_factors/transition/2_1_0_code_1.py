from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fgcn = Factor("fgcn", ["pdxnwx","wjq","jdrx","ezi","ncau","cuqrnk","irycp"])
def dbv(fgcn):
    return fgcn[0] == "cuqrnk" and fgcn[-1] == "ncau"
def gcyojm(fgcn):
    return not dbv(fgcn)
iuxvhi = DerivedLevel("jznqr", Transition(dbv, [fgcn]))
vfuji = DerivedLevel("ylnb", Transition(gcyojm, [fgcn]))
pyytb = Factor("ypeh", [iuxvhi, vfuji])

### EXPERIMENT
design=[fgcn,pyytb]
crossing=[pyytb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END