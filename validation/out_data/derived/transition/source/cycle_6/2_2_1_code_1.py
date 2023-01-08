from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kwj = Factor("kwj", ["fvkkc","ljrj","goim","ojynkw","ycziw","yhunwo","yxyld"])
cxz = Factor("cxz", ["fvkkc","ljrj","goim","ojynkw","ycziw","yhunwo","yxyld"])
fbyaf = Factor("fbyaf", ["fvkkc","ljrj","goim","ojynkw","ycziw","yhunwo","yxyld"])
def gfybtk(kwj, cxz, fbyaf):
    return kwj[0] != cxz[-1]
def dru(kwj, cxz, fbyaf):
    return kwj[0] == cxz[-1]
kxmyeo = Factor("qmsogb", [DerivedLevel("sjjt", Transition(gfybtk, [kwj, cxz, fbyaf])), DerivedLevel("tcsfdi", Transition(dru, [kwj, cxz, fbyaf]))])
### EXPERIMENT
design=[kwj,cxz,fbyaf,kxmyeo]
crossing=[kxmyeo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END