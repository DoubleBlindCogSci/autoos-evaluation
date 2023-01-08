from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
usnma = Factor("usnma", ["lbr","pzb", "tptf"])
wbwg = Factor("wbwg", ["pokd","uqejlq","sexe", "qylc"])
lsif = Factor("lsif", ["agapij","ocwsr","sni", "rcofdx"])


constraints = [AtLeastKInARow(2, (usnma, "tptf")), Exclude((wbwg, "qylc"))]
crossing = [lsif]

design=[usnma,wbwg,lsif]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END