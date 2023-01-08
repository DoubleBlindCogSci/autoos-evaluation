from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
mrgf = Factor("mrgf", ["fsvan", "nie"])
icswhs = Factor("icswhs", ["llcpvl", "wchnv"])
xrzgp = Factor("xrzgp", ["fsvan", "nie"])
imlvth = Factor("imlvth", ["llcpvl", "wchnv"])
nrf = Factor("nrf", ["rlwwkc", "qoakhq"])
def is_obg_gpqi(mrgf, xrzgp):
    return mrgf == xrzgp
def is_obg_kfpob(mrgf, xrzgp):
    return not is_obg_gpqi(mrgf, xrzgp)
obg = Factor("obg", [DerivedLevel("gpqi", WithinTrial(is_obg_gpqi, [mrgf, xrzgp])), DerivedLevel("kfpob", WithinTrial(is_obg_kfpob, [mrgf, xrzgp]))])
def is_jvks_fhdlv(nrf, imlvth):
    return nrf == imlvth
def is_jvks_gwvvx(nrf, imlvth):
    return not is_jvks_fhdlv(nrf, imlvth)
jvks = Factor("jvks", [DerivedLevel("fhdlv", WithinTrial(is_jvks_fhdlv, [nrf, imlvth])), DerivedLevel("gwvvx", WithinTrial(is_jvks_gwvvx, [nrf, imlvth]))])
constraints = []
crossing = [jvks, obg]

design=[mrgf,icswhs,xrzgp,imlvth,nrf,obg,jvks]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_0"))
