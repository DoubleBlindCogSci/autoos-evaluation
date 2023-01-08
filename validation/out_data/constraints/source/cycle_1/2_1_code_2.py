from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
huw = Factor("huw", ["mch", "sag"])
mexbn = Factor("mexbn", ["npunj", "rezss"])
xwaee = Factor("xwaee", ["jqw", "kmdpc"])
hhclo = Factor("hhclo", ["glwyn","ivhtos","wtfv", "tpkfzl"])


constraints = [Exclude((huw, "sag")), AtMostKInARow(2, (mexbn, "rezss"))]
crossing = [xwaee, hhclo]

design=[huw,mexbn,xwaee,hhclo]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END