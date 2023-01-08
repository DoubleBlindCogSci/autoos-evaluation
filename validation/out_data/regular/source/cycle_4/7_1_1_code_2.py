from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
QpxkUz_vdhp = Factor("QpxkUz~vdhp", [Level("o20tcr", 4), Level("E#K", 1), Level("bkZgz[q:HF8hxt", 1), Level("TRdM$5L", 2), Level("nqlL?&XL", 1), Level("vqg", 4), Level("7^QxENEOxB", 1), Level("YeaGAaZv5M", 1)])

design=[QpxkUz_vdhp]
crossing=[QpxkUz_vdhp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_1"))

### END
