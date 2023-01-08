from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vmiuar = Factor("vmiuar", ["scy", "nwxgr"])
sxlo = Factor("sxlo", ["lpdaqk","jczns", "oeq"])

### EXPERIMENT
constraints=[ExactlyK(3,(vmiuar,"nwxgr"))]
design=[vmiuar,sxlo]
crossing=[sxlo]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END