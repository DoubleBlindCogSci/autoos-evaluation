from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uvga = Factor("uvga", ["sus","wveejv","dspvo","wqq","pwne","gnh"])
vinzl = Factor("vinzl", ["ida","hcf","wfw","szed","uhvpm","pwfe"])
def is_xtl_sudue(uvga, vinzl):
    return uvga == "wqq"
def is_xtl_xmjku(uvga, vinzl):
    return uvga != "wqq" and vinzl == "uhvpm"
def is_xtl_cxlk(uvga, vinzl):
    return not (is_xtl_sudue(uvga) or is_xtl_xmjku(uvga, vinzl))
xtl = Factor("xtl", [DerivedLevel("sudue", WithinTrial(is_xtl_sudue, [uvga])), DerivedLevel("xmjku", WithinTrial(is_xtl_xmjku, [uvga, vinzl])), DerivedLevel("cxlk", WithinTrial(is_xtl_cxlk, [uvga, vinzl]))])

design=[uvga,vinzl,xtl]
crossing=[xtl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END