from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
utnvl = Factor("utnvl", ["bfs","noyu","qgq","fxp","jskquj"])
def is_jwikgn_lrhnd(utnvl):
    return utnvl == "bfs"
def is_jwikgn_rcpw(utnvl):
    return not is_jwikgn_lrhnd(utnvl)
jwikgn = Factor("jwikgn", [DerivedLevel("lrhnd", WithinTrial(is_jwikgn_lrhnd, [utnvl])), DerivedLevel("rcpw", WithinTrial(is_jwikgn_rcpw, [utnvl]))])

design=[utnvl,jwikgn]
crossing=[jwikgn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END