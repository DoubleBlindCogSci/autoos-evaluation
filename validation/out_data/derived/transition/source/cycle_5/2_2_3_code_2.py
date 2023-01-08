from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ligw = Factor("ligw", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
nwa = Factor("nwa", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
rcdafu = Factor("rcdafu", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
def is_vsz_uyqqzq(ligw, nwa, rcdafu):
    return ligw[0] == nwa[-1]
def is_vsz_irgx(ligw, nwa, rcdafu):
    return not is_vsz_uyqqzq(ligw, nwa, rcdafu)
vsz = Factor("vsz", [DerivedLevel("uyqqzq", Transition(is_vsz_uyqqzq, [ligw, nwa, rcdafu])), DerivedLevel("irgx", Transition(is_vsz_irgx, [ligw, nwa, rcdafu]))])

design=[ligw,nwa,rcdafu,vsz]
crossing=[vsz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END