from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
__J_D_CHMhfZqE = Factor(">#J5D7CHMhfZqE", [Level("qlQfUqJ{G", 1), Level("iXbtgrA", 1), Level("dTyqjFcmcBE>L", 1), Level("C8VeWdMnu1dwni", 1), Level("ScqNV_", 1), Level("PGEgKoJep", 1), Level("f:ngJai5?j^s", 1), Level("g#OlCG", 1), Level("R<f", 3)])

design=[__J_D_CHMhfZqE]
crossing=[__J_D_CHMhfZqE]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_1"))

### END
