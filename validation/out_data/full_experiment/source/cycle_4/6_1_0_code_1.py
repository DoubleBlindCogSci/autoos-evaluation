from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
nnoqy = Factor("nnoqy", ["xmqn", "tkhwvj"])
bac = Factor("bac", ["isxjfn", "gmpgkr"])
iopjv = Factor("iopjv", ["xmqn", "tkhwvj"])
lnnq = Factor("lnnq", ["isxjfn", "gmpgkr"])
svbto = Factor("svbto", ["wlmdyb", "adjimh"])
mtro = Factor("mtro", ["hgcxa", "frzn"])
def nhlkq (bac, lnnq):
    return bac == lnnq
def wiqa (bac, lnnq):
    return not nhlkq(bac, lnnq)
ggzo = Factor("ggzo", [DerivedLevel("kzir", WithinTrial(nhlkq, [bac, lnnq])), DerivedLevel("wddk", WithinTrial(wiqa, [bac, lnnq]))])
design=[ggzo,nnoqy,bac,iopjv,lnnq,svbto,mtro]
constraints=[]
crossing=[iopjv,svbto]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_0"))
