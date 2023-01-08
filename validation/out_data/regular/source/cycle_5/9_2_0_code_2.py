from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
foBeAcVgYj_ = Factor("foBeAcVgYj2", [Level("vjVFCEItOwt", 1), Level("cDYFfFf", 1), Level("IHCmSJdC}zeC", 1), Level("ocwU!Twxuzfb", 3), Level("wwTPgoo", 1), Level("Q]*zLlDSt", 1), Level("a{bY%MZCIQpMDh", 1), Level("GIHDEImSQxS", 1), Level("MA0YAZ 9ODft", 2), Level("FAFAYrA1u|I", 3), Level("ocwU!Twxuzfb", 3)])
PyzP = Factor("PyzP", [Level("mFDTa", 1), Level("opoKtKkNvzhj", 1), Level("JhDjc0_g", 1), Level("odIFPim}ZXvC", 1), Level("Sqo<KujF}", 1), Level("QG}HqG[ER7", 1), Level("gergxGLBPT7IV", 1), Level("AXcg3E~yxM", 1), Level("Lttv", 1)])

design=[foBeAcVgYj_,PyzP]
crossing=[foBeAcVgYj_,PyzP]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_0"))

### END
