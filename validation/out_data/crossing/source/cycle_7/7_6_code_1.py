from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fnxt = Factor("fnxt", ["cykoid", "oepib"])
tnqsv = Factor("tnqsv", ["xihu", "dnom"])
vuun = Factor("vuun", ["dkv", "wxkdt"])
atn = Factor("atn", ["ykxen", "tsk"])
wxbwsf = Factor("wxbwsf", ["xah", "bxpko"])
rbwew = Factor("rbwew", ["wky", "zqq"])
etb = Factor("etb", ["cceg", "jfl"])

### EXPERIMENT
design=[fnxt,tnqsv,vuun,atn,wxbwsf,rbwew,etb]
crossing=[[fnxt,tnqsv,vuun,atn,wxbwsf,rbwew,etb]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_6"))
### END