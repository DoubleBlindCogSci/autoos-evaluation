### REGULAR FACTORS
hpocc = Factor("hpocc", ["xqvh", "ppja"])
yljkz = Factor("yljkz", ["aua", "yrdzt"])
eppi = Factor("eppi", ["xqvh", "ppja"])
rkfb = Factor("rkfb", ["aua", "yrdzt"])
### DERIVED FACTORS
##
def is_bft_sxhbt(yljkz, eppi):
    return yljkz == eppi
def is_bft_bzmddf(yljkz, eppi):
    return not is_bft_sxhbt(yljkz, eppi)
bft = Factor("bft", [DerivedLevel("sxhbt", WithinTrial(is_bft_sxhbt, [yljkz, eppi])), DerivedLevel("bzmddf", WithinTrial(is_bft_bzmddf, [yljkz, eppi]))])
### EXPERIMENT
constraints = [AtLeastKInARow(4, yljkz), ExactlyKInARow(2, yljkz)]
crossing = [yljkz, bft]
design=[hpocc,yljkz,eppi,rkfb,bft]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
