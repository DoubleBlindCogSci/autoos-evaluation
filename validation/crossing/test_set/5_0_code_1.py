from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cchkx = Factor("cchkx", ["thqj", "leodpv"])
bltu = Factor("bltu", ["zjmq", "xlss"])
iji = Factor("iji", ["fpn", "putj"])
cdpwgx = Factor("cdpwgx", ["rji", "tlewtx"])
qkkivh = Factor("qkkivh", ["pemet", "tgcu"])

### EXPERIMENT
design=[cchkx,bltu,iji,cdpwgx,qkkivh]
crossing=[[cchkx,bltu,iji,cdpwgx,qkkivh]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0"))
### END