from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ljyd = Factor("ljyd", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
fxklzn = Factor("fxklzn", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
wykjm = Factor("wykjm", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
def entzqv(ljyd, wykjm, fxklzn):
    return ljyd[0] != wykjm[-1] or ljyd[-1] == fxklzn[0]
def ifaxww(ljyd, wykjm, fxklzn):
    return not entzqv(ljyd, wykjm, fxklzn)
qwcmdo = Factor("nhhng", [DerivedLevel("ubgi", Transition(entzqv, [ljyd, fxklzn, wykjm])), DerivedLevel("tiggrl", Transition(ifaxww, [ljyd, fxklzn, wykjm]))])
### EXPERIMENT
design=[ljyd,fxklzn,wykjm,qwcmdo]
crossing=[qwcmdo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END