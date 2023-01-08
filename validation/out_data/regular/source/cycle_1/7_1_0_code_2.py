from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
H_ymIW__= Factor("H#ymIW:&", [Level("qWFHHX:jFVOvX", 3), Level("rNif", 1), Level("TEFwkWzmYBth", 1), Level("jdhGrna", 1), Level("JVz", 7), Level("2t&coV#X", 1), Level("ahT", 1), Level("FoyjlRy}Q~r", 1)])

design=[H_ymIW__]
crossing=[H_ymIW__]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/7_1_0"))

### END
