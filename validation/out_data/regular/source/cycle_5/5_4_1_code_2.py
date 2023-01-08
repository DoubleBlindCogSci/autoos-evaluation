from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bxJb = Factor("bxJb", [";PVCO$aWcbz", "ylo6Y}V", "BdY#FTkBv", "rKo", "pZIl"])
VlJ = Factor("VlJ", [Level("AqzS}Bf", 1), Level("r?Tjbj!MM", 3), Level("T DkVkh^hG9", 1), Level("UuftnN ", 1), Level("~eXNL5nuuW", 1)])
MhQr = Factor("MhQr", ["TpZUe", "FaJq8okZsp<", "FpBVsTuVHl(:pE", "Z$p", "?gvaU"])
fPimoTeuEI_ = Factor("fPimoTeuEI{", ["M$[LlIlc&0qii", "4GK:qMKh", "uvyeANtA", "Tec*DFIour", "fiVqrMgCrZfq"])

design=[bxJb,VlJ,MhQr,fPimoTeuEI_]
crossing=[bxJb,VlJ,MhQr,fPimoTeuEI_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_4_1"))

### END
