from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kzyW= Factor("kzyW", [Level("mQ30", 4), Level("eL3ohDXn", 1), Level(";CURDohH", 1), Level("Z$Pnf^", 1), Level("A]8NtVkkCZ", 2), Level("3rFK^E(vzT", 7)])

design=[kzyW]
crossing=[kzyW]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_1_0"))

### END
