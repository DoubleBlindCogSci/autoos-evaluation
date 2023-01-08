from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xjkwdl = Factor("xjkwdl", ["mmji","amld","kjw","cylzzt","duein","chne","zqjd","howz"])
def is_chqiby_azfana(xjkwdl):
    return xjkwdl == "chne"
def is_chqiby_eqs(xjkwdl):
    return xjkwdl == "cylzzt"
def is_chqiby_dnfd(xjkwdl):
    return not (is_chqiby_azfana(xjkwdl) or is_chqiby_eqs(xjkwdl))
chqiby= Factor("chqiby", [DerivedLevel("azfana", WithinTrial(is_chqiby_azfana, [xjkwdl])), DerivedLevel("eqs", WithinTrial(is_chqiby_eqs, [xjkwdl])), DerivedLevel("dnfd", WithinTrial(is_chqiby_dnfd, [xjkwdl]))])

design=[xjkwdl,chqiby]
crossing=[chqiby]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
