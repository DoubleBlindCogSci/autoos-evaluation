from sweetpea import *
import os
_dir=os.path.dirname(__file__)
izs = Factor("izs", ["ubcopp", "lkyv"])
hzgyu = Factor("hzgyu", ["mjt", "fsq"])
wozdzq = Factor("wozdzq", ["nxn", "wfqkyb"])
gfq = Factor("gfq", ["zdhgcp", "bgogqj"])
wmnza = Factor("wmnza", ["qpzh", "rpjvzm"])
nuvyka = Factor("nuvyka", ["cmfdmb", "cikeev"])
ezxzj = Factor("ezxzj", ["miimq", "oaaut"])
constraints = []
crossing = [[izs, hzgyu, wozdzq], [gfq, wmnza, nuvyka, ezxzj]]


design=[izs,hzgyu,wozdzq,gfq,wmnza,nuvyka,ezxzj]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END