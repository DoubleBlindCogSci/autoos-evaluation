from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
phhw = Factor("phhw", ["ucxedj", "zyqzp"])
tvqit = Factor("tvqit", ["gkddvg", "mzd"])
wahay = Factor("wahay", ["ucxedj", "zyqzp"])
kam = Factor("kam", ["gkddvg", "mzd"])
lunun = Factor("lunun", ["abh", "gpjpwd"])
design=[phhw,tvqit,wahay,kam,lunun]
constraints=[]
crossing=[phhw,kam]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_0"))
