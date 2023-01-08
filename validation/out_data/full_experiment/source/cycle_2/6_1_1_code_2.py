from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
kqslu = Factor("kqslu", ["famp", "cmff"])
kjt = Factor("kjt", ["uhoqoh", "aazgln"])
trysn = Factor("trysn", ["famp", "cmff"])
dbp = Factor("dbp", ["uhoqoh", "aazgln"])
miayr = Factor("miayr", ["rfddz", "tth"])
hdrgrk = Factor("hdrgrk", ["wbesla", "kknw"])
def is_xdaerc_ddfx(kjt, dbp):
    return kjt == dbp
def is_xdaerc_retip(kjt, dbp):
    return not is_xdaerc_ddfx(kjt, dbp)
xdaerc= Factor("xdaerc", [DerivedLevel("ddfx", WithinTrial(is_xdaerc_ddfx, [kjt, dbp])), DerivedLevel("retip", WithinTrial(is_xdaerc_retip, [kjt, dbp]))])
constraints = [AtLeastKInARow(4, (dbp, "uhoqoh"))]
crossing = [kjt, xdaerc]

design=[kqslu,kjt,trysn,dbp,miayr,hdrgrk,xdaerc]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_1"))
