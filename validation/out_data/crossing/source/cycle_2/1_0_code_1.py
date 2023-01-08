from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eatw = Factor("eatw", ["yuryh", "ugaxqo"])
ywjbjy = Factor("ywjbjy", ["qoy", "rogcnz"])
gjvq = Factor("gjvq", ["ludm", "hccoca"])

### EXPERIMENT
design=[eatw,ywjbjy,gjvq]
crossing=[[eatw,ywjbjy,gjvq],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_0"))
### END