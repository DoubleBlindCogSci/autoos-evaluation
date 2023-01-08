from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cltze = Factor("cltze", ["gqqyk","ewjlag","gwoqns","kib","reqqt","btbfe"])
def is_auvl_iyqnrx(cltze):
    return cltze[-1] != "reqqt" and cltze[0] == "btbfe"
def is_auvl_zbaapf(cltze):
    return not is_auvl_iyqnrx(cltze)
auvl = Factor("auvl", [DerivedLevel("iyqnrx", Window(is_auvl_iyqnrx, [cltze], 2, 1)), DerivedLevel("zbaapf", Window(is_auvl_zbaapf, [cltze], 2, 1))])

design=[cltze,auvl]
crossing=[auvl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END