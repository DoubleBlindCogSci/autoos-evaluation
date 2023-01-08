from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tprnu= Factor("tprnu", ["aot","aqp","eldx","bsxt","lklq","xkjq","hnt"])
def is_shrv_ngmg(tprnu):
    return tprnu[0] == tprnu[-2]
def is_shrv_jvk(tprnu):
    return tprnu[0] == tprnu[-1]
def is_shrv_jrldp(tprnu):
    return not (is_shrv_ngmg(tprnu) or is_shrv_jvk(tprnu))
shrv= Factor("shrv", [DerivedLevel("ngmg", Window(is_shrv_ngmg, [tprnu], 2, 1)), DerivedLevel("jvk", Window(is_shrv_jvk, [tprnu], 2, 1)), DerivedLevel("jrldp", Window(is_shrv_jrldp, [tprnu], 2, 1))])

design=[tprnu,shrv]
crossing=[shrv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
