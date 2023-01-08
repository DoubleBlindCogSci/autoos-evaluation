### REGULAR FACTORS
gqw = Factor("gqw", ["ohpe", "rbclng"])
wdp = Factor("wdp", ["eioqw", "rrvin"])
nrbavq = Factor("nrbavq", ["ohpe", "rbclng"])
xlpll = Factor("xlpll", ["eioqw", "rrvin"])
xne = Factor("xne", ["erjk", "yow"])
cee = Factor("cee", ["yqzavs", "gof"])
### DERIVED FACTORS
##
def rofz(nrbavq, wdp):
    return nrbavq == wdp
def yfsv(nrbavq, wdp):
    return not rofz(nrbavq, wdp)
zzsf = Factor("zzsf", [
    DerivedLevel("cmjwd", WithinTrial(rofz, [nrbavq, wdp])),
    DerivedLevel("yffeb", WithinTrial(yfsv, [nrbavq, wdp]))
])
### EXPERIMENT
design=[zzsf,gqw,wdp,nrbavq,xlpll,xne,cee]
constraints=[MinimumTrials(39)]
crossing=[nrbavq,cee]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
