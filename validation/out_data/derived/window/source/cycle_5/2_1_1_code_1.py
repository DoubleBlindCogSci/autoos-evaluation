from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zdak = Factor("zdak", ["ggre","xxp","ibydm","ylnped","oiudo"])
def irvb(zdak):
    return zdak[-2] == "xxp" or zdak[0] != "ggre"
def rvtgby(zdak):
    return not (zdak[-2] == "xxp") and not (zdak[-2] != "ggre")
xdiwh = DerivedLevel("oixwnd", Window(irvb, [zdak],3,1))
xwrvw = DerivedLevel("kwdpox", Window(rvtgby, [zdak],3,1))
gqihnp = Factor("bzrh", [xdiwh, xwrvw])

### EXPERIMENT
design=[zdak,gqihnp]
crossing=[gqihnp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END