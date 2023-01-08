from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ybfh = Factor("ybfh", ["hei", "mtftut"])
zustfn = Factor("zustfn", ["pidczl", "ynuosc"])
clr = Factor("clr", ["rvf", "hfqpwa"])

### EXPERIMENT
design=[ybfh,zustfn,clr]
crossing=[[ybfh,zustfn,clr],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END