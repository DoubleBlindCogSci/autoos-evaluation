from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rxerxr = Factor("rxerxr", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
begh = Factor("begh", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
jwacc = Factor("jwacc", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
def uoks(rxerxr, begh, jwacc):
     return begh[-2] == rxerxr[0] and rxerxr[-2] != jwacc[0]
def cvq(rxerxr, begh, jwacc):
     return begh[-2] != rxerxr[0] and rxerxr[-2] == jwacc[0]
def pfmwt(rxerxr, begh, jwacc):
     return (not rxerxr[0] == begh[-2]) and (rxerxr[-2] != jwacc[0])
oidv = DerivedLevel("woyerc", Window(uoks, [rxerxr, begh, jwacc],3,1))
ljy = DerivedLevel("xpt", Window(cvq, [rxerxr, begh, jwacc],3,1))
uqvamn = DerivedLevel("vblwpg", Window(pfmwt, [rxerxr, begh, jwacc],3,1))
zss = Factor("dhaal", [oidv, ljy, uqvamn])

### EXPERIMENT
design=[rxerxr,begh,jwacc,zss]
crossing=[zss]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END