from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bTW3=[Level('lyOOD[0U>uxX',3),Level('QSOx9Ljaxj',10),'kSg']
XDOSB=Factor("UN _V[2fs",bTW3)
tTIywLzB=[Level('EpXmH',10),Level("JlQX9",5),Level('R1#V',8)]
hIBf3skp=Factor('F9Q>XrOfyoLdMm',tTIywLzB)

### EXPERIMENT
design=[XDOSB,hIBf3skp]
crossing=[XDOSB,hIBf3skp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END