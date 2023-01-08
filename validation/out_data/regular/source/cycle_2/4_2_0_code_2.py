from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
W_MTKU__WBN = Factor("W4MTKU~&WBN", [Level("WoGI;cWf", 7), Level("cybb", 1), Level("cJeCRLrkOBQ", 1), Level("tmsC4J;S", 2), Level("Yiv3rpTs[nX@Ay", 1)])
NvR___FrEbD = Factor("NvR?6@FrEbD", [Level("tsNCPlUL?", 1), Level("bBQHegf", 6), Level("%KvACU", 1), Level("lYOcU", 1)])

design=[W_MTKU__WBN,NvR___FrEbD]
crossing=[W_MTKU__WBN,NvR___FrEbD]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_0"))

### END
