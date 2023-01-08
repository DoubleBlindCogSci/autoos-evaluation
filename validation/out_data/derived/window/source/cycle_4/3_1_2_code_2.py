from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fmxd = Factor("fmxd", ["vhlg","maa","hcosa","unh","wqsak","ioxf"])
def is_knikh_wnlbw(fmxd):
    return fmxd[-1] == "hcosa" and fmxd[0] != "hcosa"
def is_knikh_hsdr(fmxd):
    return fmxd[-1] != "hcosa" and fmxd[0] == "maa"
def is_knikh_nykz(fmxd):
    return not (is_knikh_wnlbw(fmxd) or is_knikh_hsdr(fmxd))
knikh = Factor("knikh", [DerivedLevel("wnlbw", Window(is_knikh_wnlbw, [fmxd], 2, 1)), DerivedLevel("hsdr", Window(is_knikh_hsdr, [fmxd], 2, 1)), DerivedLevel("nykz", Window(is_knikh_nykz, [fmxd], 2, 1))])

design=[fmxd,knikh]
crossing=[knikh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END