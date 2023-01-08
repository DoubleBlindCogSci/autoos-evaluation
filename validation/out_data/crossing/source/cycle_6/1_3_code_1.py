from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gqvtib = Factor("gqvtib", ["svwrfb", "qqg"])
cvtja = Factor("cvtja", ["dcsdm", "whgt"])
daifg = Factor("daifg", ["yso", "dfb"])

### EXPERIMENT
design=[gqvtib,cvtja,daifg]
crossing=[[gqvtib,cvtja,daifg],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_3"))
### END