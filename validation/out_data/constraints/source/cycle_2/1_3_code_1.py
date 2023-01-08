from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qit = Factor("qit", ["qem", "jtzsus"])
yqno = Factor("yqno", ["gpl","ucbu", "jzdh"])

### EXPERIMENT
constraints=[AtMostKInARow(3,(qit,"jtzsus"))]
design=[qit,yqno]
crossing=[yqno]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_3"))
### END