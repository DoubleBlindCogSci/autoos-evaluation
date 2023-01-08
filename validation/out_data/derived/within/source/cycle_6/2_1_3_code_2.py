from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sbgof = Factor("sbgof", ["dyvzhy","aoyucf","usidz","bjzmpk","agqjo","kane","duwtm"])
def is_zdy_luk(sbgof):
    return sbgof != "agqjo"
def is_zdy_upjgxb(sbgof):
    return not is_zdy_luk(sbgof)
zdy = Factor("zdy", [DerivedLevel("luk", WithinTrial(is_zdy_luk, [sbgof])), DerivedLevel("upjgxb", WithinTrial(is_zdy_upjgxb, [sbgof]))])

design=[sbgof,zdy]
crossing=[zdy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END