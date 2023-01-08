from sweetpea import *
import os
_dir=os.path.dirname(__file__)
opywr = Factor("opywr", ["swf", "buxg"])
cgp = Factor("cgp", ["bpji", "aqgjwe"])
tdabtp = Factor("tdabtp", ["cbb", "oowftv"])
ahdqgn = Factor("ahdqgn", ["wwf", "nzpo"])
ewo = Factor("ewo", ["xgjiui", "zqjua"])
qenbtx = Factor("qenbtx", ["chioj", "revq"])
constraints = []
crossing = [[opywr, cgp, tdabtp, ahdqgn, ewo], [qenbtx]]


design=[opywr,cgp,tdabtp,ahdqgn,ewo,qenbtx]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END