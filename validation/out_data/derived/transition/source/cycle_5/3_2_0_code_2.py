from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
etbwc = Factor("etbwc", ["vng","lrcjcy","otkqu","lih","lql","kic","evkwk"])
xpzx = Factor("xpzx", ["rwa","wmkbw","drfacm","zuhuen","tlxb","kdoe","dgtt"])
def is_itt_mhi(etbwc, xpzx):
    return etbwc[-1] == "otkqu" and xpzx[0] != "drfacm"
def is_itt_zjkjh(etbwc, xpzx):
    return etbwc[-1] != "otkqu" and xpzx[0] == "drfacm"
def is_itt_mktwdr(etbwc, xpzx):
    return not (is_itt_mhi(etbwc, xpzx) or is_itt_zjkjh(etbwc, xpzx))
itt = Factor("itt", [DerivedLevel("mhi", Transition(is_itt_mhi, [etbwc, xpzx])), DerivedLevel("zjkjh", Transition(is_itt_zjkjh, [etbwc, xpzx])), DerivedLevel("mktwdr", Transition(is_itt_mktwdr, [etbwc, xpzx]))])

design=[etbwc,xpzx,itt]
crossing=[itt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END