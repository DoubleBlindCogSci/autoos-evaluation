from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IoojsU = Factor("IoojsU", ["IQxnzYxWdit", "y fmBT}gqxsme", "xiDCDA>rI", "HXwO<pkYTBZns", "uMfQhhFTmMN", "s7G", "_lJKNI", "9zX3A]zV", "fOU"])

design=[IoojsU]
crossing=[IoojsU]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_1"))

### END
