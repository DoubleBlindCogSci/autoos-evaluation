from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
lovf = Factor("lovf", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
prpbhg = Factor("prpbhg", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
rnik = Factor("rnik", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
def zyb(lovf, rnik, prpbhg):
    return lovf == rnik
def ytaig(lovf, rnik, prpbhg):
    return lovf != rnik
jibma = DerivedLevel("ldor", WithinTrial(zyb, [lovf, prpbhg, rnik]))
womtv = DerivedLevel("rue", WithinTrial(ytaig, [lovf, prpbhg, rnik]))
exrux = Factor("fuvcg", [jibma, womtv])

### EXPERIMENT
design=[lovf,prpbhg,rnik,exrux]
crossing=[exrux]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END