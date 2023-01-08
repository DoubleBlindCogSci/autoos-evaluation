from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
m_PHyvQ = Factor("m&PHyvQ", [Level("i#D)yTu3P", 5), Level("lvIY:P?MB", 1), Level("DZsh", 1)])
vVp_b = Factor("vVp b", [Level("PFYD5", 1), Level("FtU<PsDEEGvBN<", 1), Level("*RO6qw$lFxs", 4)])
pzr_XuysBLwLxh = Factor("pzr[XuysBLwLxh", [Level("VxaIv:XbDfJ", 1), Level("sAfRl", 1), Level("#8zqe", 10)])

design=[m_PHyvQ,vVp_b,pzr_XuysBLwLxh]
crossing=[m_PHyvQ,vVp_b,pzr_XuysBLwLxh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_0"))

### END
