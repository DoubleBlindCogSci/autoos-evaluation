from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hxtk = Factor("hxtk", ["rnl","umdg","xoc","bdfo","jood","iqjrov"])
def is_jofvzx_xzyabw(hxtk):
    return hxtk[0] == "iqjrov" and hxtk[-1] != "jood"
def is_jofvzx_fqpfw(hxtk):
    return hxtk[0] != "iqjrov" and hxtk[-1] == "jood"
def is_jofvzx_cacgyf(hxtk):
    return not (is_jofvzx_xzyabw(hxtk) or is_jofvzx_fqpfw(hxtk))
jofvzx = Factor("jofvzx", [DerivedLevel("xzyabw", Transition(is_jofvzx_xzyabw, [hxtk])), DerivedLevel("fqpfw", Transition(is_jofvzx_fqpfw, [hxtk])), DerivedLevel("cacgyf", Transition(is_jofvzx_cacgyf, [hxtk]))])

design=[hxtk,jofvzx]
crossing=[jofvzx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END