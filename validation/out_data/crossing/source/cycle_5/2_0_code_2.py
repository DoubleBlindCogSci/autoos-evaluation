from sweetpea import *
import os
_dir=os.path.dirname(__file__)
qqfyue = Factor("qqfyue", ["odf", "jyegq"])
quqjp = Factor("quqjp", ["zxi", "tehreq"])
ttzzfo = Factor("ttzzfo", ["bwwr", "timqo"])
wjdpdv = Factor("wjdpdv", ["kgne", "yhq"])
ggae = Factor("ggae", ["loac", "vaejq"])
igrv = Factor("igrv", ["tqy", "zcbovm"])
constraints = []
crossing = [[qqfyue, quqjp, ttzzfo, wjdpdv], [ggae, igrv]]


design=[qqfyue,quqjp,ttzzfo,wjdpdv,ggae,igrv]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END