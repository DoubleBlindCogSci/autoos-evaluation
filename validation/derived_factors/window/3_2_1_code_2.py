from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hmi = Factor("hmi", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
pkyoho = Factor("pkyoho", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
efzpc = Factor("efzpc", ["nlve","ikl","xdaxd","yyrp","ivju","wmvjxq","movp","hta"])
def is_abobi_zebmpm(hmi, pkyoho, efzpc):
    return pkyoho[0] == hmi[-1] and hmi[0] != efzpc[-1]
def is_abobi_ury(hmi, pkyoho, efzpc):
    return pkyoho[0] != hmi[-1] and efzpc[-1] == hmi[0]
def is_abobi_ljy(hmi, pkyoho, efzpc):
    return not (is_abobi_zebmpm(hmi, pkyoho, efzpc) or is_abobi_ury(hmi, pkyoho, efzpc))
abobi = Factor("abobi", [DerivedLevel("zebmpm", Window(is_abobi_zebmpm, [hmi, pkyoho, efzpc], 2, 1)), DerivedLevel("ury", Window(is_abobi_ury, [hmi, pkyoho, efzpc], 2, 1)), DerivedLevel("ljy", Window(is_abobi_ljy, [hmi, pkyoho, efzpc], 2, 1))])

design=[hmi,pkyoho,efzpc,abobi]
crossing=[abobi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END