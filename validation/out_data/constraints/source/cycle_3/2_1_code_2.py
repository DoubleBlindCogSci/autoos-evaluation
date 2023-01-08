from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pjc = Factor("pjc", ["hsh","ddh", "nspchy"])
jjptqo = Factor("jjptqo", ["smhs", "cnhxtr"])
ned = Factor("ned", ["rzc","dgvq","isrwm", "pgl"])


constraints = [AtMostKInARow(3, (pjc, "nspchy")), AtLeastKInARow(4, (jjptqo, "cnhxtr"))]
crossing = [ned]

design=[pjc,jjptqo,ned]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END