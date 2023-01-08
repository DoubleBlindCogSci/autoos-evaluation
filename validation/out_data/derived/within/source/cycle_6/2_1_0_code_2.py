from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nvxrqf = Factor("nvxrqf", ["ufzf","bba","aigkq","ruoqc","iaofn","gjcsc"])
def is_tpqu_dnl(nvxrqf):
    return nvxrqf == "ufzf"
def is_tpqu_sodo(nvxrqf):
    return not is_tpqu_dnl(nvxrqf)
tpqu = Factor("tpqu", [DerivedLevel("dnl", WithinTrial(is_tpqu_dnl, [nvxrqf])), DerivedLevel("sodo", WithinTrial(is_tpqu_sodo, [nvxrqf]))])

design=[nvxrqf,tpqu]
crossing=[tpqu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END