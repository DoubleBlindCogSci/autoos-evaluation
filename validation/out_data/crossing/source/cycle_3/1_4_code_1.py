from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xrmdtq = Factor("xrmdtq", ["qsdwuv", "rtel"])
lejj = Factor("lejj", ["czoo", "dnmdzs"])
hqht = Factor("hqht", ["elxnc", "mxzpkv"])

### EXPERIMENT
design=[xrmdtq,lejj,hqht]
crossing=[[xrmdtq,lejj,hqht],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_4"))
### END