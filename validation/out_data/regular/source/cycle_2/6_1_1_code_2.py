from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bKCN = Factor("bKCN", [Level(":NUysnqtG{iRn(", 10), Level("bVTtnrnteksEr", 6), Level("ySkzbupsM", 4), Level("fOS", 3), Level("3bbnhcbE", 1), Level("bzRkSJ", 1)])

design=[bKCN]
crossing=[bKCN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_1"))

### END
