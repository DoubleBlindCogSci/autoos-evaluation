from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vlaGqWn_o = Factor("vlaGqWn9o", [Level("QExdHPz", 1), Level("PxuyEyg", 1), Level("pTTS_Cm!|fF", 1), Level("X[fYi5Y", 4), Level("bLQNt", 1), Level("jZCE|M", 1), Level("lhKZ2", 1), Level("fTGxLOrXBBhg", 1), Level("Tg}J#Tu", 1)])
XnN_xX_NLRvh = Factor("XnN}xX|NLRvh", [Level("9KwN(~[a T~mM", 1), Level("2QD}PUXxzDy)", 1), Level("AR?UqJjF$A1mT8", 1), Level("2qG(I", 1), Level("zcyOnK", 1), Level("Gczy", 1), Level("LfhTXQrFnc", 1)])

design=[vlaGqWn_o,XnN_xX_NLRvh]
crossing=[vlaGqWn_o,XnN_xX_NLRvh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_1"))

### END
