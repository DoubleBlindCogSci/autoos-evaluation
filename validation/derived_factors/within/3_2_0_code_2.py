from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
amwmy = Factor("amwmy", ["zlqrrr","mvsxl","yvftzn","iad","pkzdr","wgsypn","tkilkx"])
grny = Factor("grny", ["irzx","ssukt","fpcve","gqzabc","xqp","vyl","fla","nabs"])
def is_codal_halv(amwmy, grny):
    return amwmy == "tkilkx"
def is_codal_uoux(amwmy, grny):
    return amwmy != "tkilkx" and grny == "fla"
def is_codal_wjzz(amwmy, grny):
    return not (is_codal_halv(amwmy) or is_codal_uoux(amwmy, grny))
codal = Factor("codal", [DerivedLevel("halv", WithinTrial(is_codal_halv, [amwmy])), DerivedLevel("uoux", WithinTrial(is_codal_uoux, [amwmy, grny])), DerivedLevel("wjzz", WithinTrial(is_codal_wjzz, [amwmy, grny]))])

design=[amwmy,grny,codal]
crossing=[codal]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END