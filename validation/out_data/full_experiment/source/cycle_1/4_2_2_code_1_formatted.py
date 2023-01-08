### REGULAR FACTORS
kwvw = Factor("kwvw", ["ltprq", "busur"])
vsgmy = Factor("vsgmy", ["dry", "affc"])
muv = Factor("muv", ["ltprq", "busur"])
pdajd = Factor("pdajd", ["dry", "affc"])
### DERIVED FACTORS
##
def sqrsgs (vsgmy, pdajd):
    return vsgmy == pdajd
def wol (vsgmy, pdajd):
    return not sqrsgs(vsgmy, pdajd)
rlhkr = Factor("rlhkr", [DerivedLevel("heml", WithinTrial(sqrsgs, [vsgmy, pdajd])), DerivedLevel("cepv", WithinTrial(wol, [vsgmy, pdajd]))])
##
def rpmiok (muv, kwvw):
    return muv == kwvw
def farn (muv, kwvw):
    return not rpmiok(muv, kwvw)
tkkanm = Factor("tkkanm", [DerivedLevel("qgxcm", WithinTrial(rpmiok, [muv, kwvw])), DerivedLevel("ggwik", WithinTrial(farn, [muv, kwvw]))])
### EXPERIMENT
design=[rlhkr,tkkanm,kwvw,vsgmy,muv,pdajd]
constraints=[ExactlyKInARow(2, vsgmy),AtMostKInARow(2, pdajd)]
crossing=[vsgmy,tkkanm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
