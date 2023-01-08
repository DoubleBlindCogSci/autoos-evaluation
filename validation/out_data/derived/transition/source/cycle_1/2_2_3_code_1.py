from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cfgp = Factor("cfgp", ["zhb","auqymj","yadxcf","foatf","zmuqt","zaydr"])
zotx = Factor("zotx", ["fvqksd","qokmyw","mvhnjp","spmw","ldmd","gndf","gob"])
def hsuzp(cfgp, zotx):
    return cfgp[0] != "yadxcf" and zotx[-1] != "ldmd"
def qzs(cfgp,zotx):
    return cfgp[0] == "yadxcf" or not (zotx[-1] != "ldmd")
ajvm = DerivedLevel("uhrgs", Transition(hsuzp, [cfgp, zotx]))
cei = DerivedLevel("vrqyuv", Transition(qzs, [cfgp, zotx]))
sje = Factor("oum", [ajvm, cei])

### EXPERIMENT
design=[cfgp,zotx,sje]
crossing=[sje]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END