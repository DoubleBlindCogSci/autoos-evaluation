from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oqq = Factor("oqq", ["cvyjvv", "peeo"])
stvcsi = Factor("stvcsi", ["ucuap", "nas"])
uckevd = Factor("uckevd", ["mgnzg", "gdmmwm"])
hkf = Factor("hkf", ["hxpkb", "unuyg"])
xbb = Factor("xbb", ["fgzvwg", "rbbzyq"])
txbmgq = Factor("txbmgq", ["bvhsmo", "qmlnqq"])
bnarjw = Factor("bnarjw", ["sumro", "rncyug"])

### EXPERIMENT
design=[oqq,stvcsi,uckevd,hkf,xbb,txbmgq,bnarjw]
crossing=[[oqq,stvcsi,uckevd],[hkf,xbb],[txbmgq,bnarjw]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END