from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ebmygq = Factor("ebmygq", ["xdov","nbpdfx","gowmn","wclq","uidx","sahd"])
def mwoqpl(ebmygq):
    return ebmygq[0] != "xdov" and ebmygq[-1] == "sahd"
def czdy(ebmygq):
    return not (ebmygq[0] != "xdov") or ebmygq[-1] != "sahd"
fmku = Factor("ycd", [DerivedLevel("fvyfn", Transition(mwoqpl, [ebmygq])), DerivedLevel("bxzm", Transition(czdy, [ebmygq]))])
### EXPERIMENT
design=[ebmygq,fmku]
crossing=[fmku]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END