from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pva = Factor("pva", ["uzzge","chl","bemjj","tzm","qxlo"])
def qyy(pva):
    return pva != "uzzge" and pva != "qxlo"
def yuuxh(pva):
    return not (pva != "uzzge") or not (pva != "qxlo")
jdf = DerivedLevel("lqfnc", WithinTrial(qyy, [pva]))
ggri = DerivedLevel("elroif", WithinTrial(yuuxh, [pva]))
ewnxcc = Factor("zolw", [jdf, ggri])

### EXPERIMENT
design=[pva,ewnxcc]
crossing=[ewnxcc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END