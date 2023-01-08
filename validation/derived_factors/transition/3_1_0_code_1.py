from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ahpu = Factor("ahpu", ["uha","kfgvi","vfifq","vwqq","yza","kbq"])
def ycfhe(ahpu):
     return ahpu[0] == "kbq" and ahpu[-1] != "vwqq"
def apk(ahpu):
     return (not "kbq" != ahpu[0]) and  "vwqq" == ahpu[-1]
def vrqhcn(ahpu):
     return (not ahpu[0] == "kbq") and (not ahpu[-1] == "vwqq")
fuvaq = DerivedLevel("dhvhl", Transition(ycfhe, [ahpu]))
vwtofu = DerivedLevel("ysbhd", Transition(apk, [ahpu]))
uuhah = DerivedLevel("ryb", Transition(vrqhcn, [ahpu]))
naeix = Factor("xzsh", [fuvaq, vwtofu, uuhah])

### EXPERIMENT
design=[ahpu,naeix]
crossing=[naeix]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END