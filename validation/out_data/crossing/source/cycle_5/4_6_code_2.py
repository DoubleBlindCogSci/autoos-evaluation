from sweetpea import *
import os
_dir=os.path.dirname(__file__)
dcn = Factor("dcn", ["szf", "xhcu"])
waqn = Factor("waqn", ["mcwz", "mley"])
vqoxup = Factor("vqoxup", ["zorblp", "mkigli"])
mdpk = Factor("mdpk", ["pueyki", "nqmkrm"])
iekv = Factor("iekv", ["rfkf", "gda"])
oghk = Factor("oghk", ["qfaux", "yhog"])
iiefi = Factor("iiefi", ["usztr", "olg"])
pxm = Factor("pxm", ["gupww", "egk"])
dkycj = Factor("dkycj", ["ovkguy", "qkhc"])
mwq = Factor("mwq", ["qlvmkc", "qfmitq"])
aif = Factor("aif", ["pzlitx", "ipxh"])
pus = Factor("pus", ["fdnq", "yodje"])
constraints = []
crossing = [[dcn, waqn, vqoxup, mdpk], [iekv, oghk, iiefi, pxm], [dkycj, mwq], [aif, pus]]


design=[dcn,waqn,vqoxup,mdpk,iekv,oghk,iiefi,pxm,dkycj,mwq,aif,pus]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_6"))

### END