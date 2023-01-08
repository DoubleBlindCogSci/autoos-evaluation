from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tglvmx = Factor("tglvmx", ["tkon","nzbpe","eyjenc","fkjtmj","pulu","uls","hkfa"])
def is_brbmt_prtnf(tglvmx):
    return tglvmx[0] == "pulu" and tglvmx[-1] != "tkon"
def is_brbmt_racrn(tglvmx):
    return tglvmx[0] != "pulu" and tglvmx[-1] == "tkon"
def is_brbmt_olao(tglvmx):
    return not (is_brbmt_prtnf(tglvmx) or is_brbmt_racrn(tglvmx))
brbmt = Factor("brbmt", [DerivedLevel("prtnf", Transition(is_brbmt_prtnf, [tglvmx])), DerivedLevel("racrn", Transition(is_brbmt_racrn, [tglvmx])), DerivedLevel("olao", Transition(is_brbmt_olao, [tglvmx]))])

design=[tglvmx,brbmt]
crossing=[brbmt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END