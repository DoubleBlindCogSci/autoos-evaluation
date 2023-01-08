from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bkko = Factor("bkko", ["kgps","znme","mal","mjfv","hypcpg","xtxxh","dpvo"])
def hucjb(bkko):
    return bkko[0] == "dpvo" or bkko[-1] != "mal"
def sfzfu(bkko):
    return not hucjb(bkko)
kont = DerivedLevel("vipacv", Transition(hucjb, [bkko]))
txav = DerivedLevel("vrumbw", Transition(sfzfu, [bkko]))
hmr = Factor("fhgy", [kont, txav])

### EXPERIMENT
design=[bkko,hmr]
crossing=[hmr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END