from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
dfqk = Factor("dfqk", ["psdz", "flwj"])
ptzx = Factor("ptzx", ["xhsut", "zgap"])
jyg = Factor("jyg", ["psdz", "flwj"])
gqdbe = Factor("gqdbe", ["xhsut", "zgap"])
xgijm = Factor("xgijm", ["swu", "jdvb"])
zlvm = Factor("zlvm", ["fxydov", "qqc"])
def is_jczjok_hsh(xgijm, zlvm):
    return xgijm == zlvm
def is_jczjok_eik(xgijm, zlvm):
    return not is_jczjok_hsh(xgijm, zlvm)
jczjok= Factor("jczjok", [DerivedLevel("hsh", WithinTrial(is_jczjok_hsh, [xgijm, zlvm])), DerivedLevel("eik", WithinTrial(is_jczjok_eik, [xgijm, zlvm]))])
constraints = [MinimumTrials(52), ExactlyK(3, zlvm)]
crossing = [xgijm, dfqk]

design=[dfqk,ptzx,jyg,gqdbe,xgijm,zlvm]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_1_2"))
