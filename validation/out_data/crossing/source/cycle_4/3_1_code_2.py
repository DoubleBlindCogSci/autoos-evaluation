from sweetpea import *
import os
_dir=os.path.dirname(__file__)
yoqjb = Factor("yoqjb", ["gvnmel", "adigy"])
nxfdg = Factor("nxfdg", ["gdknxm", "qypoor"])
cpezj = Factor("cpezj", ["hzgs", "suc"])
idyt = Factor("idyt", ["ynbdks", "osky"])
vlfhih = Factor("vlfhih", ["yaeo", "lyarl"])
cglr = Factor("cglr", ["kzhumc", "dutq"])
mhv = Factor("mhv", ["izwus", "rzes"])
yohyq = Factor("yohyq", ["tsfohq", "dghsn"])
constraints = []
crossing = [[yoqjb, nxfdg], [cpezj, idyt, vlfhih, cglr], [mhv, yohyq]]


design=[yoqjb,nxfdg,cpezj,idyt,vlfhih,cglr,mhv,yohyq]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END