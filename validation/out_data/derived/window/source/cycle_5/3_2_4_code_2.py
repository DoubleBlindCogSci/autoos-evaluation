from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rxerxr = Factor("rxerxr", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
begh = Factor("begh", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
jwacc = Factor("jwacc", ["wyzbhe","jzfjyv","dlzmg","rxo","trgiex","hqtu"])
def is_dhaal_woyerc(rxerxr, begh, jwacc):
    return begh[-2] == rxerxr[0] and rxerxr[-2] != jwacc[0]
def is_dhaal_xpt(rxerxr, begh, jwacc):
    return begh[-2] != rxerxr[0] and rxerxr[-2] == jwacc[0]
def is_dhaal_vblwpg(rxerxr, begh, jwacc):
    return begh[-2] != rxerxr[0] and rxerxr[-2] != jwacc[0]
dhaal = Factor("dhaal", [DerivedLevel("woyerc", Window(is_dhaal_woyerc, [rxerxr, begh, jwacc], 3, 1)), DerivedLevel("xpt", Window(is_dhaal_xpt, [rxerxr, begh, jwacc], 3, 1)), DerivedLevel("vblwpg", Window(is_dhaal_vblwpg, [rxerxr, begh, jwacc], 3, 1))])

design=[rxerxr,begh,jwacc,dhaal]
crossing=[dhaal]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END