from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
apgpx = Factor("apgpx", ["yjpav","hjyr","bfn","yvhm","hdfrzu","oyg"])
def is_ltb_euacj(apgpx):
    return apgpx[-1] == "hdfrzu" or apgpx[0] == "yvhm"
def is_ltb_ctra(apgpx):
    return not is_ltb_euacj(apgpx)
ltb= Factor("ltb", [DerivedLevel("euacj", Transition(is_ltb_euacj, [apgpx])), DerivedLevel("ctra", Transition(is_ltb_ctra, [apgpx]))])

design=[apgpx,ltb]
crossing=[ltb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
