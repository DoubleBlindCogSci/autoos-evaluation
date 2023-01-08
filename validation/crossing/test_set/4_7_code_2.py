from sweetpea import *
import os
_dir=os.path.dirname(__file__)
rgvugy = Factor("rgvugy", ["jpx", "xge"])
cauzu = Factor("cauzu", ["ehqe", "uucyu"])
wfd = Factor("wfd", ["dloqx", "orftw"])
mzlu = Factor("mzlu", ["ctspeq", "ngfso"])
constraints = []
crossing = [rgvugy, cauzu, wfd, mzlu]


design=[rgvugy,cauzu,wfd,mzlu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_7"))

### END