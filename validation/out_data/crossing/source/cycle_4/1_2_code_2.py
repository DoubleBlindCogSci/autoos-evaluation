from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ybfh = Factor("ybfh", ["hei", "mtftut"])
zustfn = Factor("zustfn", ["pidczl", "ynuosc"])
clr = Factor("clr", ["rvf", "hfqpwa"])
constraints = []
crossing = [ybfh, zustfn, clr]


design=[ybfh,zustfn,clr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_2"))

### END