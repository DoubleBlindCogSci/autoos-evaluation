from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rialx = Factor("rialx", ["eroaje", "pobcf"])
zikm = Factor("zikm", ["tabv", "ysa"])
eet = Factor("eet", ["pvb", "mem"])

### EXPERIMENT
design=[rialx,zikm,eet]
crossing=[[rialx],[zikm,eet],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3"))
### END