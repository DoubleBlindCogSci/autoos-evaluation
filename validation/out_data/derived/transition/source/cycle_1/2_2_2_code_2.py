from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ljyd= Factor("ljyd", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
fxklzn= Factor("fxklzn", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
wykjm= Factor("wykjm", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
def is_nhhng_ubgi(ljyd, fxklzn, wykjm):
    return ljyd[0] != wykjm[-1] or ljyd[0] == fxklzn[-1]
def is_nhhng_tiggrl(ljyd, fxklzn, wykjm):
    return not is_nhhng_ubgi(ljyd, fxklzn, wykjm)
nhhng= Factor("nhhng", [DerivedLevel("ubgi", Transition(is_nhhng_ubgi, [ljyd, fxklzn, wykjm])), DerivedLevel("tiggrl", Transition(is_nhhng_tiggrl, [ljyd, fxklzn, wykjm]))])

design=[ljyd,fxklzn,wykjm,nhhng]
crossing=[nhhng]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
