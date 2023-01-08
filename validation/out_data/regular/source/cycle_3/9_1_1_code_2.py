from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JKBPzBU = Factor("JKBPzBU", [Level("U%FtEOSTpSwfjd", 1), Level("H~evAikoDEKVR", 1), Level("ctredfO% CQ_", 10), Level("X~SEnMhS", 7), Level("icMpHODgz", 8), Level("2UWYyW}(RJF#", 1), Level("RwHxF?Ja", 4), Level("Ke?lmHB2nnyNCT", 1), Level("5xgSaZd>MXCxK", 1)])

design=[JKBPzBU]
crossing=[JKBPzBU]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_1_1"))

### END
