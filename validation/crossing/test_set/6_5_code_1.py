from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hencr = Factor("hencr", ["nfjaif", "mwkwr"])
roz = Factor("roz", ["hjma", "wmnuyk"])
dmbpfx = Factor("dmbpfx", ["bgxvf", "lgt"])
angahx = Factor("angahx", ["sir", "oju"])
naq = Factor("naq", ["ytv", "oxvba"])
ugaj = Factor("ugaj", ["ewr", "klcacq"])

### EXPERIMENT
design=[hencr,roz,dmbpfx,angahx,naq,ugaj]
crossing=[[hencr,roz,dmbpfx,angahx,naq,ugaj]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_5"))
### END