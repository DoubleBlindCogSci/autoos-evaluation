from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eyffzz = Factor("eyffzz", ["qac","kkbcvv","hqe","upgqu","ccczq","wfx","fgacg"])
def vrc(eyffzz):
    return eyffzz != "upgqu"
def bmg(eyffzz):
    return eyffzz == "upgqu"
tatr = DerivedLevel("arby", WithinTrial(vrc, [eyffzz]))
hss = DerivedLevel("teft", WithinTrial(bmg, [eyffzz]))
zsym = Factor("itt", [tatr, hss])

### EXPERIMENT
design=[eyffzz,zsym]
crossing=[zsym]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END