from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lovf = Factor("lovf", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
prpbhg = Factor("prpbhg", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
rnik = Factor("rnik", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
def is_fuvcg_ldor(lovf, rnik, prpbhg):
    return lovf == rnik
def is_fuvcg_rue(lovf, rnik, prpbhg):
    return not is_fuvcg_ldor(lovf, rnik, prpbhg)
fuvcg = Factor("fuvcg", [DerivedLevel("ldor", WithinTrial(is_fuvcg_ldor, [lovf, rnik, prpbhg])), DerivedLevel("rue", WithinTrial(is_fuvcg_rue, [lovf, rnik, prpbhg]))])

design=[lovf,prpbhg,rnik,fuvcg]
crossing=[fuvcg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END