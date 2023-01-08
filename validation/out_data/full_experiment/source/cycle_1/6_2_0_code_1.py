from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vce = Factor("vce", ["lblh", "uer"])
nacsbx = Factor("nacsbx", ["dykns", "fhnvoo"])
nqydwt = Factor("nqydwt", ["lblh", "uer"])
nizx = Factor("nizx", ["dykns", "fhnvoo"])
qlbbhb = Factor("qlbbhb", ["grviw", "njrmn"])
mmbm = Factor("mmbm", ["fqzevn", "qstpt"])
def qfvl (nizx, mmbm):
    return nizx == mmbm
def iposdx (nizx, mmbm):
    return not qfvl(nizx, mmbm)
yayb = Factor("yayb", [DerivedLevel("uvqryf", WithinTrial(qfvl, [nizx, mmbm])), DerivedLevel("uaty", WithinTrial(iposdx, [nizx, mmbm]))])
def rgc (nqydwt, vce):
    return nqydwt == vce
def jxua (nqydwt, vce):
    return not rgc(nqydwt, vce)
wwukd = Factor("wwukd", [DerivedLevel("qrmzj", WithinTrial(rgc, [nqydwt, vce])), DerivedLevel("cvihx", WithinTrial(jxua, [nqydwt, vce]))])
design=[yayb,wwukd,vce,nacsbx,nqydwt,nizx,qlbbhb,mmbm]
constraints=[]
crossing=[nqydwt,nacsbx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_2_0"))
