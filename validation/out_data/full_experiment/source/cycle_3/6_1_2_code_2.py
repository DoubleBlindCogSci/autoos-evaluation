from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
kgx = Factor("kgx", ["rxrgv", "xdqhc"])
ujbe = Factor("ujbe", ["jaehg", "gmnopl"])
cbiwgn = Factor("cbiwgn", ["rxrgv", "xdqhc"])
tqlnk = Factor("tqlnk", ["jaehg", "gmnopl"])
pdhel = Factor("pdhel", ["hpziox", "wisqo"])
sfe = Factor("sfe", ["nep", "oqcus"])
def is_latl_dgcdsk(pdhel, ujbe):
    return pdhel == ujbe
def is_latl_zxrpht(pdhel, ujbe):
    return not is_latl_dgcdsk(pdhel, ujbe)
latl = Factor("latl", [DerivedLevel("dgcdsk", WithinTrial(is_latl_dgcdsk, [pdhel, ujbe])), DerivedLevel("zxrpht", WithinTrial(is_latl_zxrpht, [pdhel, ujbe]))])
constraints = [AtMostKInARow(2, sfe), AtLeastKInARow(2, ujbe)]
crossing = [cbiwgn, latl]

design=[kgx,ujbe,cbiwgn,tqlnk,pdhel,sfe,latl]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_2"))
