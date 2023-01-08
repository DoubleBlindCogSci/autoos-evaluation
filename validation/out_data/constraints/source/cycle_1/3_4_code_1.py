from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
azeeg = Factor("azeeg", ["vitp", "zqn"])
efwt = Factor("efwt", ["iof", "nmmcqx"])
qepeev = Factor("qepeev", ["jpbg","wshfv","dmey", "ytsq"])
nuly = Factor("nuly", ["yrv","izg", "qoq"])
mehu = Factor("mehu", ["knauow","qmsjfv", "euq"])
lpbgp = Factor("lpbgp", ["ruufar","epcf","upiuv", "tqffgv"])

### EXPERIMENT
constraints=[Exclude((azeeg,"zqn")),AtLeastKInARow(3,(efwt,"nmmcqx")),MinimumTrials(46)]
design=[azeeg,efwt,qepeev,nuly,mehu,lpbgp]
crossing=[nuly,mehu,lpbgp]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_4"))
### END