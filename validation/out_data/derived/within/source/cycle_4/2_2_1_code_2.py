from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qewi = Factor("qewi", ["itopo","shnnlm","gnsc","isdqw","kao","irvbtr"])
aeghx = Factor("aeghx", ["atity","tbd","balz","rdtvt","hex"])
def is_dhddg_jupn(qewi, aeghx):
    return qewi != "isdqw" or aeghx != "atity"
def is_dhddg_laphw(qewi, aeghx):
    return not is_dhddg_jupn(qewi, aeghx)
dhddg= Factor("dhddg", [DerivedLevel("jupn", WithinTrial(is_dhddg_jupn, [qewi, aeghx])), DerivedLevel("laphw", WithinTrial(is_dhddg_laphw, [qewi, aeghx]))])

design=[qewi,aeghx,dhddg]
crossing=[dhddg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END