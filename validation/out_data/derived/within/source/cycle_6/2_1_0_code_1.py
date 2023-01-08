from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nvxrqf = Factor("nvxrqf", ["ufzf","bba","aigkq","ruoqc","iaofn","gjcsc"])
def iqwfmj(nvxrqf):
    return nvxrqf == "ufzf"
def tlwk(nvxrqf):
    return nvxrqf != "ufzf"
xhbw = DerivedLevel("dnl", WithinTrial(iqwfmj, [nvxrqf]))
nea = DerivedLevel("sodo", WithinTrial(tlwk, [nvxrqf]))
pxvsb = Factor("tpqu", [xhbw, nea])

### EXPERIMENT
design=[nvxrqf,pxvsb]
crossing=[pxvsb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END