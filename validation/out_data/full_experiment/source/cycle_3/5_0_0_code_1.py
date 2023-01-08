from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
oil = Factor("oil", ["kcz", "ydgf"])
zrx = Factor("zrx", ["byouc", "qtcbz"])
zks = Factor("zks", ["kcz", "ydgf"])
ynz = Factor("ynz", ["byouc", "qtcbz"])
sweiz = Factor("sweiz", ["nljf", "stg"])
design=[oil,zrx,zks,ynz,sweiz]
constraints=[]
crossing=[zks,zrx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_0"))
