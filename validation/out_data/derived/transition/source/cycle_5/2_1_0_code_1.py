from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uuio = Factor("uuio", ["qceyif","kzktl","hcq","tegzat","xyakx"])
def lmpfm(uuio):
    return uuio[0] != "xyakx" and uuio[-1] == "qceyif"
def dzirej(uuio):
    return not (uuio[0] != "xyakx") or not (uuio[0] == "qceyif")
inmgt = DerivedLevel("utg", Transition(lmpfm, [uuio]))
sbynvl = DerivedLevel("ytn", Transition(dzirej, [uuio]))
lrzh = Factor("dbo", [inmgt, sbynvl])

### EXPERIMENT
design=[uuio,lrzh]
crossing=[lrzh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END