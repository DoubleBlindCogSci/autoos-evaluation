from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bU_QmWVBkTTKGI= Factor("bU3QmWVBkTTKGI", [Level("sxu9cN{pecKeH", 8), Level("N< LEsp_Pb", 1)])

design=[bU_QmWVBkTTKGI]
crossing=[bU_QmWVBkTTKGI]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/2_1_1"))

### END
