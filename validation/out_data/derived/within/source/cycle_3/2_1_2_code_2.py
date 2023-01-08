from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eyffzz = Factor("eyffzz", ["qac","kkbcvv","hqe","upgqu","ccczq","wfx","fgacg"])
def is_itt_arby(eyffzz):
    return eyffzz != "upgqu"
def is_itt_teft(eyffzz):
    return not is_itt_arby(eyffzz)
itt= Factor("itt", [DerivedLevel("arby", WithinTrial(is_itt_arby, [eyffzz])), DerivedLevel("teft", WithinTrial(is_itt_teft, [eyffzz]))])

design=[eyffzz,itt]
crossing=[itt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
