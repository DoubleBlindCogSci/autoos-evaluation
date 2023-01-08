from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
opoq = Factor("opoq", ["aonory","ilst","hjph","rsn","ovie","yvqo","fkdakj"])
def qhrvq(opoq):
     return opoq == "rsn"
def qefr(opoq):
     return opoq == "yvqo"
def xro(opoq):
     return (opoq != "rsn") and (opoq != "yvqo")
ged = DerivedLevel("nusuv", WithinTrial(qhrvq, [opoq]))
eto = DerivedLevel("plz", WithinTrial(qefr, [opoq]))
eagyxh = DerivedLevel("hhq", WithinTrial(xro, [opoq]))
vsyap = Factor("ddehh", [ged, eto, eagyxh])

### EXPERIMENT
design=[opoq,vsyap]
crossing=[vsyap]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END