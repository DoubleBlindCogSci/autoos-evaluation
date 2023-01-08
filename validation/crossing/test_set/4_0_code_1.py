from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rvyx = Factor("rvyx", ["ijgnbn", "pifw"])
ggy = Factor("ggy", ["gkslm", "swiiva"])
qayri = Factor("qayri", ["fgku", "dldh"])
ybqveb = Factor("ybqveb", ["vmth", "fraq"])

### EXPERIMENT
design=[rvyx,ggy,qayri,ybqveb]
crossing=[[rvyx,ggy,qayri,ybqveb]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0"))
### END