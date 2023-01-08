from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ibjrq = Factor("ibjrq", ["pex","spfgp","bccih","medubx","xvar","mgiaz"])
def is_aaur_dlvyco(ibjrq):
    return ibjrq[-2] == "mgiaz" and ibjrq[-1] != "pex"
def is_aaur_kpo(ibjrq):
    return not is_aaur_dlvyco(ibjrq)
aaur = Factor("aaur", [DerivedLevel("dlvyco", Window(is_aaur_dlvyco, [ibjrq], 3, 1)), DerivedLevel("kpo", Window(is_aaur_kpo, [ibjrq], 3, 1))])

design=[ibjrq,aaur]
crossing=[aaur]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END