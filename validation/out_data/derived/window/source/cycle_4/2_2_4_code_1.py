from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nlr = Factor("nlr", ["sgsj","vuk","kmpqwy","mazjw","wvwp","yehmq","mqagvn"])
aucsgj = Factor("aucsgj", ["qeurh","mhe","uwqyhv","bfqqa","yiqbx","ysvxtv","pmjk"])
def zzvzgx(nlr, aucsgj):
    return nlr[-1] == "yehmq" and aucsgj[-2] == "pmjk"
def gdg(nlr,aucsgj):
    return nlr[-1] != "yehmq" or not (aucsgj[-2] == "pmjk")
ygigg = Factor("wnegfv", [DerivedLevel("sxu", Window(zzvzgx, [nlr, aucsgj],3,1)), DerivedLevel("anfc", Window(gdg, [nlr, aucsgj],3,1))])
### EXPERIMENT
design=[nlr,aucsgj,ygigg]
crossing=[ygigg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END