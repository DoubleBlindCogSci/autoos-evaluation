from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wkxeux = Factor("wkxeux", ["fkfoz","ykppsa","ymh", "eizson"])
xiviu = Factor("xiviu", ["fycrk","uszp", "weaelw"])

### EXPERIMENT
constraints=[AtLeastKInARow(2,(wkxeux,"eizson"))]
design=[wkxeux,xiviu]
crossing=[xiviu]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_1"))
### END