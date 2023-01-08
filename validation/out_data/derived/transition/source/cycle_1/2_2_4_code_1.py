from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rail = Factor("rail", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
hes = Factor("hes", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
kpngck = Factor("kpngck", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
def kywa(rail, hes, kpngck):
    return rail[0] != hes[-1] or rail[-1] != kpngck[0]
def biofxd(rail, hes, kpngck):
    return not kywa(rail, hes, kpngck)
pghbkq = Factor("nbftir", [DerivedLevel("skb", Transition(kywa, [rail, hes, kpngck])), DerivedLevel("afo", Transition(biofxd, [rail, hes, kpngck]))])
### EXPERIMENT
design=[rail,hes,kpngck,pghbkq]
crossing=[pghbkq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END