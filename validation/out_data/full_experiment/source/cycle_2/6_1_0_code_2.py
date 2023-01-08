from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
aiq = Factor("aiq", ["dbjumx", "woafy"])
jefa = Factor("jefa", ["qkd", "zighty"])
leophp = Factor("leophp", ["dbjumx", "woafy"])
vwqn = Factor("vwqn", ["qkd", "zighty"])
zovw = Factor("zovw", ["qtjexx", "swxghh"])
qexm = Factor("qexm", ["ggxeg", "lbxnp"])
def is_pye_bqekyw(jefa, leophp):
    return jefa == leophp
def is_pye_ygfjnn(jefa, leophp):
    return not is_pye_bqekyw(jefa, leophp)
pye= Factor("pye", [DerivedLevel("bqekyw", WithinTrial(is_pye_bqekyw, [jefa, leophp])), DerivedLevel("ygfjnn", WithinTrial(is_pye_ygfjnn, [jefa, leophp]))])
constraints = []
crossing = [vwqn, aiq]

design=[aiq,jefa,leophp,vwqn,zovw,qexm,pye]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_0"))
