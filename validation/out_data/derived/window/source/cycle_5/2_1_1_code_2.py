from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zdak = Factor("zdak", ["ggre","xxp","ibydm","ylnped","oiudo"])
def is_bzrh_oixwnd(zdak):
    return zdak[-2] == "xxp" or zdak[0] != "ggre"
def is_bzrh_kwdpox(zdak):
    return not is_bzrh_oixwnd(zdak)
bzrh = Factor("bzrh", [DerivedLevel("oixwnd", Window(is_bzrh_oixwnd, [zdak], 3, 1)), DerivedLevel("kwdpox", Window(is_bzrh_kwdpox, [zdak], 3, 1))])

design=[zdak,bzrh]
crossing=[bzrh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END