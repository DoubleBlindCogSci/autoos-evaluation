from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
blfi = Factor("blfi", ["xrnn","rlkzh","npeot","csob","aivye","poogo","hmoz","ptqeqs"])
rqnon = Factor("rqnon", ["ekaq","yonm","nhq","dtojhe","xjijq","cww","cuwi"])
def imxkzh(blfi, rqnon):
     return blfi[-1] == "poogo" and rqnon[0] != "cuwi"
def dbw(blfi, rqnon):
     return "poogo" != blfi[-1] and rqnon[0] == "cuwi"
def gfxk(blfi, rqnon):
     return (not blfi[-1] == "poogo") and (rqnon[0] != "cuwi")
qki = DerivedLevel("uqln", Transition(imxkzh, [blfi, rqnon]))
fnugz = DerivedLevel("lydag", Transition(dbw, [blfi, rqnon]))
dckg = DerivedLevel("enmxhf", Transition(gfxk, [blfi, rqnon]))
ckx = Factor("aqw", [qki, fnugz, dckg])

### EXPERIMENT
design=[blfi,rqnon,ckx]
crossing=[ckx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END