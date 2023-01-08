### REGULAR FACTORS
kwvw = Factor("kwvw", ["ltprq", "busur"])
vsgmy = Factor("vsgmy", ["dry", "affc"])
muv = Factor("muv", ["ltprq", "busur"])
pdajd = Factor("pdajd", ["dry", "affc"])
### DERIVED FACTORS
##
def is_rlhkr_heml(vsgmy, pdajd):
    return vsgmy == pdajd
def is_rlhkr_cepv(vsgmy, pdajd):
    return not is_rlhkr_heml(vsgmy, pdajd)
rlhkr= Factor("rlhkr", [DerivedLevel("heml", WithinTrial(is_rlhkr_heml, [vsgmy, pdajd])), DerivedLevel("cepv", WithinTrial(is_rlhkr_cepv, [vsgmy, pdajd]))])
##
def is_tkkanm_qgxcm(muv, kwvw):
    return muv == kwvw
def is_tkkanm_ggwik(muv, kwvw):
    return not is_tkkanm_qgxcm(muv, kwvw)
tkkanm= Factor("tkkanm", [DerivedLevel("qgxcm", WithinTrial(is_tkkanm_qgxcm, [muv, kwvw])), DerivedLevel("ggwik", WithinTrial(is_tkkanm_ggwik, [muv, kwvw]))])
### EXPERIMENT
constraints = [ExactlyKInARow(2, (vsgmy, "dry")), AtMostKInARow(2, (pdajd, "affc"))]
crossing = [vsgmy, tkkanm]
design=[kwvw,vsgmy,muv,pdajd,rlhkr,tkkanm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
