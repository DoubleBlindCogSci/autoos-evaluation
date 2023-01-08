from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bhlc = Factor("bhlc", ["ytqhf","rma","ilbt","aiyuj","pwo","jno","rxrnp"])
jqwma = Factor("jqwma", ["tmc","elrer","tezuge","xbkz","imbn"])
def is_yva_ecbu(bhlc, jqwma):
    return bhlc != "ilbt" or jqwma == "tezuge"
def is_yva_lugj(bhlc, jqwma):
    return not is_yva_ecbu(bhlc, jqwma)
yva= Factor("yva", [DerivedLevel("ecbu", WithinTrial(is_yva_ecbu, [bhlc, jqwma])), DerivedLevel("lugj", WithinTrial(is_yva_lugj, [bhlc, jqwma]))])

design=[bhlc,jqwma,yva]
crossing=[yva]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
