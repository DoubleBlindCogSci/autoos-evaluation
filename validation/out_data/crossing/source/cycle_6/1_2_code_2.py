from sweetpea import *
import os
_dir=os.path.dirname(__file__)
fadcs = Factor("fadcs", ["tob", "asjqcz"])
hdasx = Factor("hdasx", ["uzndxk", "pbl"])
drq = Factor("drq", ["pzce", "wta"])
constraints = []
crossing = [fadcs, hdasx, drq]


design=[fadcs,hdasx,drq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_2"))

### END