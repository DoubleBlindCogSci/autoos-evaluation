from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hiyv = Factor("hiyv", ["ygbj", "htyl"])
mnhchw = Factor("mnhchw", ["gkvaa", "zkwqsk"])
bcwn = Factor("bcwn", ["khkkt", "ehw"])
akif = Factor("akif", ["rwhjv", "npi"])

### EXPERIMENT
design=[hiyv,mnhchw,bcwn,akif]
crossing=[[hiyv,mnhchw,bcwn,akif]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1"))
### END