from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yqdhvs = Factor("yqdhvs", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
jfb = Factor("jfb", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
zepq = Factor("zepq", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
def is_hsus_jhu(yqdhvs, jfb, zepq):
    return yqdhvs[0] != jfb[-1] or yqdhvs[-1] != zepq[0]
def is_hsus_fxycq(yqdhvs, jfb, zepq):
    return not is_hsus_jhu(yqdhvs, jfb, zepq)
hsus = Factor("hsus", [DerivedLevel("jhu", Transition(is_hsus_jhu, [yqdhvs, jfb, zepq])), DerivedLevel("fxycq", Transition(is_hsus_fxycq, [yqdhvs, jfb, zepq]))])

design=[yqdhvs,jfb,zepq,hsus]
crossing=[hsus]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END