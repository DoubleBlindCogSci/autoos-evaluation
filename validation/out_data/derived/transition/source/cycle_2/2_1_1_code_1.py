from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rjaw = Factor("rjaw", ["kjzxjz","fkez","xepdr","wodnb","autly","fuq"])
def ihhfs(rjaw):
    return rjaw[0] != "wodnb" and rjaw[-1] == "xepdr"
def tunbf(rjaw):
    return not ihhfs(rjaw)
ycx = Factor("kumm", [DerivedLevel("endn", Transition(ihhfs, [rjaw])), DerivedLevel("bwbhn", Transition(tunbf, [rjaw]))])
### EXPERIMENT
design=[rjaw,ycx]
crossing=[ycx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END