### REGULAR FACTORS
mrgf = Factor("mrgf", ["fsvan", "nie"])
icswhs = Factor("icswhs", ["llcpvl", "wchnv"])
xrzgp = Factor("xrzgp", ["fsvan", "nie"])
imlvth = Factor("imlvth", ["llcpvl", "wchnv"])
nrf = Factor("nrf", ["rlwwkc", "qoakhq"])
### DERIVED FACTORS
##
def hrw (mrgf, xrzgp):
    return mrgf == xrzgp
def hqty (mrgf, xrzgp):
    return not hrw(mrgf, xrzgp)
obg = Factor("obg", [DerivedLevel("gpqi", WithinTrial(hrw, [mrgf, xrzgp])), DerivedLevel("kfpob", WithinTrial(hqty, [mrgf, xrzgp]))])
##
def hnhm (nrf, imlvth):
    return nrf == imlvth
def tyfmtz (nrf, imlvth):
    return not hnhm(nrf, imlvth)
jvks = Factor("jvks", [DerivedLevel("fhdlv", WithinTrial(hnhm, [nrf, imlvth])), DerivedLevel("gwvvx", WithinTrial(tyfmtz, [nrf, imlvth]))])
### EXPERIMENT
design=[obg,jvks,mrgf,icswhs,xrzgp,imlvth,nrf]
constraints=[]
crossing=[jvks,obg]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
