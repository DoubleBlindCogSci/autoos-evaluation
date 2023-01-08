from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vsro = Factor("vsro", ["gloon","eqoo","vuu","kquio","wun","afivz"])
def dlf(vsro):
     return "kquio" == vsro
def addpu(vsro):
     return "wun" == vsro
def izxzxt(vsro):
     return (not dlf(vsro)) and (not vsro == "wun")
ysab = DerivedLevel("gjctkf", WithinTrial(dlf, [vsro]))
wvzpq = DerivedLevel("jshfbz", WithinTrial(addpu, [vsro]))
jyadpw = DerivedLevel("jhcmef", WithinTrial(izxzxt, [vsro]))
xvfcd = Factor("giq", [ysab, wvzpq, jyadpw])

### EXPERIMENT
design=[vsro,xvfcd]
crossing=[xvfcd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END