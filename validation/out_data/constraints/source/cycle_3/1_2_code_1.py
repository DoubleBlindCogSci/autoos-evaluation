from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uxhhmg = Factor("uxhhmg", ["mhwyv","eoca", "wyy"])
xyx = Factor("xyx", ["ncwxx","xwfk","xdaeck", "oel"])
tyun = Factor("tyun", ["nppxje", "ewquqs"])

### EXPERIMENT
constraints=[AtMostKInARow(2,(uxhhmg,"wyy"))]
design=[uxhhmg,xyx,tyun]
crossing=[xyx,tyun]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END