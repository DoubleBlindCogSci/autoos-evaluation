### REGULAR FACTORS
kqslu = Factor("kqslu", ["famp", "cmff"])
kjt = Factor("kjt", ["uhoqoh", "aazgln"])
trysn = Factor("trysn", ["famp", "cmff"])
dbp = Factor("dbp", ["uhoqoh", "aazgln"])
miayr = Factor("miayr", ["rfddz", "tth"])
hdrgrk = Factor("hdrgrk", ["wbesla", "kknw"])
### DERIVED FACTORS
##
def is_xdaerc_ddfx(kjt, dbp):
    return kjt == dbp
def is_xdaerc_retip(kjt, dbp):
    return not is_xdaerc_ddfx(kjt, dbp)
xdaerc= Factor("xdaerc", [DerivedLevel("ddfx", WithinTrial(is_xdaerc_ddfx, [kjt, dbp])), DerivedLevel("retip", WithinTrial(is_xdaerc_retip, [kjt, dbp]))])
### EXPERIMENT
constraints = [AtLeastKInARow(4, (dbp, "uhoqoh"))]
crossing = [kjt, xdaerc]
design=[kqslu,kjt,trysn,dbp,miayr,hdrgrk]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
