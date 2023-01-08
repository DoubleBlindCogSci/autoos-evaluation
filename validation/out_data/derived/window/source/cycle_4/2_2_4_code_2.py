from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nlr = Factor("nlr", ["sgsj","vuk","kmpqwy","mazjw","wvwp","yehmq","mqagvn"])
aucsgj = Factor("aucsgj", ["qeurh","mhe","uwqyhv","bfqqa","yiqbx","ysvxtv","pmjk"])
def is_wnegfv_sxu(nlr, aucsgj):
    return nlr[-1] == "yehmq" and aucsgj[-2] == "pmjk"
def is_wnegfv_anfc(nlr, aucsgj):
    return not is_wnegfv_sxu(nlr, aucsgj)
wnegfv = Factor("wnegfv", [DerivedLevel("sxu", Window(is_wnegfv_sxu, [nlr, aucsgj], 3, 1)), DerivedLevel("anfc", Window(is_wnegfv_anfc, [nlr, aucsgj], 3, 1))])

design=[nlr,aucsgj,wnegfv]
crossing=[wnegfv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END