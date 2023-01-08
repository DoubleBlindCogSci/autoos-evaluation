from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qax = Factor("qax", ["laysc","tbdi", "jtmlcs"])
hgduyx = Factor("hgduyx", ["iwyr", "ewexc"])
czn = Factor("czn", ["cvxhp","btp","nvj", "yqvovc"])
qlrk = Factor("qlrk", ["qxszv", "tqjydm"])
sybqg = Factor("sybqg", ["prfug", "teuq"])


constraints = [ExactlyK(2, (qax, "jtmlcs")), Exclude((hgduyx, "ewexc")), AtMostKInARow(2, (czn, "yqvovc"))]
crossing = [[qlrk], [sybqg]]

design=[qax,hgduyx,czn,qlrk,sybqg]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3"))

### END