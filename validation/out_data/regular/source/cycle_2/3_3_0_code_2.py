from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wP_lSU_Jo = Factor("wP!lSU:Jo", ["DH0m", "HCmbqdwc", "LDpdEOjb "])
JGAH = Factor("JGAH", [Level("<lakDe ^]GVW", 1), Level("ZG|yNqHHCj", 1), Level("Ccj6hzwXo", 10)])
_jInqv_ochDhc = Factor("]jInqv9ochDhc", [Level("QzCKug", 1), Level("ausuT5", 6), Level("zHC9vPvYw", 1)])

design=[wP_lSU_Jo,JGAH,_jInqv_ochDhc]
crossing=[wP_lSU_Jo,JGAH,_jInqv_ochDhc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_0"))

### END
