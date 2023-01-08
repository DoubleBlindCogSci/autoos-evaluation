from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qqfyue = Factor("qqfyue", ["odf", "jyegq"])
quqjp = Factor("quqjp", ["zxi", "tehreq"])
ttzzfo = Factor("ttzzfo", ["bwwr", "timqo"])
wjdpdv = Factor("wjdpdv", ["kgne", "yhq"])
ggae = Factor("ggae", ["loac", "vaejq"])
igrv = Factor("igrv", ["tqy", "zcbovm"])

### EXPERIMENT
design=[qqfyue,quqjp,ttzzfo,wjdpdv,ggae,igrv]
crossing=[[qqfyue,quqjp,ttzzfo,wjdpdv],[ggae,igrv],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_0"))
### END