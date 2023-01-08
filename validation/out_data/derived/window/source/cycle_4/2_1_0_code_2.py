from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hxtcdr = Factor("hxtcdr", ["qvoo","bmx","tjlgc","ozz","wdedml","bwrbl"])
def is_yaeoo_vtwb(hxtcdr):
    return hxtcdr[-3] != "tjlgc" or hxtcdr[0] == "bwrbl"
def is_yaeoo_tzocpv(hxtcdr):
    return not is_yaeoo_vtwb(hxtcdr)
yaeoo= Factor("yaeoo", [DerivedLevel("vtwb", Window(is_yaeoo_vtwb, [hxtcdr], 4, 1)), DerivedLevel("tzocpv", Window(is_yaeoo_tzocpv, [hxtcdr], 4, 1))])

design=[hxtcdr,yaeoo]
crossing=[yaeoo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END