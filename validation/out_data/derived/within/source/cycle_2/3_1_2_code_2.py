from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pcqefj= Factor("pcqefj", ["cdjnz","lgco","rduahx","fdu","fmy","mcsovj","cmb","cmj"])
def is_dgm_btv(pcqefj):
    return pcqefj == "lgco"
def is_dgm_hvi(pcqefj):
    return pcqefj == "fmy"
def is_dgm_hyajkt(pcqefj):
    return not (is_dgm_btv(pcqefj) or is_dgm_hvi(pcqefj))
dgm= Factor("dgm", [DerivedLevel("btv", WithinTrial(is_dgm_btv, [pcqefj])), DerivedLevel("hvi", WithinTrial(is_dgm_hvi, [pcqefj])), DerivedLevel("hyajkt", WithinTrial(is_dgm_hyajkt, [pcqefj]))])

design=[pcqefj, dgm]
crossing=[dgm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
