from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VZL___Vj = Factor("VZL!$ Vj", [Level("TyczWs8", 1), Level("]or]k#p", 1), Level(")zHA)", 1), Level("6uVQ", 1), Level("HTYhhc", 1), Level("XekN|beDN", 1), Level("ZzeQLqLFBozjjF", 1), Level("ONf}Lot4", 1)])
RpRpPYMpS = Factor("RpRpPYMpS", [Level("Ecu", 1), Level("gilfzxyVLQ&I", 1), Level("L^yDtUn", 1), Level("jSpcW", 1), Level("a5_UWzvD", 1), Level("rcAzdoxEGV", 1), Level("YX!", 6), Level(" &rhUDiOF", 1)])
wOGTqUJVF = Factor("wOGTqUJVF", [Level("KHp)icMSJN", 1), Level("mdHbMEST[avr", 4), Level("bOzBry", 1), Level("le7jNn:}DS~Kf", 1), Level("fQX", 10), Level("B Vd", 1), Level("Jx<aDX", 6), Level("iWU@yXvE", 1), Level("mZ:sME", 6)])

design=[VZL___Vj,RpRpPYMpS,wOGTqUJVF]
crossing=[VZL___Vj,RpRpPYMpS,wOGTqUJVF]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_1"))

### END
