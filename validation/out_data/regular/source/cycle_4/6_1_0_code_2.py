from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pyOE_N_yFBpB = Factor("pyOE~N7yFBpB", [Level("IDtdzk(QdMaMl", 1), Level("wrbmtjn#CxL", 1), Level("Q2Y", 1), Level("H&bDpC", 1), Level(":VAJHl${Lso", 1), Level("XmEcAJgQYMNJf", 1), Level("DY5", 1)])

design=[pyOE_N_yFBpB]
crossing=[pyOE_N_yFBpB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_0"))

### END
