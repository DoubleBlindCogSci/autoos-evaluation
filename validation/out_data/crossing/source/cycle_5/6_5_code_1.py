from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hvee = Factor("hvee", ["xaq", "xqq"])
vktw = Factor("vktw", ["wedzy", "axdxh"])
zib = Factor("zib", ["pgy", "qegt"])
cwtvf = Factor("cwtvf", ["fikzxw", "hsrlo"])
gfti = Factor("gfti", ["ldvi", "dkg"])
pvqim = Factor("pvqim", ["zys", "eudc"])
czij = Factor("czij", ["qrzr", "mqlnbp"])
rzfw = Factor("rzfw", ["qhvs", "vrag"])
iaebrr = Factor("iaebrr", ["kvevqa", "romx"])
cprzzu = Factor("cprzzu", ["heehbt", "slxdjd"])
lcgs = Factor("lcgs", ["siykq", "bjkap"])
whlm = Factor("whlm", ["hymgil", "mxkvi"])
wedc = Factor("wedc", ["alnd", "bgzc"])
adp = Factor("adp", ["qel", "yaftk"])
xfj = Factor("xfj", ["hgw", "uiwyn"])
fog = Factor("fog", ["xbu", "axyhq"])
jxtxma = Factor("jxtxma", ["tnhlvi", "iwfx"])

### EXPERIMENT
design=[hvee,vktw,zib,cwtvf,gfti,pvqim,czij,rzfw,iaebrr,cprzzu,lcgs,whlm,wedc,adp,xfj,fog,jxtxma]
crossing=[[hvee,vktw,zib,cwtvf],[gfti,pvqim,czij,rzfw],[iaebrr,cprzzu,lcgs],[whlm,wedc,adp],[xfj,fog],[jxtxma],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_5"))
### END