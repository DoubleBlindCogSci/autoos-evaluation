from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rail= Factor("rail", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
hes= Factor("hes", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
kpngck= Factor("kpngck", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
def is_nbftir_skb(rail, hes, kpngck):
    return rail[0] != hes[-1] or rail[0] != kpngck[1]
def is_nbftir_afo(rail, hes, kpngck):
    return not is_nbftir_skb(rail, hes, kpngck)
nbftir= Factor("nbftir", [DerivedLevel("skb", Transition(is_nbftir_skb, [rail, hes, kpngck])), DerivedLevel("afo", Transition(is_nbftir_afo, [rail, hes, kpngck]))])

design=[rail,hes,kpngck,nbftir]
crossing=[nbftir]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
