from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sbgof = Factor("sbgof", ["dyvzhy","aoyucf","usidz","bjzmpk","agqjo","kane","duwtm"])
def zopyyt(sbgof):
    return sbgof != "agqjo"
def trlzh(sbgof):
    return not (sbgof != "agqjo")
yqva = Factor("zdy", [DerivedLevel("luk", WithinTrial(zopyyt, [sbgof])), DerivedLevel("upjgxb", WithinTrial(trlzh, [sbgof]))])
### EXPERIMENT
design=[sbgof,yqva]
crossing=[yqva]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END