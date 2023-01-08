from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vsxv = Factor("vsxv", ["drgme","mkvx","lgzcfj","bmgf","fnoe","fzsngf","thvsaa"])
def is_yasz_gtz(vsxv):
    return vsxv[0] != "mkvx" or vsxv[-1] == "drgme"
def is_yasz_xdnx(vsxv):
    return not is_yasz_gtz(vsxv)
yasz = Factor("yasz", [DerivedLevel("gtz", Transition(is_yasz_gtz, [vsxv])), DerivedLevel("xdnx", Transition(is_yasz_xdnx, [vsxv]))])

design=[vsxv,yasz]
crossing=[yasz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END