from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ufcU = Factor("ufcU", [Level("n *CPd", 1), Level("A1x %OydT", 10), Level("uIZZirH!kEYwIg", 7), Level("PIJGKRCnawR", 5), Level("(MatxpxIQo", 9), Level("UzD", 1), Level("nf9cvX", 1)])
QG = Factor("QG", [Level("*BFnz", 2), Level("wHtvDBrYsxy", 1), Level(";kFWwrleT", 1), Level("ABvq:YM^kO", 7), Level("1UROfWtA|HTbk", 1), Level("RthmVAcUJ%u]RT", 1), Level("ctS", 1)])

design=[ufcU,QG]
crossing=[ufcU,QG]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_1"))

### END
