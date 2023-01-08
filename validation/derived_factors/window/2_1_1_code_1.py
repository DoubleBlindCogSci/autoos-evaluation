from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ess = Factor("ess", ["iowfse","qez","rir","nusbx","jfbht","adxuko","qxe"])
def rgynhn(ess):
    return ess[-1] != "qez" and ess[-2] != "iowfse"
def skwpvl(ess):
    return ess[-1] == "qez" or not (ess[-2] != "iowfse")
ozaha = DerivedLevel("llat", Window(rgynhn, [ess],3,1))
qfbkan = DerivedLevel("dksrk", Window(skwpvl, [ess],3,1))
hvyd = Factor("wfrxc", [ozaha, qfbkan])

### EXPERIMENT
design=[ess,hvyd]
crossing=[hvyd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END