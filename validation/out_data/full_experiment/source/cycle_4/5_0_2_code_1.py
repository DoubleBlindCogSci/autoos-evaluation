from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
muv = Factor("muv", ["hdbuig", "xtfto"])
xqnr = Factor("xqnr", ["razmc", "byv"])
rggn = Factor("rggn", ["hdbuig", "xtfto"])
xhstdg = Factor("xhstdg", ["razmc", "byv"])
vezedn = Factor("vezedn", ["osby", "tkvl"])
design=[muv,xqnr,rggn,xhstdg,vezedn]
constraints=[AtLeastKInARow(2, muv),ExactlyKInARow(4, rggn)]
crossing=[rggn,vezedn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_2"))
