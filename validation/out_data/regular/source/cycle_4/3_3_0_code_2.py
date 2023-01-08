from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_pkr_EXiq = Factor(";pkr{EXiq", ["uhUXnEXCs8HyfK", "pvE!bQ>UONI6y", "AnkCSis)xOlIC"])
zdo = Factor("zdo", ["Urj1gZikPN", "MiU", "U~d@SfnHGS"])
mF_KSYGW = Factor("mF9KSYGW", ["KYAxQO", "Iry1Asyr; ;Gy", "DLJOkI"])

design=[_pkr_EXiq,zdo,mF_KSYGW]
crossing=[_pkr_EXiq,zdo,mF_KSYGW]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_0"))

### END
