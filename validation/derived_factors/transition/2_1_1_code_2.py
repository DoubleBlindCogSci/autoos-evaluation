from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jgcxpk = Factor("jgcxpk", ["caw","yzadyh","tilsa","gowz","yzx","fbiz","fhp"])
def is_yfnul_nroqxs(jgcxpk):
    return jgcxpk[0] != "yzadyh" or jgcxpk[-1] == "fbiz"
def is_yfnul_rszvp(jgcxpk):
    return not is_yfnul_nroqxs(jgcxpk)
yfnul = Factor("yfnul", [DerivedLevel("nroqxs", Transition(is_yfnul_nroqxs, [jgcxpk])), DerivedLevel("rszvp", Transition(is_yfnul_rszvp, [jgcxpk]))])

design=[jgcxpk,yfnul]
crossing=[yfnul]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END