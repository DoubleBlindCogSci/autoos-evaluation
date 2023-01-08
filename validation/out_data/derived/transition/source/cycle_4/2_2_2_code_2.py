from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
shdi = Factor("shdi", ["yetkbx","qdkggy","zsrvfd","lsz","iomwsu","spxtfk"])
zbahnb = Factor("zbahnb", ["hzzgg","fttwj","gvlyd","dfhilo","oggzmn","acli","xfifs"])
def is_dpnj_xtnum(shdi, zbahnb):
    return shdi[0] != "zsrvfd" and zbahnb[-1] != "fttwj"
def is_dpnj_pop(shdi, zbahnb):
    return not is_dpnj_xtnum(shdi, zbahnb)
dpnj= Factor("dpnj", [DerivedLevel("xtnum", Transition(is_dpnj_xtnum, [shdi, zbahnb])), DerivedLevel("pop", Transition(is_dpnj_pop, [shdi, zbahnb]))])

design=[shdi,zbahnb,dpnj]
crossing=[dpnj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END