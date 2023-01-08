### REGULAR FACTORS
vipu = Factor("vipu", ["nqaj", "fftz"])
pfl = Factor("pfl", ["vyo", "xkgy"])
nshhcw = Factor("nshhcw", ["nqaj", "fftz"])
bwmn = Factor("bwmn", ["vyo", "xkgy"])
### DERIVED FACTORS
##
def is_yic_guxkbh(bwmn, nshhcw):
    return bwmn == nshhcw
def is_yic_wekqv(bwmn, nshhcw):
    return not is_yic_guxkbh(bwmn, nshhcw)
yic = Factor("yic", [DerivedLevel("guxkbh", WithinTrial(is_yic_guxkbh, [bwmn, nshhcw])), DerivedLevel("wekqv", WithinTrial(is_yic_wekqv, [bwmn, nshhcw]))])
##
def is_sxt_pzruw(pfl, vipu):
    return pfl == vipu
def is_sxt_mcsdum(pfl, vipu):
    return not is_sxt_pzruw(pfl, vipu)
sxt = Factor("sxt", [DerivedLevel("pzruw", WithinTrial(is_sxt_pzruw, [pfl, vipu])), DerivedLevel("mcsdum", WithinTrial(is_sxt_mcsdum, [pfl, vipu]))])
### EXPERIMENT
constraints = []
crossing = [pfl, bwmn]
design=[vipu,pfl,nshhcw,bwmn,yic,sxt]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
