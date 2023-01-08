from sweetpea import *
import os
_dir=os.path.dirname(__file__)
rwkz = Factor("rwkz", ["vtddew", "rha"])
dhuwc = Factor("dhuwc", ["mklqzk", "zyquia"])
moadg = Factor("moadg", ["lpr", "cawkn"])
otjxz = Factor("otjxz", ["vlifgg", "lxpn"])
hqvz = Factor("hqvz", ["vlm", "lqjayy"])
zmrh = Factor("zmrh", ["zgd", "bppzyn"])
lwxlx = Factor("lwxlx", ["efkalb", "xjrbbf"])
cumsze = Factor("cumsze", ["emcjm", "jwyyg"])
pgsh = Factor("pgsh", ["wakkb", "bnl"])
yfmdz = Factor("yfmdz", ["rtm", "iophnl"])
azcv = Factor("azcv", ["iqnhr", "mlenr"])
sonr = Factor("sonr", ["axek", "gvhme"])
swg = Factor("swg", ["kxhb", "xoxaiz"])
constraints = []
crossing = [[rwkz, dhuwc, moadg], [otjxz, hqvz, zmrh, lwxlx], [cumsze, pgsh, yfmdz], [azcv, sonr, swg]]


design=[rwkz,dhuwc,moadg,otjxz,hqvz,zmrh,lwxlx,cumsze,pgsh,yfmdz,azcv,sonr,swg]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_0"))

### END