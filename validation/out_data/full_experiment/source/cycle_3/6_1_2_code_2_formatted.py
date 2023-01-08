### REGULAR FACTORS
kgx = Factor("kgx", ["rxrgv", "xdqhc"])
ujbe = Factor("ujbe", ["jaehg", "gmnopl"])
cbiwgn = Factor("cbiwgn", ["rxrgv", "xdqhc"])
tqlnk = Factor("tqlnk", ["jaehg", "gmnopl"])
pdhel = Factor("pdhel", ["hpziox", "wisqo"])
sfe = Factor("sfe", ["nep", "oqcus"])
### DERIVED FACTORS
##
def is_latl_dgcdsk(pdhel, ujbe):
    return pdhel == ujbe
def is_latl_zxrpht(pdhel, ujbe):
    return not is_latl_dgcdsk(pdhel, ujbe)
latl = Factor("latl", [DerivedLevel("dgcdsk", WithinTrial(is_latl_dgcdsk, [pdhel, ujbe])), DerivedLevel("zxrpht", WithinTrial(is_latl_zxrpht, [pdhel, ujbe]))])
### EXPERIMENT
constraints = [AtMostKInARow(2, sfe), AtLeastKInARow(2, ujbe)]
crossing = [cbiwgn, latl]
design=[kgx,ujbe,cbiwgn,tqlnk,pdhel,sfe,latl]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
