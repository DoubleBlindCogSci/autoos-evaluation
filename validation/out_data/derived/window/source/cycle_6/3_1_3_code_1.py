from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ltb = Factor("ltb", ["ydna","rsx","dlpyg","zjrod","dfy","vdlgyc"])
def bjwk(ltb):
     return ltb[-1] == "dfy" and not ltb[-2] == "dfy"
def wju(ltb):
     return not "dfy" == ltb[-1] and  "ydna" == ltb[-2]
def gegwoa(ltb):
     return (ltb[-1] != "dfy") and (not wju(ltb))
acek = Factor("hva", [DerivedLevel("gziav", Window(bjwk, [ltb],3,1)), DerivedLevel("zldu", Window(wju, [ltb],3,1)),DerivedLevel("kycwij", Window(gegwoa, [ltb],3,1))])
### EXPERIMENT
design=[ltb,acek]
crossing=[acek]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END