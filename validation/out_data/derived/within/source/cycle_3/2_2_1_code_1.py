from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bhlc = Factor("bhlc", ["ytqhf","rma","ilbt","aiyuj","pwo","jno","rxrnp"])
jqwma = Factor("jqwma", ["tmc","elrer","tezuge","xbkz","imbn"])
def ezz(bhlc, jqwma):
    return bhlc != "ilbt" or jqwma == "tezuge"
def bjanw(bhlc,jqwma):
    return not ezz(bhlc, jqwma)
rmedy = DerivedLevel("ecbu", WithinTrial(ezz, [bhlc, jqwma]))
hnkvbp = DerivedLevel("lugj", WithinTrial(bjanw, [bhlc, jqwma]))
fpvufl = Factor("yva", [rmedy, hnkvbp])

### EXPERIMENT
design=[bhlc,jqwma,fpvufl]
crossing=[fpvufl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END