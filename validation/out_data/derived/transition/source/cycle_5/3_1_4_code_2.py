from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kcjg = Factor("kcjg", ["xal","yxlmog","nepg","nft","wdnjd","wzx","ltwgre","bbj"])
def is_fpzy_ivdsvt(kcjg):
    return kcjg[0] == "wzx" and kcjg[-1] != "nft"
def is_fpzy_ngq(kcjg):
    return kcjg[0] != "wzx" and kcjg[-1] == "nft"
def is_fpzy_enjasj(kcjg):
    return not (is_fpzy_ivdsvt(kcjg) or is_fpzy_ngq(kcjg))
fpzy = Factor("fpzy", [DerivedLevel("ivdsvt", Transition(is_fpzy_ivdsvt, [kcjg])), DerivedLevel("ngq", Transition(is_fpzy_ngq, [kcjg])), DerivedLevel("enjasj", Transition(is_fpzy_enjasj, [kcjg]))])

design=[kcjg,fpzy]
crossing=[fpzy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END