from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
aiq = Factor("aiq", ["dbjumx", "woafy"])
jefa = Factor("jefa", ["qkd", "zighty"])
leophp = Factor("leophp", ["dbjumx", "woafy"])
vwqn = Factor("vwqn", ["qkd", "zighty"])
zovw = Factor("zovw", ["qtjexx", "swxghh"])
qexm = Factor("qexm", ["ggxeg", "lbxnp"])
def ypkh (jefa, leophp):
    return jefa == leophp
def znu (jefa, leophp):
    return not ypkh(jefa, leophp)
pye = Factor("pye", [DerivedLevel("bqekyw", WithinTrial(ypkh, [jefa, leophp])), DerivedLevel("ygfjnn", WithinTrial(znu, [jefa, leophp]))])
design=[pye,aiq,jefa,leophp,vwqn,zovw,qexm]
constraints=[]
crossing=[vwqn,aiq]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_0"))
