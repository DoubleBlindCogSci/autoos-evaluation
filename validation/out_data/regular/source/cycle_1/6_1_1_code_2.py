from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nY_kjAPaEC= Factor("nY6kjAPaEC", [Level("L8z", 1), Level("3$ms", 1), Level("GErthOVs", 4), Level("ZcOO{RhA;oIpcx", 1), Level("sZcZqO<Pv ", 1), Level("hBWKh", 1)])

design=[nY_kjAPaEC]
crossing=[nY_kjAPaEC]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_1_1"))

### END
