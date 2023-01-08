from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cpaotp = Factor("cpaotp", ["hsipy","lzfk","ygh","johine","qxb","sgyyen"])
def wsfsf(cpaotp):
    return cpaotp[0] == "lzfk" or cpaotp[-1] != "johine"
def uma(cpaotp):
    return not (cpaotp[0] == "lzfk") and cpaotp[-1] == "johine"
pdyuy = DerivedLevel("hbk", Transition(wsfsf, [cpaotp]))
ljyv = DerivedLevel("bswz", Transition(uma, [cpaotp]))
dpj = Factor("qweqys", [pdyuy, ljyv])

### EXPERIMENT
design=[cpaotp,dpj]
crossing=[dpj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END