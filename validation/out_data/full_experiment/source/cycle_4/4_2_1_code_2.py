from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
wzltf = Factor("wzltf", ["wkh", "jfimzl"])
xkx = Factor("xkx", ["xdmxg", "yrlgcb"])
adasp = Factor("adasp", ["wkh", "jfimzl"])
kbdfej = Factor("kbdfej", ["xdmxg", "yrlgcb"])
def is_hwsmo_mpopni(wzltf, kbdfej):
    return wzltf == kbdfej
def is_hwsmo_wicxmx(wzltf, kbdfej):
    return not is_hwsmo_mpopni(wzltf, kbdfej)
hwsmo = Factor("hwsmo", [DerivedLevel("mpopni", WithinTrial(is_hwsmo_mpopni, [wzltf, kbdfej])), DerivedLevel("wicxmx", WithinTrial(is_hwsmo_wicxmx, [wzltf, kbdfej]))])
def is_ejihet_ylb(adasp, xkx):
    return adasp == xkx
def is_ejihet_fedzj(adasp, xkx):
    return not is_ejihet_ylb(adasp, xkx)
ejihet = Factor("ejihet", [DerivedLevel("ylb", WithinTrial(is_ejihet_ylb, [adasp, xkx])), DerivedLevel("fedzj", WithinTrial(is_ejihet_fedzj, [adasp, xkx]))])
constraints = [AtMostKInARow(2, adasp)]
crossing = [ejihet, kbdfej]

design=[wzltf,xkx,adasp,kbdfej,hwsmo,ejihet]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_1"))
