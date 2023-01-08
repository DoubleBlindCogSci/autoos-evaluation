from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
woa = Factor("woa", ["jjbf","tmxd", "jmo"])
ssvhq = Factor("ssvhq", ["swxqp","vkorxn", "jegphi"])
hcmjtm = Factor("hcmjtm", ["avg", "whmy"])

### EXPERIMENT
constraints=[AtLeastKInARow(4,(woa,"jmo"))]
design=[woa,ssvhq,hcmjtm]
crossing=[ssvhq,hcmjtm]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END