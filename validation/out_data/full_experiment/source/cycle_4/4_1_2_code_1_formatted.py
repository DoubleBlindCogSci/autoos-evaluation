### REGULAR FACTORS
hpocc = Factor("hpocc", ["xqvh", "ppja"])
yljkz = Factor("yljkz", ["aua", "yrdzt"])
eppi = Factor("eppi", ["xqvh", "ppja"])
rkfb = Factor("rkfb", ["aua", "yrdzt"])
### DERIVED FACTORS
##
def wgh (yljkz, eppi):
    return yljkz == eppi
def lgdqp (yljkz, eppi):
    return not wgh(yljkz, eppi)
bft = Factor("bft", [DerivedLevel("sxhbt", WithinTrial(wgh, [yljkz, eppi])), DerivedLevel("bzmddf", WithinTrial(lgdqp, [yljkz, eppi]))])
##
### EXPERIMENT
design=[bft,hpocc,yljkz,eppi,rkfb]
constraints=[AtLeastKInARow(4, yljkz),ExactlyKInARow(2, yljkz)]
crossing=[yljkz,bft]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
