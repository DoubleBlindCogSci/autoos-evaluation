from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
ptxf = Factor("ptxf", ["nsmjwr", "iqbzt"])
fthd = Factor("fthd", ["fuezsy", "ddldqs"])
lln = Factor("lln", ["nsmjwr", "iqbzt"])
lfcap = Factor("lfcap", ["fuezsy", "ddldqs"])
tku = Factor("tku", ["qupefs", "nbo"])
rvpgn = Factor("rvpgn", ["pysk", "ihgxhj"])
def ihy (lfcap, fthd):
    return lfcap == fthd
def jfenxo (lfcap, fthd):
    return not ihy(lfcap, fthd)
hjkr = Factor("hjkr", [DerivedLevel("xwex", WithinTrial(ihy, [lfcap, fthd])), DerivedLevel("cidq", WithinTrial(jfenxo, [lfcap, fthd]))])
design=[hjkr,ptxf,fthd,lln,lfcap,tku,rvpgn]
constraints=[]
crossing=[fthd,tku]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_1_0"))
