from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mapj = Factor("mapj", ["kgou","fqf","ezoep","ygf","vdy","wjm"])
nvqy = Factor("nvqy", ["kgou","fqf","ezoep","ygf","vdy","wjm"])
bgc = Factor("bgc", ["kgou","fqf","ezoep","ygf","vdy","wjm"])
def ajjrhp(mapj, nvqy, bgc):
    return mapj != nvqy
def vpwhy(mapj, nvqy, bgc):
    return mapj == nvqy
onccpi = DerivedLevel("xkx", WithinTrial(ajjrhp, [mapj, nvqy, bgc]))
gwf = DerivedLevel("ptsfnc", WithinTrial(vpwhy, [mapj, nvqy, bgc]))
pytmg = Factor("pcc", [onccpi, gwf])

### EXPERIMENT
design=[mapj,nvqy,bgc,pytmg]
crossing=[pytmg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END