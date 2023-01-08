from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yqdhvs = Factor("yqdhvs", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
jfb = Factor("jfb", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
zepq = Factor("zepq", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
def bzh(yqdhvs, jfb, zepq):
    return yqdhvs[0] != jfb[-1] or yqdhvs[-1] != zepq[0]
def quvv(yqdhvs, jfb, zepq):
    return yqdhvs[0] == jfb[-1] and yqdhvs[-1] == zepq[0]
kwpbs = DerivedLevel("jhu", Transition(bzh, [yqdhvs, jfb, zepq]))
obwjl = DerivedLevel("fxycq", Transition(quvv, [yqdhvs, jfb, zepq]))
wyhxus = Factor("hsus", [kwpbs, obwjl])

### EXPERIMENT
design=[yqdhvs,jfb,zepq,wyhxus]
crossing=[wyhxus]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END