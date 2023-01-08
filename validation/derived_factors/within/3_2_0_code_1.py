from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
amwmy = Factor("amwmy", ["zlqrrr","mvsxl","yvftzn","iad","pkzdr","wgsypn","tkilkx"])
grny = Factor("grny", ["irzx","ssukt","fpcve","gqzabc","xqp","vyl","fla","nabs"])
def rugexs(amwmy, grny):
     return amwmy == "tkilkx"
def swo(amwmy, grny):
     return "tkilkx" != amwmy and  grny == "fla"
def xvgyju(amwmy, grny):
     return (not rugexs(amwmy, grny)) and (not swo(amwmy, grny))
kkw = DerivedLevel("halv", WithinTrial(rugexs, [amwmy, grny]))
tilxhn = DerivedLevel("uoux", WithinTrial(swo, [amwmy, grny]))
sahxm = DerivedLevel("wjzz", WithinTrial(xvgyju, [amwmy, grny]))
kyskvb = Factor("codal", [kkw, tilxhn, sahxm])

### EXPERIMENT
design=[amwmy,grny,kyskvb]
crossing=[kyskvb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END