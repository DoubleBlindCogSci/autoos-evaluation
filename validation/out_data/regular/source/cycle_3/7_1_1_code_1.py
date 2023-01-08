from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dhOffUy3nl5=[Level("MhCRjDd^B",6),'NaojDFgbY',"f<jFIjM<T:infl"," vfv0b9eIBJ","y3yFXXOdqBN",Level('UqNCR[U',6),'<HK']
BykfIP8d5GH=Factor("HkRppP#AZ",dhOffUy3nl5)

### EXPERIMENT
design=[BykfIP8d5GH]
crossing=[BykfIP8d5GH]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_1"))
### END