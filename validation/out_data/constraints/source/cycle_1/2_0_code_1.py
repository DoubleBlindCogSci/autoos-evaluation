from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oxw = Factor("oxw", ["gim","hdxee","lyfjip", "xncbds"])
aaspho = Factor("aaspho", ["pawt","hbr", "btkh"])
wxndnx = Factor("wxndnx", ["ktg", "oxvwfe"])
xgcgk = Factor("xgcgk", ["gixwlb", "zxx"])

### EXPERIMENT
constraints=[ExactlyK(3,(oxw,"xncbds")),MinimumTrials(40)]
design=[oxw,aaspho,wxndnx,xgcgk]
crossing=[wxndnx,xgcgk]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_0"))
### END