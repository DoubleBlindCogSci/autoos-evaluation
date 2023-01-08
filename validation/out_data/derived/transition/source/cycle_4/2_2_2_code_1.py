from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
shdi = Factor("shdi", ["yetkbx","qdkggy","zsrvfd","lsz","iomwsu","spxtfk"])
zbahnb = Factor("zbahnb", ["hzzgg","fttwj","gvlyd","dfhilo","oggzmn","acli","xfifs"])
def kjm(shdi, zbahnb):
    return shdi[0] != "zsrvfd" and zbahnb[-1] != "fttwj"
def adc(shdi,zbahnb):
    return not (shdi[0] != "zsrvfd") or zbahnb[-1] == "fttwj"
ccmh = DerivedLevel("xtnum", Transition(kjm, [shdi, zbahnb]))
mod = DerivedLevel("pop", Transition(adc, [shdi, zbahnb]))
zrhi = Factor("dpnj", [ccmh, mod])

### EXPERIMENT
design=[shdi,zbahnb,zrhi]
crossing=[zrhi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END