from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HkRppP_AZ = Factor("HkRppP#AZ", [Level("MhCRjDd^B", 6), Level("NaojDFgbY", 1), Level("f<jFIjM<T:infl", 1), Level(" vfv0b9eIBJ", 1), Level("y3yFXXOdqBN", 1), Level("UqNCR[U", 6), Level("<HK", 1)])

design=[HkRppP_AZ]
crossing=[HkRppP_AZ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_1"))

### END
