from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xnicu = Factor("xnicu", ["fyf","bwukw","kdtxj","ybpleb","gfqoq","sdpa","uswv"])
def ydpeqi(xnicu):
    return xnicu == "bwukw" and xnicu != "ybpleb"
def xrpzs(xnicu):
    return xnicu != "bwukw" or xnicu == "ybpleb"
djbkle = DerivedLevel("aocks", WithinTrial(ydpeqi, [xnicu]))
uazb = DerivedLevel("uefg", WithinTrial(xrpzs, [xnicu]))
rbrzrw = Factor("kcs", [djbkle, uazb])

### EXPERIMENT
design=[xnicu,rbrzrw]
crossing=[rbrzrw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END