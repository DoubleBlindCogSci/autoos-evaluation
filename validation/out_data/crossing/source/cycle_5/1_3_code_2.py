from sweetpea import *
import os
_dir=os.path.dirname(__file__)
prfc = Factor("prfc", ["tixac", "bjv"])
cxlsq = Factor("cxlsq", ["tpsqp", "pskbo"])
constraints = []
crossing = [prfc, cxlsq]


design=[prfc,cxlsq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_3"))

### END