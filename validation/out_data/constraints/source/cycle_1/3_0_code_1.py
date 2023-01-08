from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jxtk = Factor("jxtk", ["kdu","uimlpi", "jqdtud"])
baiy = Factor("baiy", ["qyxsc","ghivy","izkxr", "gutwm"])
cpcz = Factor("cpcz", ["roi","ntvfg", "rvn"])
xnh = Factor("xnh", ["zqbma","zlje", "mcvffd"])
qqvz = Factor("qqvz", ["jopqkj","hun", "oqua"])

### EXPERIMENT
constraints=[AtMostKInARow(2,(jxtk,"jqdtud")),AtLeastKInARow(3,(baiy,"gutwm")),ExactlyKInARow(3,(cpcz,"rvn"))]
design=[jxtk,baiy,cpcz,xnh,qqvz]
crossing=[xnh,qqvz]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_0"))
### END