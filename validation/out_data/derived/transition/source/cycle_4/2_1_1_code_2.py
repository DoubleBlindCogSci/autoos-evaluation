from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bkko = Factor("bkko", ["kgps","znme","mal","mjfv","hypcpg","xtxxh","dpvo"])
def is_fhgy_vipacv(bkko):
    return bkko[0] == "dpvo" or bkko[-1] != "mal"
def is_fhgy_vrumbw(bkko):
    return not is_fhgy_vipacv(bkko)
fhgy= Factor("fhgy", [DerivedLevel("vipacv", Transition(is_fhgy_vipacv, [bkko])), DerivedLevel("vrumbw", Transition(is_fhgy_vrumbw, [bkko]))])

design=[bkko,fhgy]
crossing=[fhgy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END