from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dPsIbBsXpE = Factor("dPsIbBsXpE", ["pPRUvEyTvE", "jxlzg}LvS$QelF", "CtG6z5qtQ0GPK", "YE*aR", "M4qy&Lm6x", "ZJVQThen", "QFD WY}bgsolVL", "SfM;p"])
_pWH = Factor("&pWH", ["D;vqqfmDlaG8", "QdO*m9DVjw", "LT}w^F2(", "{3egwQj", "0pB?G", "zzn", "YBzuuR", "BxwMlgclUw", "NycuKWQGvd"])

design=[dPsIbBsXpE,_pWH]
crossing=[dPsIbBsXpE,_pWH]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_2_1"))

### END
