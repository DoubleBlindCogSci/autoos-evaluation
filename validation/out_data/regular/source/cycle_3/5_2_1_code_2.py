from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mFqDNN_M_bv = Factor("mFqDNN!M;bv", [Level("zNetXJow", 5), Level("DfMFe", 1), Level("y_St", 1), Level("WxWi", 7), Level("kGiXa5<bdFP", 5)])
wR_XQip_ = Factor("wR?XQip4", [Level("KVkCfe", 1), Level("X3xzKAD", 1), Level("2xTlvaElNl", 1), Level("HwqO", 5), Level("Yjr", 1), Level("Lo>UHI", 1)])

design=[mFqDNN_M_bv,wR_XQip_]
crossing=[mFqDNN_M_bv,wR_XQip_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_1"))

### END
