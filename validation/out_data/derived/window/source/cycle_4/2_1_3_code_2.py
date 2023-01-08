from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yctm = Factor("yctm", ["wuvy","gdjl","itmmu","ucfi","vhew","akgbzo","pav"])
def is_rvdi_uqzei(yctm):
    return yctm[-1] != "vhew" and yctm[0] == "akgbzo"
def is_rvdi_zlku(yctm):
    return not is_rvdi_uqzei(yctm)
rvdi = Factor("rvdi", [DerivedLevel("uqzei", Window(is_rvdi_uqzei, [yctm], 2, 1)), DerivedLevel("zlku", Window(is_rvdi_zlku, [yctm], 2, 1))])

design=[yctm,rvdi]
crossing=[rvdi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END