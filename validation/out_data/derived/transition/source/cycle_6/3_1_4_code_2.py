from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
axxxy = Factor("axxxy", ["gwlfl","hgte","nms","norqt","vxrjpm","dpvh"])
def is_dirfp_ksw(axxxy):
    return axxxy[0] == "vxrjpm" and axxxy[-1] != "hgte"
def is_dirfp_sjt(axxxy):
    return axxxy[0] != "vxrjpm" and axxxy[-1] == "hgte"
def is_dirfp_flwqk(axxxy):
    return not (is_dirfp_ksw(axxxy) or is_dirfp_sjt(axxxy))
dirfp = Factor("dirfp", [DerivedLevel("ksw", Transition(is_dirfp_ksw, [axxxy])), DerivedLevel("sjt", Transition(is_dirfp_sjt, [axxxy])), DerivedLevel("flwqk", Transition(is_dirfp_flwqk, [axxxy]))])

design=[axxxy,dirfp]
crossing=[dirfp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END