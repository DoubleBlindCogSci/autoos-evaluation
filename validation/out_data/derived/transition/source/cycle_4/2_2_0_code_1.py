from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zbl = Factor("zbl", ["ecmf","kdv","ymd","vpiv","wfcfy"])
jvc = Factor("jvc", ["heic","flb","pgw","nosjfm","mcbage","sdixdv"])
def pseno(zbl, jvc):
    return zbl[0] != "vpiv" and jvc[-1] != "heic"
def zcdfq(zbl,jvc):
    return not pseno(zbl, jvc)
grx = DerivedLevel("scp", Transition(pseno, [zbl, jvc]))
japhbg = DerivedLevel("kelr", Transition(zcdfq, [zbl, jvc]))
adu = Factor("tnq", [grx, japhbg])

### EXPERIMENT
design=[zbl,jvc,adu]
crossing=[adu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END