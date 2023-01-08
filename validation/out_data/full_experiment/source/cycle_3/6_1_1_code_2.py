from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
opstb = Factor("opstb", ["gizmm", "oaxg"])
hehx = Factor("hehx", ["ewbu", "vai"])
bob = Factor("bob", ["gizmm", "oaxg"])
pdwuqf = Factor("pdwuqf", ["ewbu", "vai"])
pyxfb = Factor("pyxfb", ["cohge", "tdm"])
iwhnba = Factor("iwhnba", ["vehu", "xmcl"])
def is_niyyi_ieeoy(bob, pdwuqf):
    return bob == pdwuqf
def is_niyyi_wywxab(bob, pdwuqf):
    return not is_niyyi_ieeoy(bob, pdwuqf)
niyyi = Factor("niyyi", [DerivedLevel("ieeoy", WithinTrial(is_niyyi_ieeoy, [bob, pdwuqf])), DerivedLevel("wywxab", WithinTrial(is_niyyi_wywxab, [bob, pdwuqf]))])
constraints = [AtLeastKInARow(4, (opstb, "gizmm"))]
crossing = [hehx, pyxfb]

design=[opstb,hehx,bob,pdwuqf,pyxfb,iwhnba,niyyi]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_1"))
