from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ybb = Factor("ybb", ["zlxvn","qnbiws","grsu", "xlbex"])
lhfi = Factor("lhfi", ["bus", "zcdpts"])
mlenz = Factor("mlenz", ["pvgv","ozx","flork", "mumnj"])
pqzau = Factor("pqzau", ["fhlk", "gkahpj"])


constraints = [AtMostKInARow(4, (ybb, "xlbex")), AtLeastKInARow(3, (lhfi, "zcdpts"))]
crossing = [mlenz, pqzau]

design=[ybb,lhfi,mlenz,pqzau]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END