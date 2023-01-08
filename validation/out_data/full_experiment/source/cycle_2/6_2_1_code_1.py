from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
rwbf = Factor("rwbf", ["wnxvop", "xpjtji"])
pfval = Factor("pfval", ["vxwj", "nwvr"])
tmqk = Factor("tmqk", ["wnxvop", "xpjtji"])
zay = Factor("zay", ["vxwj", "nwvr"])
axn = Factor("axn", ["ifj", "wrhjrn"])
dwra = Factor("dwra", ["nbowyy", "jxen"])
def gmjvnf (rwbf, tmqk):
    return rwbf == tmqk
def eegjyq (rwbf, tmqk):
    return not gmjvnf(rwbf, tmqk)
wwbdfd = Factor("wwbdfd", [DerivedLevel("stfge", WithinTrial(gmjvnf, [rwbf, tmqk])), DerivedLevel("gfxw", WithinTrial(eegjyq, [rwbf, tmqk]))])
def mwbtm (pfval, dwra):
    return pfval == dwra
def tgdade (pfval, dwra):
    return not mwbtm(pfval, dwra)
zyaxqg = Factor("zyaxqg", [DerivedLevel("oxlyic", WithinTrial(mwbtm, [pfval, dwra])), DerivedLevel("cmfig", WithinTrial(tgdade, [pfval, dwra]))])
design=[wwbdfd,zyaxqg,rwbf,pfval,tmqk,zay,axn,dwra]
constraints=[AtMostKInARow(2, wwbdfd)]
crossing=[dwra,zyaxqg]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_1"))
