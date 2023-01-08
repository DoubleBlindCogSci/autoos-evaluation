from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xjkwdl = Factor("xjkwdl", ["mmji","amld","kjw","cylzzt","duein","chne","zqjd","howz"])
def sdizeo(xjkwdl):
     return xjkwdl == "chne"
def utrr(xjkwdl):
     return xjkwdl == "cylzzt"
def xokmmi(xjkwdl):
     return (xjkwdl != "chne") and (not xjkwdl == "cylzzt")
gpvl = DerivedLevel("azfana", WithinTrial(sdizeo, [xjkwdl]))
supqp = DerivedLevel("eqs", WithinTrial(utrr, [xjkwdl]))
nyhivj = DerivedLevel("dnfd", WithinTrial(xokmmi, [xjkwdl]))
bhx = Factor("chqiby", [gpvl, supqp, nyhivj])

### EXPERIMENT
design=[xjkwdl,bhx]
crossing=[bhx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END