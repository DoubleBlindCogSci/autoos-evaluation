from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
kwvw = Factor("kwvw", ["ltprq", "busur"])
vsgmy = Factor("vsgmy", ["dry", "affc"])
muv = Factor("muv", ["ltprq", "busur"])
pdajd = Factor("pdajd", ["dry", "affc"])
def sqrsgs (vsgmy, pdajd):
    return vsgmy == pdajd
def wol (vsgmy, pdajd):
    return not sqrsgs(vsgmy, pdajd)
rlhkr = Factor("rlhkr", [DerivedLevel("heml", WithinTrial(sqrsgs, [vsgmy, pdajd])), DerivedLevel("cepv", WithinTrial(wol, [vsgmy, pdajd]))])
def rpmiok (muv, kwvw):
    return muv == kwvw
def farn (muv, kwvw):
    return not rpmiok(muv, kwvw)
tkkanm = Factor("tkkanm", [DerivedLevel("qgxcm", WithinTrial(rpmiok, [muv, kwvw])), DerivedLevel("ggwik", WithinTrial(farn, [muv, kwvw]))])
design=[rlhkr,tkkanm,kwvw,vsgmy,muv,pdajd]
constraints=[ExactlyKInARow(2, vsgmy),AtMostKInARow(2, pdajd)]
crossing=[vsgmy,tkkanm]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_2_2"))
