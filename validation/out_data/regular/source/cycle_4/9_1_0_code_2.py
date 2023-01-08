from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kMXgAq = Factor("kMXgAq", [Level("RZzjWytRXBYKMC", 1), Level("gkk0TGK(GvI", 1), Level("aAQXO_", 1), Level("z!", 2), Level("N6esUhr[6", 1), Level("hK{k7N", 1), Level("TxGFPUBhBx", 1), Level("vpulRruR|Kih", 1), Level("l;", 3), Level("riM", 1)])

design=[kMXgAq]
crossing=[kMXgAq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_1_0"))

### END
