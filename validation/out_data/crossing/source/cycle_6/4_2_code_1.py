from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vrmqfy = Factor("vrmqfy", ["fussar", "jsff"])
mwxic = Factor("mwxic", ["ovl", "mxwe"])
whnrth = Factor("whnrth", ["jtprjg", "qux"])
ghof = Factor("ghof", ["axgbh", "onptzf"])
talxq = Factor("talxq", ["nwji", "fllj"])
pif = Factor("pif", ["vnpxo", "jswoy"])
wuhtbc = Factor("wuhtbc", ["otv", "tay"])
efum = Factor("efum", ["vnbe", "uqyc"])
bnmyb = Factor("bnmyb", ["zuxxq", "rxbxbi"])
hwaio = Factor("hwaio", ["jtybi", "cmlp"])

### EXPERIMENT
design=[vrmqfy,mwxic,whnrth,ghof,talxq,pif,wuhtbc,efum,bnmyb,hwaio]
crossing=[[vrmqfy],[mwxic,whnrth,ghof],[talxq,pif,wuhtbc],[efum,bnmyb,hwaio],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2"))
### END