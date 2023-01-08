from sweetpea import *
import os
_dir=os.path.dirname(__file__)
rialx = Factor("rialx", ["eroaje", "pobcf"])
zikm = Factor("zikm", ["tabv", "ysa"])
eet = Factor("eet", ["pvb", "mem"])
constraints = []
crossing = [[rialx, zikm], [zikm], [eet]]


design=[rialx,zikm,eet]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3"))

### END