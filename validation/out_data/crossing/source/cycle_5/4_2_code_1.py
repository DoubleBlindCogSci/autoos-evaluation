from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
apc = Factor("apc", ["rsh", "stbpj"])
oty = Factor("oty", ["gtihuv", "pbbq"])
lnks = Factor("lnks", ["xokq", "xww"])
llxhe = Factor("llxhe", ["qcdhca", "dcbbyj"])
ihdk = Factor("ihdk", ["hihj", "iqdq"])
pmewud = Factor("pmewud", ["pwhpfv", "ltcxjx"])
svxcxx = Factor("svxcxx", ["ludo", "tzfubv"])
zvn = Factor("zvn", ["vii", "foaf"])

### EXPERIMENT
design=[apc,oty,lnks,llxhe,ihdk,pmewud,svxcxx,zvn]
crossing=[[apc,oty],[lnks,llxhe],[ihdk,pmewud],[svxcxx,zvn],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2"))
### END