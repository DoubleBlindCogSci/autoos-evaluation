from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
rzvsr = Factor("rzvsr", ["yxgq", "kdlfys"])
rornu = Factor("rornu", ["hbiv", "hgctr"])
prcbkw = Factor("prcbkw", ["yxgq", "kdlfys"])
dgm = Factor("dgm", ["hbiv", "hgctr"])
twr = Factor("twr", ["tqrww", "pyezt"])
rcoee = Factor("rcoee", ["oepv", "hhe"])
constraints = []
crossing = [dgm, rzvsr]

design=[rzvsr,rornu,prcbkw,dgm,twr,rcoee]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_0_0"))
