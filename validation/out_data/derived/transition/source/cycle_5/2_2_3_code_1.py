from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ligw = Factor("ligw", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
nwa = Factor("nwa", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
rcdafu = Factor("rcdafu", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
def mokiba(ligw, nwa, rcdafu):
    return ligw[0] == nwa[-1]
def wsgd(ligw, nwa, rcdafu):
    return ligw[0] != nwa[-1]
ivpzy = DerivedLevel("uyqqzq", Transition(mokiba, [ligw, nwa, rcdafu]))
hyyems = DerivedLevel("irgx", Transition(wsgd, [ligw, nwa, rcdafu]))
gujpcx = Factor("vsz", [ivpzy, hyyems])

### EXPERIMENT
design=[ligw,nwa,rcdafu,gujpcx]
crossing=[gujpcx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END