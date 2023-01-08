### REGULAR FACTORS
uwlh = Factor("uwlh", ["hhs", "ptiktj"])
uza = Factor("uza", ["uiq", "tmxav"])
bog = Factor("bog", ["hhs", "ptiktj"])
boh = Factor("boh", ["uiq", "tmxav"])
### DERIVED FACTORS
##
def sgnyq (uwlh, boh):
    return uwlh == boh
def rqq (uwlh, boh):
    return not sgnyq(uwlh, boh)
znx = Factor("znx", [DerivedLevel("yjafe", WithinTrial(sgnyq, [uwlh, boh])), DerivedLevel("kndf", WithinTrial(rqq, [uwlh, boh]))])
##
def rmxdxd (uza, bog):
    return uza == bog
def bkeh (uza, bog):
    return not rmxdxd(uza, bog)
dupc = Factor("dupc", [DerivedLevel("duyj", WithinTrial(rmxdxd, [uza, bog])), DerivedLevel("ffiokh", WithinTrial(bkeh, [uza, bog]))])
### EXPERIMENT
design=[znx,dupc,uwlh,uza,bog,boh]
constraints=[AtLeastKInARow(3, znx),ExactlyKInARow(3, boh)]
crossing=[bog,uza]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
