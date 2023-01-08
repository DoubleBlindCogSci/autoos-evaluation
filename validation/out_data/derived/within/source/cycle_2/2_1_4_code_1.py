from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
spuf = Factor("spuf", ["yuyfqp","hzj","aylik","iwydnx","gcxdph","tsvw"])
def iarcb(spuf):
    return spuf == "tsvw" and spuf == "yuyfqp"
def cwc(spuf):
    return not iarcb(spuf)
mlee = Factor("swgls", [DerivedLevel("sylfgy", WithinTrial(iarcb, [spuf])), DerivedLevel("zmdb", WithinTrial(cwc, [spuf]))])
### EXPERIMENT
design=[spuf,mlee]
crossing=[mlee]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END