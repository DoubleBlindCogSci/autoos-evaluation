from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZxWJj4Jviln=Factor("JXOI",["BEpuBY",'N^SGXto|Cngvs',Level("I$mGyTQu",2),Level("jucV",10),Level("CYQENSCtLMWpHT",2),"b5X"])

### EXPERIMENT
design=[ZxWJj4Jviln]
crossing=[ZxWJj4Jviln]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_1"))
### END