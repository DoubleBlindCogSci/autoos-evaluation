from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fqrce = Factor("fqrce", ["juzx", "ujne"])
sncswb = Factor("sncswb", ["flsz", "lliwb"])
ugqvv = Factor("ugqvv", ["guxdq", "tottb"])
cqhdiu = Factor("cqhdiu", ["syqow", "xfyict"])
xrmn = Factor("xrmn", ["otpmc", "pepb"])
iakch = Factor("iakch", ["igoux", "wdufed"])
mytf = Factor("mytf", ["gkyk", "cknkkw"])

### EXPERIMENT
design=[fqrce,sncswb,ugqvv,cqhdiu,xrmn,iakch,mytf]
crossing=[[fqrce,sncswb,ugqvv,cqhdiu,xrmn,iakch,mytf]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1"))
### END