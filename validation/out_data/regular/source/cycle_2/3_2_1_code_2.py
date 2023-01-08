from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
UN _V[2fs = Factor("UN _V[2fs", [Level("lyOOD[0U>uxX", 3), Level("QSOx9Ljaxj", 1), Level("kSg", 1)])
F_Q_XrOfyoLdMm = Factor("F9Q>XrOfyoLdMm", [Level("EpXmH", 10), Level("JlQX9", 1), Level("R1#V", 8)])

design=[F_Q_XrOfyoLdMm]
crossing=[F_Q_XrOfyoLdMm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
