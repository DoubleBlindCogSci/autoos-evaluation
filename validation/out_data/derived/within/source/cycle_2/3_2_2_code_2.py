from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qmcxwy= Factor("qmcxwy", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
jnubcb= Factor("jnubcb", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
yntx= Factor("yntx", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
def is_iwnx_lcas(qmcxwy, yntx, jnubcb):
    return qmcxwy == yntx
def is_iwnx_xxk(qmcxwy, yntx, jnubcb):
    return qmcxwy != yntx and qmcxwy == jnubcb
def is_iwnx_twq(qmcxwy, yntx, jnubcb):
    return qmcxwy != yntx and qmcxwy != jnubcb
iwnx= Factor("iwnx", [DerivedLevel("lcas", WithinTrial(is_iwnx_lcas, [qmcxwy, yntx, jnubcb])), DerivedLevel("xxk", WithinTrial(is_iwnx_xxk, [qmcxwy, yntx, jnubcb])), DerivedLevel("twq", WithinTrial(is_iwnx_twq, [qmcxwy, yntx, jnubcb]))])

design=[qmcxwy,jnubcb,yntx, iwnx]
crossing=[iwnx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
