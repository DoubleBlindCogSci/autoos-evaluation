from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cfgp= Factor("cfgp", ["zhb","auqymj","yadxcf","foatf","zmuqt","zaydr"])
zotx= Factor("zotx", ["fvqksd","qokmyw","mvhnjp","spmw","ldmd","gndf","gob"])

def is_oum_uhrgs(cfgp, zotx):
    return cfgp[0] != "yadxcf" and zotx[0] != "ldmd"
def is_oum_vrqyuv(cfgp, zotx):
    return not is_oum_uhrgs(cfgp, zotx)
oum= Factor("oum", [DerivedLevel("uhrgs", Transition(is_oum_uhrgs, [cfgp, zotx])), DerivedLevel("vrqyuv", Transition(is_oum_vrqyuv, [cfgp, zotx]))])


design=[cfgp,zotx,oum]
crossing=[oum]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
