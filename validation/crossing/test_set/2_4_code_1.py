from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fovgn = Factor("fovgn", ["zudbr", "ibomx"])
dxt = Factor("dxt", ["untgp", "kuvqd"])

### EXPERIMENT
design=[fovgn,dxt]
crossing=[[fovgn,dxt]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_4"))
### END