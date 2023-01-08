### REGULAR FACTORS
kqslu = Factor("kqslu", ["famp", "cmff"])
kjt = Factor("kjt", ["uhoqoh", "aazgln"])
trysn = Factor("trysn", ["famp", "cmff"])
dbp = Factor("dbp", ["uhoqoh", "aazgln"])
miayr = Factor("miayr", ["rfddz", "tth"])
hdrgrk = Factor("hdrgrk", ["wbesla", "kknw"])
### DERIVED FACTORS
##
def zkjbd (kjt, dbp):
    return kjt == dbp
def bsycn (kjt, dbp):
    return not zkjbd(kjt, dbp)
xdaerc = Factor("xdaerc", [DerivedLevel("ddfx", WithinTrial(zkjbd, [kjt, dbp])), DerivedLevel("retip", WithinTrial(bsycn, [kjt, dbp]))])
##
### EXPERIMENT
design=[xdaerc,kqslu,kjt,trysn,dbp,miayr,hdrgrk]
constraints=[AtLeastKInARow(4, dbp)]
crossing=[kjt,xdaerc]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
