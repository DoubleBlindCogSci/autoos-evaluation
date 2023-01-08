from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
blfi = Factor("blfi", ["xrnn","rlkzh","npeot","csob","aivye","poogo","hmoz","ptqeqs"])
rqnon = Factor("rqnon", ["ekaq","yonm","nhq","dtojhe","xjijq","cww","cuwi"])
def is_aqw_uqln(blfi, rqnon):
    return blfi[-1] == "poogo" and rqnon[0] != "cuwi"
def is_aqw_lydag(blfi, rqnon):
    return blfi[-1] != "poogo" and rqnon[0] == "cuwi"
def is_aqw_enmxhf(blfi, rqnon):
    return not (is_aqw_uqln(blfi, rqnon) or is_aqw_lydag(blfi, rqnon))
aqw= Factor("aqw", [DerivedLevel("uqln", Transition(is_aqw_uqln, [blfi, rqnon])), DerivedLevel("lydag", Transition(is_aqw_lydag, [blfi, rqnon])), DerivedLevel("enmxhf", Transition(is_aqw_enmxhf, [blfi, rqnon]))])

design=[blfi,rqnon,aqw]
crossing=[aqw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
