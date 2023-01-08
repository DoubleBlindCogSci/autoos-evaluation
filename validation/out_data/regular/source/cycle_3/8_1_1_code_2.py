from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_eEupC_Jwie = Factor("_eEupC2Jwie", [Level("PcVtxJnQCXGZnq", 10), Level("S?mAlmsWc", 1), Level("KKVbMI9x5", 9), Level("N^LhliXCbH?lT", 8), Level("kXOOQcLN$lEf", 7), Level("My}akkTrp", 6), Level("U]CBm", 4), Level("DTMyiaIZ", 3)])

design=[_eEupC_Jwie]
crossing=[_eEupC_Jwie]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_1"))

### END
