from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ush = Factor("ush", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
roxpg = Factor("roxpg", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
rpnreo = Factor("rpnreo", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
def is_mvsa_znieko(ush, roxpg, rpnreo):
    return roxpg == ush
def is_mvsa_oyeh(ush, roxpg, rpnreo):
    return roxpg != ush and rpnreo == ush
def is_mvsa_fhn(ush, roxpg, rpnreo):
    return roxpg != ush and rpnreo != ush
mvsa = Factor("mvsa", [DerivedLevel("znieko", WithinTrial(is_mvsa_znieko, [ush, roxpg, rpnreo])), DerivedLevel("oyeh", WithinTrial(is_mvsa_oyeh, [ush, roxpg, rpnreo])), DerivedLevel("fhn", WithinTrial(is_mvsa_fhn, [ush, roxpg, rpnreo]))])

design=[ush,roxpg,rpnreo,mvsa]
crossing=[mvsa]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END