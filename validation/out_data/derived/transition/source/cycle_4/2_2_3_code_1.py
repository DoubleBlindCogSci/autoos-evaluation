from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
umpyn = Factor("umpyn", ["qex","icexol","bsxpyh","btmdcl","ttkvg","cfm","zqnooi"])
jqdtso = Factor("jqdtso", ["khn","kpmej","iloa","wfhfoe","kqzey"])
def yejmti(umpyn, jqdtso):
    return umpyn[0] != "btmdcl" or jqdtso[-1] == "wfhfoe"
def xemo(umpyn,jqdtso):
    return not (umpyn[0] != "btmdcl") and jqdtso[-1] != "wfhfoe"
zhaecb = Factor("tzb", [DerivedLevel("ypm", Transition(yejmti, [umpyn, jqdtso])), DerivedLevel("nkhll", Transition(xemo, [umpyn, jqdtso]))])
### EXPERIMENT
design=[umpyn,jqdtso,zhaecb]
crossing=[zhaecb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END