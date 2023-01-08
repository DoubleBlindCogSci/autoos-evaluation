from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vvn = Factor("vvn", ["lwji", "rsij"])
lvhgrl = Factor("lvhgrl", ["stnj", "jqv"])
cvevby = Factor("cvevby", ["lwji", "rsij"])
qyb = Factor("qyb", ["stnj", "jqv"])
mtmh = Factor("mtmh", ["uol", "ykzew"])
nocq = Factor("nocq", ["xuk", "djohfx"])
design=[vvn,lvhgrl,cvevby,qyb,mtmh,nocq]
constraints=[]
crossing=[qyb,lvhgrl]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_0_0"))
