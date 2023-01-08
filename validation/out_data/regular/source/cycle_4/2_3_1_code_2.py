from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kj_bFlzzZxBUWN = Factor("kj8bFlzzZxBUWN", [Level(";Sn$P0(OjN&u7!", 1), Level("JngTJvF[Q<w", 2), Level("T$8z%QZiu7[", 1)])
_eKIIcWPARN_ = Factor("&eKIIcWPARN%", ["E&XhX}ucj;", "{trZJ(zWTu"])
iDRw = Factor("iDRw", ["aoLSwy_mvY0HAg", "MAQD[8hhm"])

design=[kj_bFlzzZxBUWN,_eKIIcWPARN_,iDRw]
crossing=[kj_bFlzzZxBUWN,_eKIIcWPARN_,iDRw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_1"))

### END
