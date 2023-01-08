### REGULAR FACTORS
wzltf = Factor("wzltf", ["wkh", "jfimzl"])
xkx = Factor("xkx", ["xdmxg", "yrlgcb"])
adasp = Factor("adasp", ["wkh", "jfimzl"])
kbdfej = Factor("kbdfej", ["xdmxg", "yrlgcb"])
### DERIVED FACTORS
##
def is_hwsmo_mpopni(wzltf, kbdfej):
    return wzltf == kbdfej
def is_hwsmo_wicxmx(wzltf, kbdfej):
    return not is_hwsmo_mpopni(wzltf, kbdfej)
hwsmo = Factor("hwsmo", [DerivedLevel("mpopni", WithinTrial(is_hwsmo_mpopni, [wzltf, kbdfej])), DerivedLevel("wicxmx", WithinTrial(is_hwsmo_wicxmx, [wzltf, kbdfej]))])
##
def is_ejihet_ylb(adasp, xkx):
    return adasp == xkx
def is_ejihet_fedzj(adasp, xkx):
    return not is_ejihet_ylb(adasp, xkx)
ejihet = Factor("ejihet", [DerivedLevel("ylb", WithinTrial(is_ejihet_ylb, [adasp, xkx])), DerivedLevel("fedzj", WithinTrial(is_ejihet_fedzj, [adasp, xkx]))])
### EXPERIMENT
constraints = [AtMostKInARow(2, adasp)]
crossing = [ejihet, kbdfej]
design=[wzltf,xkx,adasp,kbdfej,hwsmo,ejihet]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
