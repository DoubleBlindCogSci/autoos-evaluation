from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
kfb = Factor("kfb", ["fvdwcy", "isd"])
awwzy = Factor("awwzy", ["haqh", "nunh"])
moeh = Factor("moeh", ["fvdwcy", "isd"])
hfwn = Factor("hfwn", ["haqh", "nunh"])
def is_bvdn_evws(hfwn, awwzy):
    return hfwn == awwzy
def is_bvdn_illqj(hfwn, awwzy):
    return not is_bvdn_evws(hfwn, awwzy)
bvdn = Factor("bvdn", [DerivedLevel("evws", WithinTrial(is_bvdn_evws, [hfwn, awwzy])), DerivedLevel("illqj", WithinTrial(is_bvdn_illqj, [hfwn, awwzy]))])
constraints = []
crossing = [kfb, awwzy]

design=[kfb,awwzy,moeh,hfwn,bvdn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_0"))
