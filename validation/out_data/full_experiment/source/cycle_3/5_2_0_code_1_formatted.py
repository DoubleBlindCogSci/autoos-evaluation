### REGULAR FACTORS
byds = Factor("byds", ["wnsa", "pbvws"])
zqhjpa = Factor("zqhjpa", ["auo", "ikosc"])
ppktzu = Factor("ppktzu", ["wnsa", "pbvws"])
bwci = Factor("bwci", ["auo", "ikosc"])
rxukub = Factor("rxukub", ["txxm", "yojoxb"])
### DERIVED FACTORS
##
def wzo (bwci, rxukub):
    return bwci == rxukub
def qgra (bwci, rxukub):
    return not wzo(bwci, rxukub)
cznezw = Factor("cznezw", [DerivedLevel("fzjgi", WithinTrial(wzo, [bwci, rxukub])), DerivedLevel("qpqg", WithinTrial(qgra, [bwci, rxukub]))])
##
def rbusy (byds, zqhjpa):
    return byds == zqhjpa
def zuzbhe (byds, zqhjpa):
    return not rbusy(byds, zqhjpa)
gabz = Factor("gabz", [DerivedLevel("grwuc", WithinTrial(rbusy, [byds, zqhjpa])), DerivedLevel("tysmu", WithinTrial(zuzbhe, [byds, zqhjpa]))])
### EXPERIMENT
design=[cznezw,gabz,byds,zqhjpa,ppktzu,bwci,rxukub]
constraints=[]
crossing=[byds,ppktzu]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
