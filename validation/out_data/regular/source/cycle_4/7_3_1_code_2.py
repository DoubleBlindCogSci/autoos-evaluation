from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ydAaf__dCAAz = Factor("ydAaf6#dCAAz", [Level("bS1FNxDg", 4), Level("t2Wd", 2), "dLwZ(YH", "j#7wTVQ", "OHh", "5mJmPVI", "YSsn;oH", ")lU)tFtt", "2Fgxhis%"])
et_V = Factor("et#V", ["GSxn}", "7Kg~%$WRzC", ")GMEvtmlLGd", "dCZUVRH", "kYuq", "EJSMu?v9a", "dB4"])
bmWCjFbSVw[ i] = Factor("bmWCjFbSVw[ i]", [Level("PslhR;&", 2), "GXUYg!<", "GRG a0", "H?tHHF", "ubwsNtUe1yTh", "zoHJ5ovOzW", "hvIEVubmJ7", "X b}U"])

design=[ydAaf__dCAAz,et_V]
crossing=[ydAaf__dCAAz,et_V]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_1"))

### END
