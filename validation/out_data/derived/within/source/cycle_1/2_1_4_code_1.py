from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cnb = Factor("cnb", ["yxdvh","gwd","rdg","kvstg","dbcw","erk"])
def cdyyv(cnb):
    return cnb != "erk" and cnb != "rdg"
def btk(cnb):
    return not cdyyv(cnb)
mtre = Factor("vmehak", [DerivedLevel("zhj", WithinTrial(cdyyv, [cnb])), DerivedLevel("fuhh", WithinTrial(btk, [cnb]))])
### EXPERIMENT
design=[cnb,mtre]
crossing=[mtre]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END