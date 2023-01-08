from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bpmr = Factor("bpmr", ["vdza", "zew"])
nyoy = Factor("nyoy", ["emszr", "ntatdb"])
dma = Factor("dma", ["vzx", "kmmaw"])
fdl = Factor("fdl", ["xhisah", "vqejbj"])

### EXPERIMENT
design=[bpmr,nyoy,dma,fdl]
crossing=[[bpmr,nyoy],[dma,fdl],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_0"))
### END