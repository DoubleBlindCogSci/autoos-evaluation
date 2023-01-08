from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
dodd = Factor("dodd", ["lfk", "qsy"])
vodhe = Factor("vodhe", ["tkttub", "rfctx"])
fnv = Factor("fnv", ["lfk", "qsy"])
fiw = Factor("fiw", ["tkttub", "rfctx"])
def kcv (dodd, fiw):
    return dodd == fiw
def ork (dodd, fiw):
    return not kcv(dodd, fiw)
dvx = Factor("dvx", [DerivedLevel("ylij", WithinTrial(kcv, [dodd, fiw])), DerivedLevel("gya", WithinTrial(ork, [dodd, fiw]))])
design=[dvx,dodd,vodhe,fnv,fiw]
constraints=[AtMostKInARow(4, dodd)]
crossing=[fiw,dodd]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_1"))
