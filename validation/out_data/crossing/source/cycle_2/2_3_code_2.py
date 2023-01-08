from sweetpea import *
import os
_dir=os.path.dirname(__file__)
tviioo = Factor("tviioo", ["nvcdsd", "qhscon"])
jur = Factor("jur", ["zuzw", "jvgu"])
ptv = Factor("ptv", ["bkk", "pihi"])
xib = Factor("xib", ["nta", "ifxes"])
zxrd = Factor("zxrd", ["thqgwf", "noj"])
imte = Factor("imte", ["uaj", "mvtkat"])
srhgs = Factor("srhgs", ["ftsmsq", "hjwij"])
constraints = []
crossing = [[tviioo, jur, ptv], [xib, zxrd, imte, srhgs]]


design=[tviioo,jur,ptv,xib,zxrd,imte,srhgs]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3"))

### END