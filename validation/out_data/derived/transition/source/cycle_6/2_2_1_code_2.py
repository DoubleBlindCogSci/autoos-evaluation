from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kwj = Factor("kwj", ["fvkkc","ljrj","goim","ojynkw","ycziw","yhunwo","yxyld"])
cxz = Factor("cxz", ["fvkkc","ljrj","goim","ojynkw","ycziw","yhunwo","yxyld"])
fbyaf = Factor("fbyaf", ["fvkkc","ljrj","goim","ojynkw","ycziw","yhunwo","yxyld"])
def is_qmsogb_sjjt(kwj, cxz, fbyaf):
    return kwj[0] != cxz[-1]
def is_qmsogb_tcsfdi(kwj, cxz, fbyaf):
    return not is_qmsogb_sjjt(kwj, cxz, fbyaf)
qmsogb = Factor("qmsogb", [DerivedLevel("sjjt", Transition(is_qmsogb_sjjt, [kwj, cxz, fbyaf])), DerivedLevel("tcsfdi", Transition(is_qmsogb_tcsfdi, [kwj, cxz, fbyaf]))])

design=[kwj,cxz,fbyaf,qmsogb]
crossing=[qmsogb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END