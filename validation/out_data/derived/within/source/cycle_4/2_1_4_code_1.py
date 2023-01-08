from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
utnvl = Factor("utnvl", ["bfs","noyu","qgq","fxp","jskquj"])
def cjn(utnvl):
    return utnvl == "bfs"
def jfsul(utnvl):
    return not (utnvl == "bfs")
ieuhlb = Factor("jwikgn", [DerivedLevel("lrhnd", WithinTrial(cjn, [utnvl])), DerivedLevel("rcpw", WithinTrial(jfsul, [utnvl]))])
### EXPERIMENT
design=[utnvl,ieuhlb]
crossing=[ieuhlb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END