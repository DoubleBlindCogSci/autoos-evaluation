from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
kxk = Factor("kxk", ["nllpb", "nhg"])
oqba = Factor("oqba", ["bdalt", "xjsf"])
voo = Factor("voo", ["nllpb", "nhg"])
wtq = Factor("wtq", ["bdalt", "xjsf"])
isf = Factor("isf", ["lavu", "tqntet"])
def jeghv(voo, oqba):
    return voo == oqba
def tadi(voo, oqba):
    return not jeghv(voo, oqba)
vceeea = Factor("vceeea", [DerivedLevel("rpds", WithinTrial(jeghv, [voo, oqba])), DerivedLevel("rth", WithinTrial(tadi, [voo, oqba]))])
constraints = []
crossing = [kxk, voo]

design=[kxk,oqba,voo,wtq,isf,vceeea]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_1_0"))
