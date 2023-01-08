from sweetpea import *
import os
_dir=os.path.dirname(__file__)
dfs = Factor("dfs", ["wjj", "psvjy"])
nctkh = Factor("nctkh", ["zmdkd", "ump"])
bwnmf = Factor("bwnmf", ["kxqz", "bbd"])
omlk = Factor("omlk", ["wqhkga", "axe"])
jtt = Factor("jtt", ["zubxad", "tilcb"])
cgwwdx = Factor("cgwwdx", ["guyzoj", "tbailw"])
uue = Factor("uue", ["wwgq", "epos"])
yjipe = Factor("yjipe", ["trldo", "lapfm"])
zzwjf = Factor("zzwjf", ["xigl", "iibs"])
qkf = Factor("qkf", ["wiucq", "rwgj"])
kmwsue = Factor("kmwsue", ["dgi", "deiu"])
tluxqs = Factor("tluxqs", ["pnrg", "ktzn"])
jxuc = Factor("jxuc", ["ggzan", "urid"])
constraints = []
crossing = [[dfs, nctkh], [bwnmf, omlk, jtt], [cgwwdx, uue, yjipe, zzwjf], [qkf, kmwsue, tluxqs, jxuc]]


design=[dfs,nctkh,bwnmf,omlk,jtt,cgwwdx,uue,yjipe,zzwjf,qkf,kmwsue,tluxqs,jxuc]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2"))

### END