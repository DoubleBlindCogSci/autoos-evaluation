from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
T_dsoWn = Factor("T$dsoWn", [Level("VUlOnKNLYpW^", 5), Level(";SsnEj", 1)])
eS_i = Factor("eS?i", [Level("OxKNQLt", 1), Level("oZyMeSzICp", 7)])

design=[T_dsoWn,eS_i]
crossing=[T_dsoWn,eS_i]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
