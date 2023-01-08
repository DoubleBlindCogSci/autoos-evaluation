from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
mrgf = Factor("mrgf", ["fsvan", "nie"])
icswhs = Factor("icswhs", ["llcpvl", "wchnv"])
xrzgp = Factor("xrzgp", ["fsvan", "nie"])
imlvth = Factor("imlvth", ["llcpvl", "wchnv"])
nrf = Factor("nrf", ["rlwwkc", "qoakhq"])
def hrw (mrgf, xrzgp):
    return mrgf == xrzgp
def hqty (mrgf, xrzgp):
    return not hrw(mrgf, xrzgp)
obg = Factor("obg", [DerivedLevel("gpqi", WithinTrial(hrw, [mrgf, xrzgp])), DerivedLevel("kfpob", WithinTrial(hqty, [mrgf, xrzgp]))])
def hnhm (nrf, imlvth):
    return nrf == imlvth
def tyfmtz (nrf, imlvth):
    return not hnhm(nrf, imlvth)
jvks = Factor("jvks", [DerivedLevel("fhdlv", WithinTrial(hnhm, [nrf, imlvth])), DerivedLevel("gwvvx", WithinTrial(tyfmtz, [nrf, imlvth]))])
design=[obg,jvks,mrgf,icswhs,xrzgp,imlvth,nrf]
constraints=[]
crossing=[jvks,obg]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_0"))
