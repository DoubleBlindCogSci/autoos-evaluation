from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qewi = Factor("qewi", ["itopo","shnnlm","gnsc","isdqw","kao","irvbtr"])
aeghx = Factor("aeghx", ["atity","tbd","balz","rdtvt","hex"])
def umb(qewi, aeghx):
    return qewi != "isdqw" or aeghx != "atity"
def wvkn(qewi,aeghx):
    return not (qewi != "isdqw") and not (aeghx != "atity")
jipe = DerivedLevel("jupn", WithinTrial(umb, [qewi, aeghx]))
oevpqt = DerivedLevel("laphw", WithinTrial(wvkn, [qewi, aeghx]))
jis = Factor("dhddg", [jipe, oevpqt])

### EXPERIMENT
design=[qewi,aeghx,jis]
crossing=[jis]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END