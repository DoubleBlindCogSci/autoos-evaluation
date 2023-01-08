from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
lbb = Factor("lbb", ["yzmmfa", "arhbc"])
sndpyx = Factor("sndpyx", ["utxa", "raqlqp"])
dwbg = Factor("dwbg", ["yzmmfa", "arhbc"])
wrzorv = Factor("wrzorv", ["utxa", "raqlqp"])
luu = Factor("luu", ["gqiz", "qjv"])
design=[lbb,sndpyx,dwbg,wrzorv,luu]
constraints=[AtMostKInARow(3, luu)]
crossing=[wrzorv,luu]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_1"))
