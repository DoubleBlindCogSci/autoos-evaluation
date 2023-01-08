from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vqsru = Factor("vqsru", ["ssgt","wtd", "kdz"])
szji = Factor("szji", ["odysml", "tpt"])
fkuqb = Factor("fkuqb", ["vujh","drmoi", "eecyv"])
bpzkjs = Factor("bpzkjs", ["bub","qvib", "yfi"])
lwaowf = Factor("lwaowf", ["svertx","ggncdo","piwo", "nnnnsy"])

### EXPERIMENT
constraints=[AtLeastKInARow(2,(vqsru,"kdz")),AtMostKInARow(2,(szji,"tpt"))]
design=[vqsru,szji,fkuqb,bpzkjs,lwaowf]
crossing=[fkuqb,bpzkjs,lwaowf]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3"))
### END