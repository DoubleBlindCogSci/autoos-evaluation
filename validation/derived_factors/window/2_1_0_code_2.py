from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mqt = Factor("mqt", ["gmbm","jezzl","dcea","tibpp","kwnm","vfd"])
def is_lwd_uvkig(mqt):
    return mqt[0] != "vfd" or mqt[-2] == "gmbm"
def is_lwd_hxxhr(mqt):
    return not is_lwd_uvkig(mqt)
lwd = Factor("lwd", [DerivedLevel("uvkig", Window(is_lwd_uvkig, [mqt], 3, 1)), DerivedLevel("hxxhr", Window(is_lwd_hxxhr, [mqt], 3, 1))])

design=[mqt,lwd]
crossing=[lwd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END