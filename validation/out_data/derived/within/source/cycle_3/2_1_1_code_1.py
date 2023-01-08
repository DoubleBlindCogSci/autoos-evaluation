from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tmxw = Factor("tmxw", ["mziisl","gyd","twfm","xnr","pxy"])
def shrw(tmxw):
    return tmxw != "twfm" and tmxw == "xnr"
def gjldcm(tmxw):
    return not (tmxw != "twfm") or not (tmxw == "xnr")
tie = Factor("adtfo", [DerivedLevel("nndknu", WithinTrial(shrw, [tmxw])), DerivedLevel("gbatej", WithinTrial(gjldcm, [tmxw]))])
### EXPERIMENT
design=[tmxw,tie]
crossing=[tie]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END