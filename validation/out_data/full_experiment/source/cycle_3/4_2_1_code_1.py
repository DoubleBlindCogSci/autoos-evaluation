from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
dcoelt = Factor("dcoelt", ["trehz", "wrla"])
wohi = Factor("wohi", ["kjz", "tnks"])
zhzxp = Factor("zhzxp", ["trehz", "wrla"])
bsp = Factor("bsp", ["kjz", "tnks"])
def rhs (dcoelt, wohi):
    return dcoelt == wohi
def zeshbx (dcoelt, wohi):
    return not rhs(dcoelt, wohi)
ryvm = Factor("ryvm", [DerivedLevel("mdvu", WithinTrial(rhs, [dcoelt, wohi])), DerivedLevel("sbgra", WithinTrial(zeshbx, [dcoelt, wohi]))])
def cin (zhzxp, bsp):
    return zhzxp == bsp
def drwqm (zhzxp, bsp):
    return not cin(zhzxp, bsp)
uzbpmj = Factor("uzbpmj", [DerivedLevel("ehyn", WithinTrial(cin, [zhzxp, bsp])), DerivedLevel("vslmq", WithinTrial(drwqm, [zhzxp, bsp]))])
design=[ryvm,uzbpmj,dcoelt,wohi,zhzxp,bsp]
constraints=[MinimumTrials(45)]
crossing=[dcoelt,zhzxp]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_1"))
