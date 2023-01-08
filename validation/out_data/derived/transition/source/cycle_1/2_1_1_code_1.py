from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
exii = Factor("exii", ["fxb","ynmp","repr","znltjq","qsjul","irdbw"])
def pjri(exii):
    return exii[0] != "repr" and exii[-1] != "irdbw"
def ktv(exii):
    return not pjri(exii)
tbupwj = DerivedLevel("bsjhjv", Transition(pjri, [exii]))
hfuxyl = DerivedLevel("yaqd", Transition(ktv, [exii]))
jwjmf = Factor("ujsa", [tbupwj, hfuxyl])

### EXPERIMENT
design=[exii,jwjmf]
crossing=[jwjmf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END