### REGULAR FACTORS
mhwfb = Factor("mhwfb", ["nqfkbi", "hvatw"])
xdpvuw = Factor("xdpvuw", ["xmkm", "mbz"])
jtlrt = Factor("jtlrt", ["nqfkbi", "hvatw"])
ior = Factor("ior", ["xmkm", "mbz"])
nhulxc = Factor("nhulxc", ["ffqhy", "ydycxv"])
### DERIVED FACTORS
##
def is_mps_yunbbk(xdpvuw, jtlrt):
    return xdpvuw == jtlrt
def is_mps_gpiev(xdpvuw, jtlrt):
    return not is_mps_yunbbk(xdpvuw, jtlrt)
mps = Factor("mps", [DerivedLevel("yunbbk", WithinTrial(is_mps_yunbbk, [xdpvuw, jtlrt])), DerivedLevel("gpiev", WithinTrial(is_mps_gpiev, [xdpvuw, jtlrt]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, mhwfb), MinimumTrials(26)]
crossing = [xdpvuw, mps]
design=[mhwfb,xdpvuw,jtlrt,ior,nhulxc,mps]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
