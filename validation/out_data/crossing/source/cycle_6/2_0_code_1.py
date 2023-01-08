from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gim = Factor("gim", ["lmkoef", "ojexz"])
fitizi = Factor("fitizi", ["gkmvyq", "dujpc"])
uyk = Factor("uyk", ["xlhztr", "fnufnc"])
eajyk = Factor("eajyk", ["wetcw", "pvxnxs"])
whjgl = Factor("whjgl", ["sgtm", "itqwt"])

### EXPERIMENT
design=[gim,fitizi,uyk,eajyk,whjgl]
crossing=[[gim,fitizi,uyk],[eajyk,whjgl],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_0"))
### END