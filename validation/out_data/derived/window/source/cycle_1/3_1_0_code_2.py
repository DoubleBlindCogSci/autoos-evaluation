from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vxqndv= Factor("vxqndv", ["egnpd","aof","ybec","jcamd","gocgh","qcdyxn"])
def is_tyruji_kbpq(vxqndv):
    return vxqndv[0] == vxqndv[-2]
def is_tyruji_bmb(vxqndv):
    return vxqndv[0] == vxqndv[-1]
def is_tyruji_nfzkw(vxqndv):
    return not (is_tyruji_kbpq(vxqndv) or is_tyruji_bmb(vxqndv))
tyruji= Factor("tyruji", [DerivedLevel("kbpq", Window(is_tyruji_kbpq, [vxqndv], 3, 1)), DerivedLevel("bmb", Window(is_tyruji_bmb, [vxqndv], 3, 1)), DerivedLevel("nfzkw", Window(is_tyruji_nfzkw, [vxqndv], 3, 1))])

design=[vxqndv,tyruji]
crossing=[tyruji]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
