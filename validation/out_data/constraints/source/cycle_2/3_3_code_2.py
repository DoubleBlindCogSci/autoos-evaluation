from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cxzr = Factor("cxzr", ["xjxh", "xwjjzr"])
zoupa = Factor("zoupa", ["oneas", "brupr"])
bnqm = Factor("bnqm", ["eqzv", "axe"])
pgp = Factor("pgp", ["bwd","dxnkad", "trqmsl"])
yysq = Factor("yysq", ["ugivpp","tfjl", "tvzwjc"])


constraints = [ExactlyK(4,(cxzr, "xwjjzr")), AtLeastKInARow(4,(zoupa, "brupr")), MinimumTrials(39)]
crossing = [pgp, yysq]

design=[cxzr,zoupa,bnqm,pgp,yysq]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3"))

### END