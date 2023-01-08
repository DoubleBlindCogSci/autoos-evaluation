from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lmNbmTD=Factor("JKBPzBU",['U%FtEOSTpSwfjd','H~evAikoDEKVR',Level("ctredfO% CQ_",10),Level('X~SEnMhS',7),Level('icMpHODgz',8),"2UWYyW}(RJF#",Level("RwHxF?Ja",4),'Ke?lmHB2nnyNCT',"5xgSaZd>MXCxK"])

### EXPERIMENT
design=[lmNbmTD]
crossing=[lmNbmTD]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_1_1"))
### END