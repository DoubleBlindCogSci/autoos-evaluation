from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
umpyn = Factor("umpyn", ["qex","icexol","bsxpyh","btmdcl","ttkvg","cfm","zqnooi"])
jqdtso = Factor("jqdtso", ["khn","kpmej","iloa","wfhfoe","kqzey"])
def is_tzb_ypm(umpyn, jqdtso):
    return umpyn[0] != "btmdcl" or jqdtso[0] == "wfhfoe"
def is_tzb_nkhll(umpyn, jqdtso):
    return not is_tzb_ypm(umpyn, jqdtso)
tzb = Factor("tzb", [DerivedLevel("ypm", Transition(is_tzb_ypm, [umpyn, jqdtso])), DerivedLevel("nkhll", Transition(is_tzb_nkhll, [umpyn, jqdtso]))])

design=[umpyn,jqdtso,tzb]
crossing=[tzb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END