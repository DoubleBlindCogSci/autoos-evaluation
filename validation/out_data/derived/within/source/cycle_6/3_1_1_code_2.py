from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ylflj = Factor("ylflj", ["pegaf","elsv","sqfg","ylfirl","ebyn","fixt","oqpnm","zwuv"])
def is_wblgfh_uryw(ylflj):
    return ylflj == "ebyn"
def is_wblgfh_cajyd(ylflj):
    return ylflj == "elsv"
def is_wblgfh_dbul(ylflj):
    return not (is_wblgfh_uryw(ylflj) or is_wblgfh_cajyd(ylflj))
wblgfh = Factor("wblgfh", [DerivedLevel("uryw", WithinTrial(is_wblgfh_uryw, [ylflj])), DerivedLevel("cajyd", WithinTrial(is_wblgfh_cajyd, [ylflj])), DerivedLevel("dbul", WithinTrial(is_wblgfh_dbul, [ylflj]))])

design=[ylflj,wblgfh]
crossing=[wblgfh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END