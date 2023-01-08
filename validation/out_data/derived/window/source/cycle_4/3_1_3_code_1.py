from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eapq = Factor("eapq", ["vhnpdu","pbatp","lgksu","adm","lzk","xaxtof","hrtrsx"])
def bgsj(eapq):
     return "adm" == eapq[-2] and not eapq[-1] == "adm"
def qljtls(eapq):
     return not "adm" == eapq[-2] and  eapq[-1] == "hrtrsx"
def vjxrwh(eapq):
     return (not bgsj(eapq)) and (not eapq[-1] == "hrtrsx")
mxybt = DerivedLevel("bidy", Window(bgsj, [eapq],3,1))
stbdx = DerivedLevel("qzjjv", Window(qljtls, [eapq],3,1))
kobp = DerivedLevel("wpjoz", Window(vjxrwh, [eapq],3,1))
lxinl = Factor("xdgdqc", [mxybt, stbdx, kobp])

### EXPERIMENT
design=[eapq,lxinl]
crossing=[lxinl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END