from sweetpea import *
import os
_dir=os.path.dirname(__file__)
bwmxt = Factor("bwmxt", ["gvt", "ghsy"])
smove = Factor("smove", ["abc", "tkc"])
jpbmg = Factor("jpbmg", ["gaq", "pkn"])
lkxfjb = Factor("lkxfjb", ["ndal", "swa"])
swyq = Factor("swyq", ["kucbjb", "axdka"])
eesrn = Factor("eesrn", ["iizue", "mmd"])
ypmivr = Factor("ypmivr", ["ejad", "jnle"])
zawqaf = Factor("zawqaf", ["knvfjl", "yjwu"])
erhcpb = Factor("erhcpb", ["ozjt", "phiwk"])
pdn = Factor("pdn", ["nwlbd", "xooiu"])
nyd = Factor("nyd", ["wcaujf", "bobgju"])
constraints = []
crossing = [[bwmxt, smove, jpbmg], [lkxfjb, swyq], [eesrn, ypmivr], [zawqaf, erhcpb, pdn, nyd]]


design=[bwmxt,smove,jpbmg,lkxfjb,swyq,eesrn,ypmivr,zawqaf,erhcpb,pdn,nyd]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_6"))

### END