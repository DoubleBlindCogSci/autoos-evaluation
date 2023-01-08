from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
beq = Factor("beq", ["bqxbgz","uzh","ukgsuf","ckpm","mdcqbm"])
def oobc(beq):
    return beq[0] != "mdcqbm" and beq[-1] == "ukgsuf"
def rrlln(beq):
    return not (beq[0] != "mdcqbm") or not (beq[0] == "ukgsuf")
wolw = DerivedLevel("nopy", Transition(oobc, [beq]))
hzmf = DerivedLevel("emmbr", Transition(rrlln, [beq]))
hbzhvy = Factor("jbntgn", [wolw, hzmf])

### EXPERIMENT
design=[beq,hbzhvy]
crossing=[hbzhvy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END