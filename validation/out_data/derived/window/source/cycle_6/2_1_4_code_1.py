from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ibjrq = Factor("ibjrq", ["pex","spfgp","bccih","medubx","xvar","mgiaz"])
def poyoz(ibjrq):
    return ibjrq[-2] == "mgiaz" and ibjrq[-1] != "pex"
def hfu(ibjrq):
    return ibjrq[-2] != "mgiaz" or ibjrq[-1] == "pex"
gclwgu = Factor("aaur", [DerivedLevel("dlvyco", Window(poyoz, [ibjrq],3,1)), DerivedLevel("kpo", Window(hfu, [ibjrq],3,1))])
### EXPERIMENT
design=[ibjrq,gclwgu]
crossing=[gclwgu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END