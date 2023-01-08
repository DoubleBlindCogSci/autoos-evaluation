from sweetpea import *
import os
_dir=os.path.dirname(__file__)
cchkx = Factor("cchkx", ["thqj", "leodpv"])
bltu = Factor("bltu", ["zjmq", "xlss"])
iji = Factor("iji", ["fpn", "putj"])
cdpwgx = Factor("cdpwgx", ["rji", "tlewtx"])
qkkivh = Factor("qkkivh", ["pemet", "tgcu"])
constraints = []
crossing = [cchkx, bltu, iji, cdpwgx, qkkivh]


design=[cchkx,bltu,iji,cdpwgx,qkkivh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_0"))

### END