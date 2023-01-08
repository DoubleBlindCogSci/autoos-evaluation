from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xkth = Factor("xkth", ["uov","iez","izvy","zdmgra","wigw","ibjto","dauvi"])
phtyd = Factor("phtyd", ["ooqwku","rfrmn","isvgs","qzt","gqx","aaaoi"])
def is_hpbajg_bknevy(xkth, phtyd):
    return xkth[0] != "ibjto" and phtyd[-1] != "ooqwku"
def is_hpbajg_agynv(xkth, phtyd):
    return not is_hpbajg_bknevy(xkth, phtyd)
hpbajg = Factor("hpbajg", [DerivedLevel("bknevy", Transition(is_hpbajg_bknevy, [xkth, phtyd])), DerivedLevel("agynv", Transition(is_hpbajg_agynv, [xkth, phtyd]))])

design=[xkth,phtyd,hpbajg]
crossing=[hpbajg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END