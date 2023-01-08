from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JXOI = Factor("JXOI", [Level("BEpuBY", 1), Level("N^SGXto|Cngvs", 1), Level("I$mGyTQu", 2), Level("jucV", 10), Level("CYQENSCtLMWpHT", 1), Level("b5X", 1)])

design=[JXOI]
crossing=[JXOI]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_1"))

### END
