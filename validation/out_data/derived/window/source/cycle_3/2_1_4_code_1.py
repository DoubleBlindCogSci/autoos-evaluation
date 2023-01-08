from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hsva = Factor("hsva", ["ksmtfw","ldum","mfr","vxyb","rhjo","wghwmg"])
def jfgr(hsva):
    return hsva[0] != "wghwmg" or hsva[-1] != "ksmtfw"
def mdsr(hsva):
    return hsva[0] == "wghwmg" and hsva[-1] == "ksmtfw"
eonbo = DerivedLevel("okb", Window(jfgr, [hsva],2,1))
qzzj = DerivedLevel("atvuk", Window(mdsr, [hsva],2,1))
adihe = Factor("aizxw", [eonbo, qzzj])

### EXPERIMENT
design=[hsva,adihe]
crossing=[adihe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END