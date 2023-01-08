from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qqctd = Factor("qqctd", ["dnhr","vwlutu","erpx","aybjto","cru","vyz","nddsz"])
def is_ecx_ugeme(qqctd):
    return qqctd[-2] == "aybjto" and qqctd[0] == "vwlutu"
def is_ecx_algua(qqctd):
    return not is_ecx_ugeme(qqctd)
ecx = Factor("ecx", [DerivedLevel("ugeme", Window(is_ecx_ugeme, [qqctd], 3, 1)), DerivedLevel("algua", Window(is_ecx_algua, [qqctd], 3, 1))])

design=[qqctd,ecx]
crossing=[ecx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END