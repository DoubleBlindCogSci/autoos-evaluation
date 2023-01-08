from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ara = Factor("ara", ["zfixf","hky","diow", "rexvr"])
qvzmh = Factor("qvzmh", ["hywxxi","ymyrth","zliw", "edphtg"])
clyjhw = Factor("clyjhw", ["rfb","cpyux", "szkhcv"])


constraints = [ExactlyKInARow(3, (ara, "rexvr")), AtMostKInARow(2, (qvzmh, "edphtg"))]
crossing = [clyjhw]

design=[ara,qvzmh,clyjhw]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3"))

### END