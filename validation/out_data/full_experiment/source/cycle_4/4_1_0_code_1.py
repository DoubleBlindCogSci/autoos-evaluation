from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
kfb = Factor("kfb", ["fvdwcy", "isd"])
awwzy = Factor("awwzy", ["haqh", "nunh"])
moeh = Factor("moeh", ["fvdwcy", "isd"])
hfwn = Factor("hfwn", ["haqh", "nunh"])
def fwmm (hfwn, awwzy):
    return hfwn == awwzy
def lcnpn (hfwn, awwzy):
    return not fwmm(hfwn, awwzy)
bvdn = Factor("bvdn", [DerivedLevel("evws", WithinTrial(fwmm, [hfwn, awwzy])), DerivedLevel("illqj", WithinTrial(lcnpn, [hfwn, awwzy]))])
design=[bvdn,kfb,awwzy,moeh,hfwn]
constraints=[]
crossing=[kfb,awwzy]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_0"))
