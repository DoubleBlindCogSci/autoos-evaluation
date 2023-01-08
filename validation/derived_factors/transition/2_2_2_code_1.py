from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xkth = Factor("xkth", ["uov","iez","izvy","zdmgra","wigw","ibjto","dauvi"])
phtyd = Factor("phtyd", ["ooqwku","rfrmn","isvgs","qzt","gqx","aaaoi"])
def xxvmlj(xkth, phtyd):
    return xkth[0] != "ibjto" and phtyd[-1] != "ooqwku"
def yjhyqf(xkth,phtyd):
    return xkth[0] == "ibjto" or not (phtyd[-1] != "ooqwku")
csydmt = Factor("hpbajg", [DerivedLevel("bknevy", Transition(xxvmlj, [xkth, phtyd])), DerivedLevel("agynv", Transition(yjhyqf, [xkth, phtyd]))])
### EXPERIMENT
design=[xkth,phtyd,csydmt]
crossing=[csydmt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END