from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iVRovMGdzNfOdK= Factor("iVRovMGdzNfOdK", ["I{v&4DOXZf", "#hM", "J7G", "v6Mn~RkqfVXp"])

design=[iVRovMGdzNfOdK]
crossing=[iVRovMGdzNfOdK]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_1_0"))

### END
