from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
szaa = Factor("szaa", ["gcjifk","bhghwo","mqa","ziyrmo","wsnxr","wea"])
def usl(szaa):
    return szaa[0] == "wea" and szaa[-1] == "ziyrmo"
def azahj(szaa):
    return not usl(szaa)
mqd = DerivedLevel("tmgjgv", Transition(usl, [szaa]))
nkelfv = DerivedLevel("ttx", Transition(azahj, [szaa]))
izll = Factor("npswlj", [mqd, nkelfv])

### EXPERIMENT
design=[szaa,izll]
crossing=[izll]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END