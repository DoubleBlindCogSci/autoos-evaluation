from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pgyrs = Factor("pgyrs", ["lnv","rqsz","ehluve","tne","xme","fasal","nmd"])
def kevfqr(pgyrs):
     return "xme" == pgyrs
def obho(pgyrs):
     return "nmd" == pgyrs
def txzbjo(pgyrs):
     return (pgyrs != "xme") and (not obho(pgyrs))
kboobd = Factor("hhvbfn", [DerivedLevel("gobci", WithinTrial(kevfqr, [pgyrs])), DerivedLevel("cgp", WithinTrial(obho, [pgyrs])),DerivedLevel("bnhoc", WithinTrial(txzbjo, [pgyrs]))])
### EXPERIMENT
design=[pgyrs,kboobd]
crossing=[kboobd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END