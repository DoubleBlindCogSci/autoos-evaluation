from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Vp_JpTcEPpTvQ_ = Factor("Vp>JpTcEPpTvQ6", [Level("Exbj", 4), Level("IaU", 1), Level("WS0", 4)])
sKXkOx = Factor("sKXkOx", [Level("PJvPW", 1), Level("us~!@xvF", 1), Level("I|?pdoQyWNXNO", 2)])

design=[Vp_JpTcEPpTvQ_,sKXkOx]
crossing=[Vp_JpTcEPpTvQ_,sKXkOx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
