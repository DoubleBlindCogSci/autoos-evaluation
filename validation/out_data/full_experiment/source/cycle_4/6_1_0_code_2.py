from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
nnoqy = Factor("nnoqy", ["xmqn", "tkhwvj"])
bac = Factor("bac", ["isxjfn", "gmpgkr"])
iopjv = Factor("iopjv", ["xmqn", "tkhwvj"])
lnnq = Factor("lnnq", ["isxjfn", "gmpgkr"])
svbto = Factor("svbto", ["wlmdyb", "adjimh"])
mtro = Factor("mtro", ["hgcxa", "frzn"])
def is_ggzo_kzir(bac, lnnq):
    return bac == lnnq
def is_ggzo_wddk(bac, lnnq):
    return not is_ggzo_kzir(bac, lnnq)
ggzo = Factor("ggzo", [DerivedLevel("kzir", WithinTrial(is_ggzo_kzir, [bac, lnnq])), DerivedLevel("wddk", WithinTrial(is_ggzo_wddk, [bac, lnnq]))])
constraints = []
crossing = [iopjv, svbto]

design=[nnoqy,bac,iopjv,lnnq,svbto,mtro,ggzo]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_0"))
