from sweetpea import *
import os
_dir=os.path.dirname(__file__)
gqvtib = Factor("gqvtib", ["svwrfb", "qqg"])
cvtja = Factor("cvtja", ["dcsdm", "whgt"])
daifg = Factor("daifg", ["yso", "dfb"])
constraints = []
crossing = [[gqvtib, cvtja, daifg],]


design=[gqvtib,cvtja,daifg]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_3"))

### END
