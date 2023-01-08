from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
askal= Factor("askal", ["rkwp","kmd","wwk","pbwgni","rir"])
def is_ytik_mwumrz(askal):
    return askal == "wwk" and askal != "rir"
def is_ytik_qtz(askal):
    return askal == "rir" or askal != "wwk"
ytik= Factor("ytik", [DerivedLevel("mwumrz", WithinTrial(is_ytik_mwumrz, [askal])), DerivedLevel("qtz", WithinTrial(is_ytik_qtz, [askal]))])

design=[askal, ytik]
crossing=[ytik]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
