from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
kgx = Factor("kgx", ["rxrgv", "xdqhc"])
ujbe = Factor("ujbe", ["jaehg", "gmnopl"])
cbiwgn = Factor("cbiwgn", ["rxrgv", "xdqhc"])
tqlnk = Factor("tqlnk", ["jaehg", "gmnopl"])
pdhel = Factor("pdhel", ["hpziox", "wisqo"])
sfe = Factor("sfe", ["nep", "oqcus"])
def lgu (pdhel, ujbe):
    return pdhel == ujbe
def mxuj (pdhel, ujbe):
    return not lgu(pdhel, ujbe)
latl = Factor("latl", [DerivedLevel("dgcdsk", WithinTrial(lgu, [pdhel, ujbe])), DerivedLevel("zxrpht", WithinTrial(mxuj, [pdhel, ujbe]))])
design=[latl,kgx,ujbe,cbiwgn,tqlnk,pdhel,sfe]
constraints=[AtMostKInARow(2, sfe),AtLeastKInARow(2, ujbe)]
crossing=[cbiwgn,latl]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_2"))
