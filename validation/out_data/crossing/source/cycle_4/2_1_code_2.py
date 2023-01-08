from sweetpea import *
import os
_dir=os.path.dirname(__file__)
dmkl = Factor("dmkl", ["vho", "zkj"])
ansje = Factor("ansje", ["bogw", "vcub"])
zffjgs = Factor("zffjgs", ["yckc", "ayr"])
ashmc = Factor("ashmc", ["wfdi", "pmvu"])
hiw = Factor("hiw", ["fspw", "aop"])
constraints = []
crossing = [[dmkl], [ansje, zffjgs, ashmc, hiw]]


design=[dmkl,ansje,zffjgs,ashmc,hiw]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END