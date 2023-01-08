from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
dcoelt = Factor("dcoelt", ["trehz", "wrla"])
wohi = Factor("wohi", ["kjz", "tnks"])
zhzxp = Factor("zhzxp", ["trehz", "wrla"])
bsp = Factor("bsp", ["kjz", "tnks"])
def is_ryvm_mdvu(dcoelt, wohi):
    return dcoelt == wohi
def is_ryvm_sbgra(dcoelt, wohi):
    return not is_ryvm_mdvu(dcoelt, wohi)
ryvm = Factor("ryvm", [DerivedLevel("mdvu", WithinTrial(is_ryvm_mdvu, [dcoelt, wohi])), DerivedLevel("sbgra", WithinTrial(is_ryvm_sbgra, [dcoelt, wohi]))])
def is_uzbpmj_ehyn(zhzxp, bsp):
    return zhzxp == bsp
def is_uzbpmj_vslmq(zhzxp, bsp):
    return not is_uzbpmj_ehyn(zhzxp, bsp)
uzbpmj = Factor("uzbpmj", [DerivedLevel("ehyn", WithinTrial(is_uzbpmj_ehyn, [zhzxp, bsp])), DerivedLevel("vslmq", WithinTrial(is_uzbpmj_vslmq, [zhzxp, bsp]))])
constraints = [MinimumTrials(45)]
crossing = [dcoelt, zhzxp]

design=[dcoelt,wohi,zhzxp,bsp,ryvm,uzbpmj]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_1"))
