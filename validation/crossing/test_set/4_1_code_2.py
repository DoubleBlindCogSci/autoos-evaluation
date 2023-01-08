from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hiyv = Factor("hiyv", ["ygbj", "htyl"])
mnhchw = Factor("mnhchw", ["gkvaa", "zkwqsk"])
bcwn = Factor("bcwn", ["khkkt", "ehw"])
akif = Factor("akif", ["rwhjv", "npi"])
constraints = []
crossing = [hiyv, mnhchw, bcwn, akif]


design=[hiyv,mnhchw,bcwn,akif]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1"))

### END