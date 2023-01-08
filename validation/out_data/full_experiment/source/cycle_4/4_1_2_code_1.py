from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
hpocc = Factor("hpocc", ["xqvh", "ppja"])
yljkz = Factor("yljkz", ["aua", "yrdzt"])
eppi = Factor("eppi", ["xqvh", "ppja"])
rkfb = Factor("rkfb", ["aua", "yrdzt"])
def wgh (yljkz, eppi):
    return yljkz == eppi
def lgdqp (yljkz, eppi):
    return not wgh(yljkz, eppi)
bft = Factor("bft", [DerivedLevel("sxhbt", WithinTrial(wgh, [yljkz, eppi])), DerivedLevel("bzmddf", WithinTrial(lgdqp, [yljkz, eppi]))])
design=[bft,hpocc,yljkz,eppi,rkfb]
constraints=[AtLeastKInARow(4, yljkz),ExactlyKInARow(2, yljkz)]
crossing=[yljkz,bft]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_2"))
