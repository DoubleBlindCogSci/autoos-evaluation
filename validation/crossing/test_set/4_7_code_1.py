from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rgvugy = Factor("rgvugy", ["jpx", "xge"])
cauzu = Factor("cauzu", ["ehqe", "uucyu"])
wfd = Factor("wfd", ["dloqx", "orftw"])
mzlu = Factor("mzlu", ["ctspeq", "ngfso"])

### EXPERIMENT
design=[rgvugy,cauzu,wfd,mzlu]
crossing=[[rgvugy,cauzu,wfd,mzlu]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_7"))
### END