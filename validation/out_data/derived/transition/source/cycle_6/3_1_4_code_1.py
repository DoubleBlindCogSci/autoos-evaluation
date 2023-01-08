from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
axxxy = Factor("axxxy", ["gwlfl","hgte","nms","norqt","vxrjpm","dpvh"])
def bolf(axxxy):
     return "vxrjpm" == axxxy[0] and not axxxy[-1] == "hgte"
def jmvcxp(axxxy):
     return (axxxy[0] != "vxrjpm") and  "hgte" == axxxy[-1]
def pox(axxxy):
     return (axxxy[0] != "vxrjpm") and (not jmvcxp(axxxy))
dzqjyv = Factor("dirfp", [DerivedLevel("ksw", Transition(bolf, [axxxy])), DerivedLevel("sjt", Transition(jmvcxp, [axxxy])),DerivedLevel("flwqk", Transition(pox, [axxxy]))])
### EXPERIMENT
design=[axxxy,dzqjyv]
crossing=[dzqjyv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END