from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hmi = Factor("hmi", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
pkyoho = Factor("pkyoho", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
efzpc = Factor("efzpc", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
def fjpq(hmi, pkyoho, efzpc):
     return pkyoho[0] == hmi[-1] and hmi[0] != efzpc[-1]
def bfx(hmi, pkyoho, efzpc):
     return pkyoho[0] != hmi[-1] and efzpc[-1] == hmi[0]
def cqsitt(hmi, pkyoho, efzpc):
     return (not hmi[-1] == pkyoho[0]) and (not bfx(hmi, pkyoho, efzpc))
nclfg = Factor("abobi", [DerivedLevel("zebmpm", Window(fjpq, [hmi, pkyoho, efzpc],2,1)), DerivedLevel("ury", Window(bfx, [hmi, pkyoho, efzpc],2,1)),DerivedLevel("ljy", Window(cqsitt, [hmi, pkyoho, efzpc],2,1))])
### EXPERIMENT
design=[hmi,pkyoho,efzpc,nclfg]
crossing=[nclfg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END