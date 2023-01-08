from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zrjr = Factor("zrjr", ["aoyis","hmmcrq", "jfyiwu"])
vjaiwl = Factor("vjaiwl", ["giotq","bwj", "fvt"])
midsd = Factor("midsd", ["sgmu", "xnvn"])

### EXPERIMENT
constraints=[AtMostKInARow(2,(zrjr,"jfyiwu"))]
design=[zrjr,vjaiwl,midsd]
crossing=[vjaiwl,midsd]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_1"))
### END