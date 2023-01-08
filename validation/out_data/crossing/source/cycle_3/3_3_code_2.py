from sweetpea import *
import os
_dir=os.path.dirname(__file__)
picf = Factor("picf", ["uyji", "gmtsln"])
lewswm = Factor("lewswm", ["ajvrl", "eid"])
vynvl = Factor("vynvl", ["rgw", "xdzjqs"])
uuq = Factor("uuq", ["tgldwu", "avk"])
yxbicy = Factor("yxbicy", ["amhp", "gskkwy"])
ogizvb = Factor("ogizvb", ["clazw", "kwy"])
pnn = Factor("pnn", ["jrdbhn", "ttbn"])
xnl = Factor("xnl", ["ndz", "tyomqi"])
fbdrvy = Factor("fbdrvy", ["lvq", "twmfmc"])
constraints = []
crossing = [[picf, lewswm, vynvl], [uuq, yxbicy], [ogizvb, pnn, xnl, fbdrvy]]


design=[picf,lewswm,vynvl,uuq,yxbicy,ogizvb,pnn,xnl,fbdrvy]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3"))

### END