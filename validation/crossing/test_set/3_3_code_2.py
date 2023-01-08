from sweetpea import *
import os
_dir=os.path.dirname(__file__)
itquc = Factor("itquc", ["xxcrf", "foipl"])
drmjp = Factor("drmjp", ["fuy", "rhcso"])
bkbrc = Factor("bkbrc", ["evihfm", "erk"])
constraints = []
crossing = [itquc, drmjp, bkbrc]


design=[itquc,drmjp,bkbrc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3"))

### END