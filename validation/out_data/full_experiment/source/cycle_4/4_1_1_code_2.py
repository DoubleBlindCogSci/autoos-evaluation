from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
dodd = Factor("dodd", ["lfk", "qsy"])
vodhe = Factor("vodhe", ["tkttub", "rfctx"])
fnv = Factor("fnv", ["lfk", "qsy"])
fiw = Factor("fiw", ["tkttub", "rfctx"])
def is_dvx_ylij(dodd, fiw):
    return dodd == fiw
def is_dvx_gya(dodd, fiw):
    return not is_dvx_ylij(dodd, fiw)
dvx = Factor("dvx", [DerivedLevel("ylij", WithinTrial(is_dvx_ylij, [dodd, fiw])), DerivedLevel("gya", WithinTrial(is_dvx_gya, [dodd, fiw]))])
constraints = [AtMostKInARow(4, dodd)]
crossing = [fiw, dodd]

design=[dodd,vodhe,fnv,fiw,dvx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_1"))
