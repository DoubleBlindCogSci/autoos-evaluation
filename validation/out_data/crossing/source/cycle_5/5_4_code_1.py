from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cgsctx = Factor("cgsctx", ["urxz", "tbnjy"])
vldij = Factor("vldij", ["kkj", "dadlvm"])
jqi = Factor("jqi", ["nzdde", "yovxbj"])
dzna = Factor("dzna", ["tbre", "xmw"])
pwc = Factor("pwc", ["jfy", "wip"])
zfd = Factor("zfd", ["kkr", "mob"])
bvwrxd = Factor("bvwrxd", ["qkthp", "qmwb"])
tuswt = Factor("tuswt", ["kkgj", "uxetk"])
kmly = Factor("kmly", ["udzl", "nkcde"])

### EXPERIMENT
design=[cgsctx,vldij,jqi,dzna,pwc,zfd,bvwrxd,tuswt,kmly]
crossing=[[cgsctx,vldij],[jqi,dzna,pwc],[zfd,bvwrxd],[tuswt],[kmly],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_4"))
### END