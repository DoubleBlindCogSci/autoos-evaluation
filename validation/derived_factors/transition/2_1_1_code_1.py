from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jgcxpk = Factor("jgcxpk", ["caw","yzadyh","tilsa","gowz","yzx","fbiz","fhp"])
def udt(jgcxpk):
    return jgcxpk[0] != "yzadyh" or jgcxpk[-1] == "fbiz"
def xjg(jgcxpk):
    return not udt(jgcxpk)
ymdrz = Factor("yfnul", [DerivedLevel("nroqxs", Transition(udt, [jgcxpk])), DerivedLevel("rszvp", Transition(xjg, [jgcxpk]))])
### EXPERIMENT
design=[jgcxpk,ymdrz]
crossing=[ymdrz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END