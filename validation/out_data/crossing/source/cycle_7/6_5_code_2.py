from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hencr = Factor("hencr", ["nfjaif", "mwkwr"])
roz = Factor("roz", ["hjma", "wmnuyk"])
dmbpfx = Factor("dmbpfx", ["bgxvf", "lgt"])
angahx = Factor("angahx", ["sir", "oju"])
naq = Factor("naq", ["ytv", "oxvba"])
ugaj = Factor("ugaj", ["ewr", "klcacq"])
constraints = []
crossing = [hencr, roz, dmbpfx, angahx, naq, ugaj]


design=[hencr,roz,dmbpfx,angahx,naq,ugaj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_5"))

### END