from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mcR = Factor("mcR", [Level("Mzssd_TXadY", 1), Level("weZOt v<{t", 1), Level("gFryDiDbE1(aPH", 1), Level("EKm", 2), Level("*YCeDx", 1)])
_SsqUA = Factor("{SsqUA", ["anmNZzGN", "thussgpEZkkZg", "VWB~wR|S", "OPHshJj1Tu)5FF", "vPD", "edl&iqq"])
WzqR_ = Factor("WzqR3", ["RgCOfRe", "TEoHoo_EIR", "frHviA@FbvtiQ", "sQ#AYwsY", "wiPL"])

design=[mcR,_SsqUA,WzqR_]
crossing=[mcR,_SsqUA,WzqR_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_4_0"))

### END
