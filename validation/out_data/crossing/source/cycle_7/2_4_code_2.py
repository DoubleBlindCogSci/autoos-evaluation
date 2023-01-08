from sweetpea import *
import os
_dir=os.path.dirname(__file__)
fovgn = Factor("fovgn", ["zudbr", "ibomx"])
dxt = Factor("dxt", ["untgp", "kuvqd"])
constraints = []
crossing = [fovgn, dxt]


design=[fovgn,dxt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4"))

### END