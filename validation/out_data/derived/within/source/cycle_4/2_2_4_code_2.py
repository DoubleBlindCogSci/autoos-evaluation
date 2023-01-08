from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jpojl = Factor("jpojl", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
ewdzs = Factor("ewdzs", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
vwk = Factor("vwk", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
def is_bjn_luxv(jpojl, ewdzs, vwk):
    return jpojl != ewdzs
def is_bjn_nrhpia(jpojl, ewdzs, vwk):
    return not is_bjn_luxv(jpojl, ewdzs, vwk)
bjn = Factor("bjn", [DerivedLevel("luxv", WithinTrial(is_bjn_luxv, [jpojl, ewdzs, vwk])), DerivedLevel("nrhpia", WithinTrial(is_bjn_nrhpia, [jpojl, ewdzs, vwk]))])

design=[jpojl,ewdzs,vwk,bjn]
crossing=[bjn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END