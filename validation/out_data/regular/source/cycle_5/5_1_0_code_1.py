from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qKTKI7tO5l=Factor("EFHQ)k",[Level("oqeT|tJS<WSSEC",3),"oKrDKC",'BKfUXaJFxB|L','!y1GToHDk',"RBKNY)uvHVFAm"])

### EXPERIMENT
design=[qKTKI7tO5l]
crossing=[qKTKI7tO5l]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_0"))
### END