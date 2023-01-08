from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ltb = Factor("ltb", ["ydna","rsx","dlpyg","zjrod","dfy","vdlgyc"])
def is_hva_gziav(ltb):
    return ltb[-1] == "dfy" and ltb[-2] != "dfy"
def is_hva_zldu(ltb):
    return ltb[-1] != "dfy" and ltb[-2] == "ydna"
def is_hva_kycwij(ltb):
    return not (is_hva_gziav(ltb) or is_hva_zldu(ltb))
hva = Factor("hva", [DerivedLevel("gziav", Window(is_hva_gziav, [ltb], 3, 1)), DerivedLevel("zldu", Window(is_hva_zldu, [ltb], 3, 1)), DerivedLevel("kycwij", Window(is_hva_kycwij, [ltb], 3, 1))])

design=[ltb,hva]
crossing=[hva]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END