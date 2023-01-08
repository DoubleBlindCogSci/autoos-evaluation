from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
itquc = Factor("itquc", ["xxcrf", "foipl"])
drmjp = Factor("drmjp", ["fuy", "rhcso"])
bkbrc = Factor("bkbrc", ["evihfm", "erk"])

### EXPERIMENT
design=[itquc,drmjp,bkbrc]
crossing=[[itquc,drmjp,bkbrc]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3"))
### END