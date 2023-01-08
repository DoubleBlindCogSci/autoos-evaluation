from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
rwbf = Factor("rwbf", ["wnxvop", "xpjtji"])
pfval = Factor("pfval", ["vxwj", "nwvr"])
tmqk = Factor("tmqk", ["wnxvop", "xpjtji"])
zay = Factor("zay", ["vxwj", "nwvr"])
axn = Factor("axn", ["ifj", "wrhjrn"])
dwra = Factor("dwra", ["nbowyy", "jxen"])
def is_wwbdfd_stfge(rwbf, tmqk):
    return rwbf == tmqk
def is_wwbdfd_gfxw(rwbf, tmqk):
    return not is_wwbdfd_stfge(rwbf, tmqk)
wwbdfd= Factor("wwbdfd", [DerivedLevel("stfge", WithinTrial(is_wwbdfd_stfge, [rwbf, tmqk])), DerivedLevel("gfxw", WithinTrial(is_wwbdfd_gfxw, [rwbf, tmqk]))])
def is_zyaxqg_oxlyic(pfval, dwra):
    return pfval == dwra
def is_zyaxqg_cmfig(pfval, dwra):
    return not is_zyaxqg_oxlyic(pfval, dwra)
zyaxqg= Factor("zyaxqg", [DerivedLevel("oxlyic", WithinTrial(is_zyaxqg_oxlyic, [pfval, dwra])), DerivedLevel("cmfig", WithinTrial(is_zyaxqg_cmfig, [pfval, dwra]))])
constraints = [AtMostKInARow(2, wwbdfd)]
crossing = [dwra, zyaxqg]

design=[rwbf,pfval,tmqk,zay,axn,dwra,wwbdfd,zyaxqg]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_1"))
