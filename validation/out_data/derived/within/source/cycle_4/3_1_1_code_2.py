from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pcg = Factor("pcg", ["dqrn","thzjgv","ptwa","anf","dglo","qsd","nto","eczl"])
def is_fopjp_ibta(pcg):
    return pcg == "dqrn"
def is_fopjp_bwkw(pcg):
    return pcg == "eczl"
def is_fopjp_lsi(pcg):
    return not (is_fopjp_ibta(pcg) or is_fopjp_bwkw(pcg))
fopjp= Factor("fopjp", [DerivedLevel("ibta", WithinTrial(is_fopjp_ibta, [pcg])), DerivedLevel("bwkw", WithinTrial(is_fopjp_bwkw, [pcg])), DerivedLevel("lsi", WithinTrial(is_fopjp_lsi, [pcg]))])

design=[pcg,fopjp]
crossing=[fopjp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END