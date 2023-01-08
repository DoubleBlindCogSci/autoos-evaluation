### REGULAR FACTORS
mhwfb = Factor("mhwfb", ["nqfkbi", "hvatw"])
xdpvuw = Factor("xdpvuw", ["xmkm", "mbz"])
jtlrt = Factor("jtlrt", ["nqfkbi", "hvatw"])
ior = Factor("ior", ["xmkm", "mbz"])
nhulxc = Factor("nhulxc", ["ffqhy", "ydycxv"])
### DERIVED FACTORS
##
def brpyxa (xdpvuw, jtlrt):
    return xdpvuw == jtlrt
def lfwe (xdpvuw, jtlrt):
    return not brpyxa(xdpvuw, jtlrt)
mps = Factor("mps", [DerivedLevel("yunbbk", WithinTrial(brpyxa, [xdpvuw, jtlrt])), DerivedLevel("gpiev", WithinTrial(lfwe, [xdpvuw, jtlrt]))])
##
### EXPERIMENT
design=[mps,mhwfb,xdpvuw,jtlrt,ior,nhulxc]
constraints=[MinimumTrials(26),AtMostKInARow(4, mhwfb)]
crossing=[xdpvuw,mps]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
