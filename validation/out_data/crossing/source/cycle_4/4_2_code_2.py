from sweetpea import *
import os
_dir=os.path.dirname(__file__)
afmp = Factor("afmp", ["edrd", "wab"])
sewxa = Factor("sewxa", ["bubh", "nqjdez"])
zcx = Factor("zcx", ["evnaod", "bbqdgk"])
yxmeu = Factor("yxmeu", ["vauho", "sooa"])
duq = Factor("duq", ["mfvb", "iame"])
eptlj = Factor("eptlj", ["faatr", "slsw"])
mkv = Factor("mkv", ["lyzca", "dnnvx"])
rjp = Factor("rjp", ["gou", "vat"])
constraints = []
crossing = [[afmp, sewxa], [zcx, yxmeu, duq, eptlj], [mkv], [rjp]]


design=[afmp,sewxa,zcx,yxmeu,duq,eptlj,mkv,rjp]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2"))

### END