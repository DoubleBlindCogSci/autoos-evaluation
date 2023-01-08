from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fxc = Factor("fxc", ["orpjc","ssfjo","xmpi","erdht","awmuij"])
def dstswm(fxc):
    return fxc[0] == "xmpi" or fxc[-3] != "ssfjo"
def iwpvv(fxc):
    return not dstswm(fxc)
tdrdq = Factor("bovds", [DerivedLevel("micnu", Window(dstswm, [fxc],4,1)), DerivedLevel("zcq", Window(iwpvv, [fxc],4,1))])
### EXPERIMENT
design=[fxc,tdrdq]
crossing=[tdrdq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END