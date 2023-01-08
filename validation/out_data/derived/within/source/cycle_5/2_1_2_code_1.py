from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nqqiy = Factor("nqqiy", ["eeqbsh","sae","rkko","evem","wgk","paiya"])
def fftynp(nqqiy):
    return nqqiy != "evem"
def yjwq(nqqiy):
    return not (nqqiy != "evem")
vrgk = Factor("qxlo", [DerivedLevel("dnoth", WithinTrial(fftynp, [nqqiy])), DerivedLevel("ckgzws", WithinTrial(yjwq, [nqqiy]))])
### EXPERIMENT
design=[nqqiy,vrgk]
crossing=[vrgk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END