from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
srym = Factor("srym", ["lhdm", "iavkmi"])
qjvf = Factor("qjvf", ["nerlf", "toyjbk"])
qbbty = Factor("qbbty", ["bfkw", "wpodjm"])
dnjsfg = Factor("dnjsfg", ["ssyqhd", "prue"])
oyrqzq = Factor("oyrqzq", ["fvzixl", "piwnd"])
wjnwkf = Factor("wjnwkf", ["tccsjk", "rintt"])
gdrvz = Factor("gdrvz", ["fovkuy", "xyexzp"])
wndi = Factor("wndi", ["thujwp", "bgyy"])
omcui = Factor("omcui", ["hsey", "qywyk"])
yxhi = Factor("yxhi", ["ubjjc", "phbd"])
wnfy = Factor("wnfy", ["nadtv", "mkpzpn"])

### EXPERIMENT
design=[srym,qjvf,qbbty,dnjsfg,oyrqzq,wjnwkf,gdrvz,wndi,omcui,yxhi,wnfy]
crossing=[[srym,qjvf],[qbbty,dnjsfg,oyrqzq],[wjnwkf,gdrvz],[wndi,omcui],[yxhi],[wnfy],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2"))
### END