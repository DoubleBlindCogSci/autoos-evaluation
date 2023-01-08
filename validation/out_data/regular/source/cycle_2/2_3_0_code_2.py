from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
en_gxxvL = Factor("en gxxvL", [Level("kRtKnoE7XVWjvL", 1), Level("OSPyW{fR", 1), Level("FUWAO", 1)])
PaGCajYpIEehuq = Factor("PaGCajYpIEehuq", ["g*iu", "CSaQw"])
E__elRfqN = Factor("E[_elRfqN", [Level("U[x?obejL%", 8), Level("yjOmrT", 1)])

design=[en_gxxvL,PaGCajYpIEehuq,E__elRfqN]
crossing=[en_gxxvL,PaGCajYpIEehuq,E__elRfqN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_0"))

### END
