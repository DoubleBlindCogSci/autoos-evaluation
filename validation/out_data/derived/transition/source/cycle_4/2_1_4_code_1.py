from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vsxv = Factor("vsxv", ["drgme","mkvx","lgzcfj","bmgf","fnoe","fzsngf","thvsaa"])
def zyj(vsxv):
    return vsxv[0] != "mkvx" or vsxv[-1] == "drgme"
def fmec(vsxv):
    return not (vsxv[0] != "mkvx") and not (vsxv[0] == "drgme")
ywuu = DerivedLevel("gtz", Transition(zyj, [vsxv]))
fwis = DerivedLevel("xdnx", Transition(fmec, [vsxv]))
gyikro = Factor("yasz", [ywuu, fwis])

### EXPERIMENT
design=[vsxv,gyikro]
crossing=[gyikro]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END