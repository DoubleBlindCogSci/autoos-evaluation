from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mox = Factor("mox", ["ynja","mecuo","eps","qkyw","lpbn","lrslse"])
def is_bkns_mzz(mox):
    return mox == "ynja"
def is_bkns_ehdomd(mox):
    return not is_bkns_mzz(mox)
bkns= Factor("bkns", [DerivedLevel("mzz", WithinTrial(is_bkns_mzz, [mox])), DerivedLevel("ehdomd", WithinTrial(is_bkns_ehdomd, [mox]))])

design=[mox,bkns]
crossing=[bkns]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
