from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
msghmm = Factor("msghmm", ["fhtqa","lxlpwh","mjcz","ruxh","dbi","adzdc","frtoj"])
def axhghd(msghmm):
     return "frtoj" == msghmm[-2] and not msghmm[0] == "frtoj"
def mbacc(msghmm):
     return msghmm[-2] != "frtoj" and  "ruxh" == msghmm[0]
def rrc(msghmm):
     return (not msghmm[-2] == "frtoj") and (msghmm[0] != "ruxh")
afdm = Factor("kfz", [DerivedLevel("gbpdob", Window(axhghd, [msghmm],3,1)), DerivedLevel("aei", Window(mbacc, [msghmm],3,1)),DerivedLevel("pve", Window(rrc, [msghmm],3,1))])
### EXPERIMENT
design=[msghmm,afdm]
crossing=[afdm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END