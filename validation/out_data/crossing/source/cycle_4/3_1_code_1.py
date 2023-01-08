from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yoqjb = Factor("yoqjb", ["gvnmel", "adigy"])
nxfdg = Factor("nxfdg", ["gdknxm", "qypoor"])
cpezj = Factor("cpezj", ["hzgs", "suc"])
idyt = Factor("idyt", ["ynbdks", "osky"])
vlfhih = Factor("vlfhih", ["yaeo", "lyarl"])
cglr = Factor("cglr", ["kzhumc", "dutq"])
mhv = Factor("mhv", ["izwus", "rzes"])
yohyq = Factor("yohyq", ["tsfohq", "dghsn"])

### EXPERIMENT
design=[yoqjb,nxfdg,cpezj,idyt,vlfhih,cglr,mhv,yohyq]
crossing=[[yoqjb,nxfdg],[cpezj,idyt,vlfhih,cglr],[mhv,yohyq],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1"))
### END