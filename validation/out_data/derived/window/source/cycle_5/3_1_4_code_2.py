from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dmjbcm = Factor("dmjbcm", ["trcg","optgu","aahlc","udmppq","kiywln","hza"])
def is_hhvfof_aljh(dmjbcm):
    return dmjbcm[-2] == "kiywln" and dmjbcm[-1] != "kiywln"
def is_hhvfof_mdvn(dmjbcm):
    return dmjbcm[-2] != "kiywln" and dmjbcm[-1] == "aahlc"
def is_hhvfof_qie(dmjbcm):
    return not (is_hhvfof_aljh(dmjbcm) or is_hhvfof_mdvn(dmjbcm))
hhvfof = Factor("hhvfof", [DerivedLevel("aljh", Window(is_hhvfof_aljh, [dmjbcm], 3, 1)), DerivedLevel("mdvn", Window(is_hhvfof_mdvn, [dmjbcm], 3, 1)), DerivedLevel("qie", Window(is_hhvfof_qie, [dmjbcm], 3, 1))])

design=[dmjbcm,hhvfof]
crossing=[hhvfof]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END