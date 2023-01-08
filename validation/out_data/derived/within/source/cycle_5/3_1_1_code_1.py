from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ukoef = Factor("ukoef", ["cbm","sfqaa","yzki","aylq","fda","mawft","wte","acy"])
def smbel(ukoef):
     return "sfqaa" == ukoef
def lgcdbn(ukoef):
     return ukoef == "yzki"
def ifpjq(ukoef):
     return (not smbel(ukoef)) and (not lgcdbn(ukoef))
lrmqzr = DerivedLevel("gxnngf", WithinTrial(smbel, [ukoef]))
spyexi = DerivedLevel("bvmj", WithinTrial(lgcdbn, [ukoef]))
swvx = DerivedLevel("dzvt", WithinTrial(ifpjq, [ukoef]))
deoz = Factor("ietmq", [lrmqzr, spyexi, swvx])

### EXPERIMENT
design=[ukoef,deoz]
crossing=[deoz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END