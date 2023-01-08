from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cPWjdDvpD=Factor('ZwzVCkBnMqZTk',[Level("!Uu(qv",4),Level("?UJcu~qU",3),'QIU4@kj'])

### EXPERIMENT
design=[cPWjdDvpD]
crossing=[cPWjdDvpD]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END