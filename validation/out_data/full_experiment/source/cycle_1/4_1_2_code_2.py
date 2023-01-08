from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
lno = Factor("lno", ["sudp", "nogr"])
tula = Factor("tula", ["bkcad", "cjm"])
ygadz = Factor("ygadz", ["sudp", "nogr"])
qxlh = Factor("qxlh", ["bkcad", "cjm"])
def is_xkx_ezcq(tula, lno):
    return tula == lno
def is_xkx_wgybo(tula, lno):
    return not is_xkx_ezcq(tula, lno)
xkx = Factor("xkx", [DerivedLevel("ezcq", WithinTrial(is_xkx_ezcq, [tula, lno])), DerivedLevel("wgybo", WithinTrial(is_xkx_wgybo, [tula, lno]))])
constraints = [AtLeastKInARow(3, (tula, "bkcad")), MinimumTrials(28)]
crossing = [qxlh, xkx]

design=[lno,tula,ygadz,qxlh,xkx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_1_2"))
