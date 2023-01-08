from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cltze = Factor("cltze", ["gqqyk","ewjlag","gwoqns","kib","reqqt","btbfe"])
def xnbpop(cltze):
    return cltze[-1] != "reqqt" and cltze[0] == "btbfe"
def ljngf(cltze):
    return not xnbpop(cltze)
brsj = Factor("auvl", [DerivedLevel("iyqnrx", Window(xnbpop, [cltze],2,1)), DerivedLevel("zbaapf", Window(ljngf, [cltze],2,1))])
### EXPERIMENT
design=[cltze,brsj]
crossing=[brsj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END