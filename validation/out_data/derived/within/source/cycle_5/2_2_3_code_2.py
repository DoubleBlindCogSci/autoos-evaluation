from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mapj = Factor("mapj", ["kgou","fqf","ezoep","ygf","vdy","wjm"])
nvqy = Factor("nvqy", ["kgou","fqf","ezoep","ygf","vdy","wjm"])
bgc = Factor("bgc", ["kgou","fqf","ezoep","ygf","vdy","wjm"])
def is_pcc_xkx(mapj, nvqy, bgc):
    return mapj != nvqy
def is_pcc_ptsfnc(mapj, nvqy, bgc):
    return not is_pcc_xkx(mapj, nvqy, bgc)
pcc = Factor("pcc", [DerivedLevel("xkx", WithinTrial(is_pcc_xkx, [mapj, nvqy, bgc])), DerivedLevel("ptsfnc", WithinTrial(is_pcc_ptsfnc, [mapj, nvqy, bgc]))])

design=[mapj,nvqy,bgc,pcc]
crossing=[pcc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END