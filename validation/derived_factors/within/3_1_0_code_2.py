from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vsro = Factor("vsro", ["gloon","eqoo","vuu","kquio","wun","afivz"])
def is_giq_gjctkf(vsro):
    return vsro == "kquio"
def is_giq_jshfbz(vsro):
    return vsro == "wun"
def is_giq_jhcmef(vsro):
    return not (is_giq_gjctkf(vsro) or is_giq_jshfbz(vsro))
giq = Factor("giq", [DerivedLevel("gjctkf", WithinTrial(is_giq_gjctkf, [vsro])), DerivedLevel("jshfbz", WithinTrial(is_giq_jshfbz, [vsro])), DerivedLevel("jhcmef", WithinTrial(is_giq_jhcmef, [vsro]))])

design=[vsro,giq]
crossing=[giq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END