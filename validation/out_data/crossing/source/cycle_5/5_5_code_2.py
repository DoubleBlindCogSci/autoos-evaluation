from sweetpea import *
import os
_dir=os.path.dirname(__file__)
fchlax = Factor("fchlax", ["rrxgg", "vej"])
tyk = Factor("tyk", ["zulume", "fqhh"])
sdtf = Factor("sdtf", ["uej", "mmhiio"])
ues = Factor("ues", ["uols", "tiy"])
mgw = Factor("mgw", ["ubr", "dta"])
pbbno = Factor("pbbno", ["qdiqdy", "jsm"])
ruwiv = Factor("ruwiv", ["cxrs", "icb"])
khq = Factor("khq", ["uce", "wwi"])
unx = Factor("unx", ["rajj", "rvmuo"])
lkcp = Factor("lkcp", ["ptdk", "dnttu"])
zylbl = Factor("zylbl", ["tkpms", "xllmgx"])
hehd = Factor("hehd", ["kml", "ysefia"])
jrqn = Factor("jrqn", ["zjxlt", "bule"])
constraints = []
crossing = [[fchlax, tyk, sdtf, ues, mgw], [pbbno, ruwiv], [khq, unx, lkcp], [zylbl, hehd, jrqn]]


design=[fchlax,tyk,sdtf,ues,mgw,pbbno,ruwiv,khq,unx,lkcp,zylbl,hehd,jrqn]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_5"))

### END