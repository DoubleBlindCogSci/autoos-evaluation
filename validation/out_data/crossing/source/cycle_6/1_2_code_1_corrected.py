from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fadcs = Factor("fadcs", ["tob", "asjqcz"])
hdasx = Factor("hdasx", ["uzndxk", "pbl"])
drq = Factor("drq", ["pzce", "wta"])

### EXPERIMENT
design=[fadcs,hdasx,drq]
crossing = [[fadcs,hdasx,drq],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END
