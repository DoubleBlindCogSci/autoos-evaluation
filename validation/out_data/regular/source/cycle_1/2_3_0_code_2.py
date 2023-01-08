from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HtCPuxXG= Factor("HtCPuxXG", ["mUWJ[VHkU", "pDaTAkwbK["])
x__VYLN= Factor("x&}VYLN", ["INxF(e5pv", "lNzHD"])
gHs= Factor("gHs", ["BkFi3BXfDs6dZ", "HVdvc&>;<iZ*"])

design=[HtCPuxXG,x__VYLN,gHs]
crossing=[HtCPuxXG,x__VYLN,gHs]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/2_3_0"))

### END
