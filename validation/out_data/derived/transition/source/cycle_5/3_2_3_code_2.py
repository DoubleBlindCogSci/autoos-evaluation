from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oimbuy = Factor("oimbuy", ["zanj","byz","tcu","yhvjmi","eqmrf","aga","sykg"])
hppah = Factor("hppah", ["fiviro","eump","wmggtq","ewhvwh","glfbm","yvuvce","lsgw","skrxzy"])
def is_pklwju_pspk(oimbuy, hppah):
    return oimbuy[-1] == "sykg" and hppah[0] != "eump"
def is_pklwju_gelwv(oimbuy, hppah):
    return oimbuy[-1] != "sykg" and hppah[0] == "eump"
def is_pklwju_sswak(oimbuy, hppah):
    return not (is_pklwju_pspk(oimbuy, hppah) or is_pklwju_gelwv(oimbuy, hppah))
pklwju = Factor("pklwju", [DerivedLevel("pspk", Transition(is_pklwju_pspk, [oimbuy, hppah])), DerivedLevel("gelwv", Transition(is_pklwju_gelwv, [oimbuy, hppah])), DerivedLevel("sswak", Transition(is_pklwju_sswak, [oimbuy, hppah]))])

design=[oimbuy,hppah,pklwju]
crossing=[pklwju]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END