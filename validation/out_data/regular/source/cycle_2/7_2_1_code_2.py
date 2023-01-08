from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MP_FzIHmqdW = Factor("MP7FzIHmqdW", [Level("{vrGALh#w", 7), Level("O8RV)rv{Vh", 1), Level("AT[w", 1), Level("!lIwNNNzZhXSE", 1), Level("byA^d<jnV", 1), Level("4NMpPWsLpj", 1), Level("ap~)y7bFUm!)", 1)])
RBx = Factor("RBx", [Level("Z4QEwqb", 8), Level("Q)HnCEu5I", 1), Level("d3nmjAaP", 1), Level("XPtVlLK2gKCrj", 10), Level("5S*MThl og>jN", 1), Level("fREIS5qcowiSjA", 1), Level("YbWiXA", 1), Level("Ko>0W", 1), Level("TlZM", 1)])

design=[MP_FzIHmqdW,RBx]
crossing=[MP_FzIHmqdW,RBx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_1"))

### END
