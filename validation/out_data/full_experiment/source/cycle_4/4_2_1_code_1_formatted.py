### REGULAR FACTORS
wzltf = Factor("wzltf", ["wkh", "jfimzl"])
xkx = Factor("xkx", ["xdmxg", "yrlgcb"])
adasp = Factor("adasp", ["wkh", "jfimzl"])
kbdfej = Factor("kbdfej", ["xdmxg", "yrlgcb"])
### DERIVED FACTORS
##
def ama (wzltf, kbdfej):
    return wzltf == kbdfej
def bqnj (wzltf, kbdfej):
    return not ama(wzltf, kbdfej)
hwsmo = Factor("hwsmo", [DerivedLevel("mpopni", WithinTrial(ama, [wzltf, kbdfej])), DerivedLevel("wicxmx", WithinTrial(bqnj, [wzltf, kbdfej]))])
##
def zixeqd (adasp, xkx):
    return adasp == xkx
def mssjx (adasp, xkx):
    return not zixeqd(adasp, xkx)
ejihet = Factor("ejihet", [DerivedLevel("ylb", WithinTrial(zixeqd, [adasp, xkx])), DerivedLevel("fedzj", WithinTrial(mssjx, [adasp, xkx]))])
### EXPERIMENT
design=[hwsmo,ejihet,wzltf,xkx,adasp,kbdfej]
constraints=[AtMostKInARow(2, adasp)]
crossing=[ejihet,kbdfej]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
