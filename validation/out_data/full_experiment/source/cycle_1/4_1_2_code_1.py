from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
lno = Factor("lno", ["sudp", "nogr"])
tula = Factor("tula", ["bkcad", "cjm"])
ygadz = Factor("ygadz", ["sudp", "nogr"])
qxlh = Factor("qxlh", ["bkcad", "cjm"])
def dcbt (tula, lno):
    return tula == lno
def ygvz (tula, lno):
    return not dcbt(tula, lno)
xkx = Factor("xkx", [DerivedLevel("ezcq", WithinTrial(dcbt, [tula, lno])), DerivedLevel("wgybo", WithinTrial(ygvz, [tula, lno]))])
design=[xkx,lno,tula,ygadz,qxlh]
constraints=[MinimumTrials(28),AtLeastKInARow(3, tula)]
crossing=[qxlh,xkx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_1_2"))
