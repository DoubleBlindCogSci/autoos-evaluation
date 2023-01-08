from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nygysm = Factor("nygysm", ["migfje","uiq","hgzien","gvi","jsm","suwlo"])
def is_npxjy_cuqrj(nygysm):
    return nygysm[0] == "suwlo" or nygysm[-1] != "hgzien"
def is_npxjy_xnb(nygysm):
    return not is_npxjy_cuqrj(nygysm)
npxjy = Factor("npxjy", [DerivedLevel("cuqrj", Transition(is_npxjy_cuqrj, [nygysm])), DerivedLevel("xnb", Transition(is_npxjy_xnb, [nygysm]))])

design=[nygysm,npxjy]
crossing=[npxjy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END