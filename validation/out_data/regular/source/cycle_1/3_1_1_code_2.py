from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yzVj__cdkx= Factor("yzVj[%cdkx", [Level("M5f YwhvoB6Up", 2), "v}Q", "$vFDzKwzEwVMU"])

design=[yzVj__cdkx]
crossing=[yzVj__cdkx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/3_1_1"))

### END
