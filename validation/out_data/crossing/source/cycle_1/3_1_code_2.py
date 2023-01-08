from sweetpea import *
import os
_dir=os.path.dirname(__file__)
tdaqb = Factor("tdaqb", ["reoeyq", "ookpdw"])
faxxc = Factor("faxxc", ["iuvvk", "ognzj"])
sglcyh = Factor("sglcyh", ["cpfgqu", "dgeuxo"])
scr = Factor("scr", ["osrf", "rjej"])
ttr = Factor("ttr", ["igczf", "wzbs"])
symi = Factor("symi", ["byclc", "elkhw"])
meuhum = Factor("meuhum", ["wpwcp", "zsmxnj"])
constraints = []
crossing = [[tdaqb, faxxc, sglcyh], [scr, ttr, symi, meuhum]]


design=[tdaqb,faxxc,sglcyh,scr,ttr,symi,meuhum]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END