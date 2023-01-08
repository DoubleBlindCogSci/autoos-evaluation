from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ess = Factor("ess", ["iowfse","qez","rir","nusbx","jfbht","adxuko","qxe"])
def is_wfrxc_llat(ess):
    return ess[-1] != "qez" and ess[-2] != "iowfse"
def is_wfrxc_dksrk(ess):
    return not is_wfrxc_llat(ess)
wfrxc = Factor("wfrxc", [DerivedLevel("llat", Window(is_wfrxc_llat, [ess], 3, 1)), DerivedLevel("dksrk", Window(is_wfrxc_dksrk, [ess], 3, 1))])

design=[ess,wfrxc]
crossing=[wfrxc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END