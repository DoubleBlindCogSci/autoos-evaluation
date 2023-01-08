from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wnjfo = Factor("wnjfo", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
ydczl = Factor("ydczl", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
ezw = Factor("ezw", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
def aun(wnjfo, ydczl, ezw):
     return ydczl[-1] == wnjfo[0] and wnjfo[-1] != ezw[0]
def ulh(wnjfo, ydczl, ezw):
     return ydczl[-1] != wnjfo[0] and wnjfo[-1] == ezw[0]
def gqi(wnjfo, ydczl, ezw):
     return (not wnjfo[0] == ydczl[-1]) and (wnjfo[-1] != ezw[0])
vahh = Factor("gaovt", [DerivedLevel("wpyds", Transition(aun, [wnjfo, ydczl, ezw])), DerivedLevel("hjm", Transition(ulh, [wnjfo, ydczl, ezw])),DerivedLevel("iiyv", Transition(gqi, [wnjfo, ydczl, ezw]))])
### EXPERIMENT
design=[wnjfo,ydczl,ezw,vahh]
crossing=[vahh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END