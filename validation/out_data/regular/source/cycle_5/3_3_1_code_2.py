from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
F_n = Factor("F$n", [Level("gmrmqdrbV", 1), Level("iOWlqg$4Q", 2), Level("d>fkJUcT", 1)])
FNqnN_jO_W = Factor("FNqnN%jO4W", ["NEBDXKo", "jUlB[lEE", "LJzRmosfFX"])
zaOMtPyNtYct = Factor("zaOMtPyNtYct", ["jo~|WwwoNpBiUF", "8hEFb", "GXNN4C1wi"])

design=[F_n,FNqnN_jO_W,zaOMtPyNtYct]
crossing=[F_n,FNqnN_jO_W,zaOMtPyNtYct]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_1"))

### END
