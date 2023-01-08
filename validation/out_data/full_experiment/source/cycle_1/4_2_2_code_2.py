from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
kwvw = Factor("kwvw", ["ltprq", "busur"])
vsgmy = Factor("vsgmy", ["dry", "affc"])
muv = Factor("muv", ["ltprq", "busur"])
pdajd = Factor("pdajd", ["dry", "affc"])
def is_rlhkr_heml(vsgmy, pdajd):
    return vsgmy == pdajd
def is_rlhkr_cepv(vsgmy, pdajd):
    return not is_rlhkr_heml(vsgmy, pdajd)
rlhkr= Factor("rlhkr", [DerivedLevel("heml", WithinTrial(is_rlhkr_heml, [vsgmy, pdajd])), DerivedLevel("cepv", WithinTrial(is_rlhkr_cepv, [vsgmy, pdajd]))])
def is_tkkanm_qgxcm(muv, kwvw):
    return muv == kwvw
def is_tkkanm_ggwik(muv, kwvw):
    return not is_tkkanm_qgxcm(muv, kwvw)
tkkanm= Factor("tkkanm", [DerivedLevel("qgxcm", WithinTrial(is_tkkanm_qgxcm, [muv, kwvw])), DerivedLevel("ggwik", WithinTrial(is_tkkanm_ggwik, [muv, kwvw]))])
constraints = [ExactlyKInARow(2, (vsgmy, "dry")), AtMostKInARow(2, (pdajd, "affc"))]
crossing = [vsgmy, tkkanm]

design=[kwvw,vsgmy,muv,pdajd,rlhkr,tkkanm]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_2_2"))
