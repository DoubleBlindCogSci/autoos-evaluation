from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
hjben = Factor("hjben", ["nsfpc", "hln"])
skt = Factor("skt", ["kmx", "ddoug"])
urcbh = Factor("urcbh", ["nsfpc", "hln"])
ljh = Factor("ljh", ["kmx", "ddoug"])
constraints = []
crossing = [ljh, skt]

design=[hjben,skt,urcbh,ljh]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_0_0"))
