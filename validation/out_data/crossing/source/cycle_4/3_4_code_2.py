from sweetpea import *
import os
_dir=os.path.dirname(__file__)
sgvqy = Factor("sgvqy", ["oip", "raxz"])
xub = Factor("xub", ["rfj", "rhe"])
pvdbmq = Factor("pvdbmq", ["wnrxj", "shts"])
esnsv = Factor("esnsv", ["orppvr", "buqf"])
clqan = Factor("clqan", ["nuqmm", "pil"])
exebt = Factor("exebt", ["eqneg", "vgki"])
ifb = Factor("ifb", ["umo", "acwki"])
hgsbr = Factor("hgsbr", ["kfur", "qnjqom"])
constraints = []
crossing = [[sgvqy, xub, pvdbmq], [esnsv, clqan, exebt, ifb], [hgsbr]]


design=[sgvqy,xub,pvdbmq,esnsv,clqan,exebt,ifb,hgsbr]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_4"))

### END