from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kwUCG = Factor("kwUCG", [Level("i;bnjNey", 6), Level("oyPYkKej", 1), Level("fMJP%>kIB: W", 1), Level("Xvt%QY[bbU", 1), Level("ApHCipr", 1), Level("i@GILK", 1), Level("BTo", 10)])

design=[kwUCG]
crossing=[kwUCG]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_0"))

### END
