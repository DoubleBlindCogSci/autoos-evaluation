from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hbNsD_ILs = Factor("hbNsD9ILs", [Level("jyxr4n", 1), Level("KnydF5]Vw#N", 4)])

design=[hbNsD_ILs]
crossing=[hbNsD_ILs]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
