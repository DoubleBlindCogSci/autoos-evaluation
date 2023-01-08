from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
epf = Factor("epf", ["aae","pfezr", "dge"])
clfx = Factor("clfx", ["smak","dfvmwf","qhftpk", "gcxzn"])
xbhpdm = Factor("xbhpdm", ["jpbyaz", "cxkhi"])


constraints = [ExactlyK(4,(epf, "dge"))]
crossing = [clfx, xbhpdm]

design=[epf,clfx,xbhpdm]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_0"))

### END