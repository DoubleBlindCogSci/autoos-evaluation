from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vshu = Factor("vshu", ["delb", "yzyt"])
xekqc = Factor("xekqc", ["zdxu", "ydd"])
xnffn = Factor("xnffn", ["delb", "yzyt"])
dpfsnj = Factor("dpfsnj", ["zdxu", "ydd"])
tpuh = Factor("tpuh", ["dtr", "luunw"])
def vjm (dpfsnj, tpuh):
    return dpfsnj == tpuh
def inony (dpfsnj, tpuh):
    return not vjm(dpfsnj, tpuh)
uqdkg = Factor("uqdkg", [DerivedLevel("jxmnij", WithinTrial(vjm, [dpfsnj, tpuh])), DerivedLevel("hutd", WithinTrial(inony, [dpfsnj, tpuh]))])
design=[uqdkg,vshu,xekqc,xnffn,dpfsnj,tpuh]
constraints=[AtMostKInARow(4, uqdkg)]
crossing=[vshu,tpuh]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_1_1"))
