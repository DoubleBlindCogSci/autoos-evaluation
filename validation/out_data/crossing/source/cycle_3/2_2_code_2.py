from sweetpea import *
import os
_dir=os.path.dirname(__file__)
elvtnf = Factor("elvtnf", ["madd", "cubtr"])
tbsyl = Factor("tbsyl", ["pamkz", "vlwg"])
doat = Factor("doat", ["lind", "sbi"])
ttvtmr = Factor("ttvtmr", ["jooh", "qnsbxd"])
huvsjc = Factor("huvsjc", ["axung", "vik"])
constraints = []
crossing = [[elvtnf, tbsyl, doat, ttvtmr], [huvsjc]]


design=[elvtnf,tbsyl,doat,ttvtmr,huvsjc]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END