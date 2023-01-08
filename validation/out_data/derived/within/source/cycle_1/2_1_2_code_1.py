from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
awjcy = Factor("awjcy", ["sml","cvrrs","mkk","ymnnn","xcjv"])
def xholx(awjcy):
    return awjcy != "cvrrs" and awjcy == "sml"
def qim(awjcy):
    return not xholx(awjcy)
rczub = Factor("asxjlq", [DerivedLevel("fvhc", WithinTrial(xholx, [awjcy])), DerivedLevel("zicnbq", WithinTrial(qim, [awjcy]))])
### EXPERIMENT
design=[awjcy,rczub]
crossing=[rczub]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END