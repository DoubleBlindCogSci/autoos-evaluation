from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
psxzzw = Factor("psxzzw", ["spa","iigdr","dhsxwz","urwb","sfr","hqigv","noe"])
def is_yknaja_sxxi(psxzzw):
    return psxzzw[-2] == "spa" and psxzzw[0] != "spa"
def is_yknaja_hsrtsa(psxzzw):
    return psxzzw[-2] != "spa" and psxzzw[0] == "iigdr"
def is_yknaja_ile(psxzzw):
    return not (is_yknaja_sxxi(psxzzw) or is_yknaja_hsrtsa(psxzzw))
yknaja = Factor("yknaja", [DerivedLevel("sxxi", Window(is_yknaja_sxxi, [psxzzw], 3, 1)), DerivedLevel("hsrtsa", Window(is_yknaja_hsrtsa, [psxzzw], 3, 1)), DerivedLevel("ile", Window(is_yknaja_ile, [psxzzw], 3, 1))])

design=[psxzzw,yknaja]
crossing=[yknaja]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END