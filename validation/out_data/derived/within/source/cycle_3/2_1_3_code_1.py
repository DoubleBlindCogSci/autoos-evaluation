from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mox = Factor("mox", ["ynja","mecuo","eps","qkyw","lpbn","lrslse"])
def lodix(mox):
    return mox == "ynja"
def ryzfs(mox):
    return mox != "ynja"
ytsfj = DerivedLevel("mzz", WithinTrial(lodix, [mox]))
ezczk = DerivedLevel("ehdomd", WithinTrial(ryzfs, [mox]))
uzde = Factor("bkns", [ytsfj, ezczk])

### EXPERIMENT
design=[mox,uzde]
crossing=[uzde]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END