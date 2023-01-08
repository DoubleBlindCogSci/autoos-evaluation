from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZcVTYelGRDwiLI= Factor("ZcVTYelGRDwiLI", [Level("EsIV&NsehpG", 3), Level("xXZuP2Q!j", 1), Level("lndsygsw", 1), Level("eHaDuiVxT_sN", 1), Level("gm{mCNR", 1), Level("dFE3NILI", 1), Level("uFs;GbsDPg~1", 1)])
IadPijzVwc_d= Factor("IadPijzVwc8d", [Level("6xwBm|ciNVy", 6), Level("fGz$pJYD", 4), Level("Effa", 1), Level("zDGDrLhpaCJ&9", 1), Level("UiG8vrx}dSX", 1), Level("KdfZeOlTmj", 1), Level("W2CUuVxL", 1)])

design=[ZcVTYelGRDwiLI,IadPijzVwc_d]
crossing=[ZcVTYelGRDwiLI,IadPijzVwc_d]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/7_2_1"))

### END
