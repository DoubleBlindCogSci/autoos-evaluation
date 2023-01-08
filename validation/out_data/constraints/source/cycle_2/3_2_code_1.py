from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gzepk = Factor("gzepk", ["vzzff","kwxera", "mzr"])
xlfcmx = Factor("xlfcmx", ["dsxl","mmoylz", "yelac"])
ameud = Factor("ameud", ["mmz","bxt", "ppafk"])
wnh = Factor("wnh", ["gwrsdm","cfi","wrt", "gnbte"])
rxvqmd = Factor("rxvqmd", ["dowdj","svfof","nzbum", "rtcyv"])
mzsfvk = Factor("mzsfvk", ["dehpag", "wwxgqq"])

### EXPERIMENT
constraints=[ExactlyK(3,(gzepk,"mzr")),AtLeastKInARow(2,(xlfcmx,"yelac")),MinimumTrials(48)]
design=[gzepk,xlfcmx,ameud,wnh,rxvqmd,mzsfvk]
crossing=[wnh,rxvqmd,mzsfvk]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END