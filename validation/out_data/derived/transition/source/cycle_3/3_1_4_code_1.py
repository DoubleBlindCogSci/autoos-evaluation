from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nwk = Factor("nwk", ["fvnll","joayyf","hump","img","muti","pncppn","fwkjs","vkfvf"])
def uffmti(nwk):
     return nwk[0] == "hump" and not nwk[-1] == "pncppn"
def xup(nwk):
     return (not "hump" != nwk[0]) and  nwk[-1] == "pncppn"
def rsuir(nwk):
     return (not uffmti(nwk)) and (not nwk[-1] == "pncppn")
owo = DerivedLevel("boqyr", Transition(uffmti, [nwk]))
qapv = DerivedLevel("xfme", Transition(xup, [nwk]))
gghw = DerivedLevel("ppjfl", Transition(rsuir, [nwk]))
ybtlj = Factor("twha", [owo, qapv, gghw])

### EXPERIMENT
design=[nwk,ybtlj]
crossing=[ybtlj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END