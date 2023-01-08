from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rwhjw = Factor("rwhjw", ["jzwjxn","debaxe","phhi", "vly"])
ahkd = Factor("ahkd", ["owywe","jvflih","cqzuy", "fbs"])
mxd = Factor("mxd", ["qvq","gwia","sbl", "htdi"])
cjy = Factor("cjy", ["wpxjy","secaih", "iffp"])


constraints = [AtMostKInARow(2, (rwhjw, "vly"))]
crossing = [ahkd, mxd, cjy]

design=[rwhjw,ahkd,mxd,cjy]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_3"))

### END