from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uuio = Factor("uuio", ["qceyif","kzktl","hcq","tegzat","xyakx"])
def is_dbo_utg(uuio):
    return uuio[0] != "xyakx" and uuio[-1] == "qceyif"
def is_dbo_ytn(uuio):
    return not is_dbo_utg(uuio)
dbo = Factor("dbo", [DerivedLevel("utg", Transition(is_dbo_utg, [uuio])), DerivedLevel("ytn", Transition(is_dbo_ytn, [uuio]))])

design=[uuio,dbo]
crossing=[dbo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END