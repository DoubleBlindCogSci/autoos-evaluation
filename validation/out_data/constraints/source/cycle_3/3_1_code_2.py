from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
obxlpa = Factor("obxlpa", ["bjfoxx","ufx", "epllfq"])
hkjtl = Factor("hkjtl", ["thrgc", "yyuqc"])
gehuio = Factor("gehuio", ["vbh","joiio","fagk", "drnsu"])
frky = Factor("frky", ["erglf","vpc", "sdcx"])
xyndjq = Factor("xyndjq", ["tiy","pvbm","zmz", "ielm"])
bsm = Factor("bsm", ["obik", "ergxu"])


constraints = [AtLeastK(3, (obxlpa, "epllfq")), ExactlyK(3, (hkjtl, "yyuqc")), Exclude((gehuio, "drnsu"))]
crossing = [frky, xyndjq, bsm]

design=[obxlpa,hkjtl,gehuio,frky,xyndjq,bsm]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END