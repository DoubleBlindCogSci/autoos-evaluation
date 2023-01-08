from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ebmygq = Factor("ebmygq", ["xdov","nbpdfx","gowmn","wclq","uidx","sahd"])
def is_ycd_fvyfn(ebmygq):
    return ebmygq[0] != "xdov" and ebmygq[-1] == "sahd"
def is_ycd_bxzm(ebmygq):
    return not is_ycd_fvyfn(ebmygq)
ycd = Factor("ycd", [DerivedLevel("fvyfn", Transition(is_ycd_fvyfn, [ebmygq])), DerivedLevel("bxzm", Transition(is_ycd_bxzm, [ebmygq]))])

design=[ebmygq,ycd]
crossing=[ycd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END