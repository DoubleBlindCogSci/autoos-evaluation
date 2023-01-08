from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hwcri = Factor("hwcri", ["hipky","uwsc","cpkgs","ghvkz","kwxymw","vpz","xgg"])
def is_uwmv_duaqe(hwcri):
    return hwcri[0] == "kwxymw" and hwcri[-1] != "xgg"
def is_uwmv_axiti(hwcri):
    return hwcri[0] != "kwxymw" and hwcri[-1] == "xgg"
def is_uwmv_cco(hwcri):
    return not (is_uwmv_duaqe(hwcri) or is_uwmv_axiti(hwcri))
uwmv = Factor("uwmv", [DerivedLevel("duaqe", Transition(is_uwmv_duaqe, [hwcri])), DerivedLevel("axiti", Transition(is_uwmv_axiti, [hwcri])), DerivedLevel("cco", Transition(is_uwmv_cco, [hwcri]))])

design=[hwcri,uwmv]
crossing=[uwmv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END