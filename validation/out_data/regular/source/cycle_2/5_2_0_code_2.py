from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IRFBTnR = Factor("IRFBTnR", [Level("IQJL", 10), Level("3&h)AV", 1), Level("UUHMmNSxl", 1), Level("qrFthpS|tVeHWJ", 6), Level("GGI5Fea", 1), Level("kTSZa?Gz", 1), Level("dXEpv#xE[inoJd", 10)])
TPlnvC_ = Factor("TPlnvC*", [Level("zP%yvoiE?Bv)y", 1), Level("cS&ThNN", 6), Level("vPZpS", 1), Level("qcZYKB", 6), Level("RYc", 1)])

design=[IRFBTnR,TPlnvC_]
crossing=[IRFBTnR,TPlnvC_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_0"))

### END
