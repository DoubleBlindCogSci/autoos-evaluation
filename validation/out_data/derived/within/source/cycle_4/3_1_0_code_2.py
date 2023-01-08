from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pgyrs = Factor("pgyrs", ["lnv","rqsz","ehluve","tne","xme","fasal","nmd"])
def is_hhvbfn_gobci(pgyrs):
    return pgyrs == "xme"
def is_hhvbfn_cgp(pgyrs):
    return pgyrs == "nmd"
def is_hhvbfn_bnhoc(pgyrs):
    return not (is_hhvbfn_gobci(pgyrs) or is_hhvbfn_cgp(pgyrs))
hhvbfn= Factor("hhvbfn", [DerivedLevel("gobci", WithinTrial(is_hhvbfn_gobci, [pgyrs])), DerivedLevel("cgp", WithinTrial(is_hhvbfn_cgp, [pgyrs])), DerivedLevel("bnhoc", WithinTrial(is_hhvbfn_bnhoc, [pgyrs]))])

design=[pgyrs,hhvbfn]
crossing=[hhvbfn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END