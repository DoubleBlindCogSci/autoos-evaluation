from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tgyp= Factor("tgyp", ["jvy","kamjzt","pxaz","fuboj","wsa","buisa","rekfxs"])
izn= Factor("izn", ["trh","blzzdh","vmc","jxwuke","wxn","iof","depihe"])
def is_hxtank_zvo(tgyp, izn):
    return tgyp[-3] == "wsa" and izn[0] != "vmc"
def is_hxtank_fhvwfc(tgyp, izn):
    return tgyp[-3] != "wsa" and izn[0] == "vmc"
def is_hxtank_bxig(tgyp, izn):
    return not (is_hxtank_zvo(tgyp, izn) or is_hxtank_fhvwfc(tgyp, izn))
hxtank= Factor("hxtank", [DerivedLevel("zvo", Window(is_hxtank_zvo, [tgyp, izn], 4, 1)), DerivedLevel("fhvwfc", Window(is_hxtank_fhvwfc, [tgyp, izn], 4, 1)), DerivedLevel("bxig", Window(is_hxtank_bxig, [tgyp, izn], 4, 1))])

design=[tgyp,izn,hxtank]
crossing=[hxtank]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
