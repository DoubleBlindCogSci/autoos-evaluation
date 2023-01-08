from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
opstb = Factor("opstb", ["gizmm", "oaxg"])
hehx = Factor("hehx", ["ewbu", "vai"])
bob = Factor("bob", ["gizmm", "oaxg"])
pdwuqf = Factor("pdwuqf", ["ewbu", "vai"])
pyxfb = Factor("pyxfb", ["cohge", "tdm"])
iwhnba = Factor("iwhnba", ["vehu", "xmcl"])
def cghug (bob, pdwuqf):
    return bob == pdwuqf
def zdxjg (bob, pdwuqf):
    return not cghug(bob, pdwuqf)
niyyi = Factor("niyyi", [DerivedLevel("ieeoy", WithinTrial(cghug, [bob, pdwuqf])), DerivedLevel("wywxab", WithinTrial(zdxjg, [bob, pdwuqf]))])
design=[niyyi,opstb,hehx,bob,pdwuqf,pyxfb,iwhnba]
constraints=[AtLeastKInARow(4, opstb)]
crossing=[hehx,pyxfb]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_1"))
