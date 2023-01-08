from sweetpea import *
import os
_dir=os.path.dirname(__file__)
bpmr = Factor("bpmr", ["vdza", "zew"])
nyoy = Factor("nyoy", ["emszr", "ntatdb"])
dma = Factor("dma", ["vzx", "kmmaw"])
fdl = Factor("fdl", ["xhisah", "vqejbj"])
constraints = []
crossing = [[bpmr, nyoy], [dma, fdl]]


design=[bpmr,nyoy,dma,fdl]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END