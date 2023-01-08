from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_9AnDrA=Factor('YgtsvYET',["LX6wnk","ylO","6SyYjHVgKmk","BC~UhxQyIEw"])
aCl_z8=Factor("etcI",[Level('lxGOK',4),'opEjNb zCdxUu(',"pVcP)ui{l$w",'5[Q7PR'])

### EXPERIMENT
design=[_9AnDrA,aCl_z8]
crossing=[_9AnDrA,aCl_z8]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_0"))
### END