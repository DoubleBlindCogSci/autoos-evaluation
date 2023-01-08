from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wkxeux = Factor("wkxeux", ["fkfoz","ykppsa","ymh", "eizson"])
xiviu = Factor("xiviu", ["fycrk","uszp", "weaelw"])


constraints = [AtLeastKInARow(2, (wkxeux, "eizson"))]
crossing = [xiviu]

design=[wkxeux,xiviu]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_1"))

### END