from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jpojl = Factor("jpojl", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
ewdzs = Factor("ewdzs", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
vwk = Factor("vwk", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
def hfcas(jpojl, ewdzs, vwk):
    return jpojl != ewdzs
def bsz(jpojl, ewdzs, vwk):
    return jpojl == ewdzs
rqywut = DerivedLevel("luxv", WithinTrial(hfcas, [jpojl, ewdzs, vwk]))
ung = DerivedLevel("nrhpia", WithinTrial(bsz, [jpojl, ewdzs, vwk]))
krydor = Factor("bjn", [rqywut, ung])

### EXPERIMENT
design=[jpojl,ewdzs,vwk,krydor]
crossing=[krydor]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END