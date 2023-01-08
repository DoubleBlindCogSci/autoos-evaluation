from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qbzh = Factor("qbzh", ["ginswl","sxl","kxzb","xbq","dibh","lyz"])
def uaafhs(qbzh):
     return qbzh == "dibh"
def vln(qbzh):
     return "lyz" == qbzh
def oujcz(qbzh):
     return (not qbzh == "dibh") and (qbzh != "lyz")
nrpu = DerivedLevel("emqd", WithinTrial(uaafhs, [qbzh]))
bczyw = DerivedLevel("kmrzf", WithinTrial(vln, [qbzh]))
hmgtc = DerivedLevel("jxeygo", WithinTrial(oujcz, [qbzh]))
ztcpxy = Factor("boymv", [nrpu, bczyw, hmgtc])

### EXPERIMENT
design=[qbzh,ztcpxy]
crossing=[ztcpxy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END