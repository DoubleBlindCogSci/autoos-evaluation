from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dmkl = Factor("dmkl", ["vho", "zkj"])
ansje = Factor("ansje", ["bogw", "vcub"])
zffjgs = Factor("zffjgs", ["yckc", "ayr"])
ashmc = Factor("ashmc", ["wfdi", "pmvu"])
hiw = Factor("hiw", ["fspw", "aop"])

### EXPERIMENT
design=[dmkl,ansje,zffjgs,ashmc,hiw]
crossing=[[dmkl],[ansje,zffjgs,ashmc,hiw],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1"))
### END