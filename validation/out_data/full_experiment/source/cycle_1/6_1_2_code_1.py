from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
dfqk = Factor("dfqk", ["psdz", "flwj"])
ptzx = Factor("ptzx", ["xhsut", "zgap"])
jyg = Factor("jyg", ["psdz", "flwj"])
gqdbe = Factor("gqdbe", ["xhsut", "zgap"])
xgijm = Factor("xgijm", ["swu", "jdvb"])
zlvm = Factor("zlvm", ["fxydov", "qqc"])
def wlyd (xgijm, zlvm):
    return xgijm == zlvm
def qsnv (xgijm, zlvm):
    return not wlyd(xgijm, zlvm)
jczjok = Factor("jczjok", [DerivedLevel("hsh", WithinTrial(wlyd, [xgijm, zlvm])), DerivedLevel("eik", WithinTrial(qsnv, [xgijm, zlvm]))])
design=[jczjok,dfqk,ptzx,jyg,gqdbe,xgijm,zlvm]
constraints=[ExactlyKInARow(3, zlvm),MinimumTrials(52)]
crossing=[xgijm,dfqk]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_1_2"))
