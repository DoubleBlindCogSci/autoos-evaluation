from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_O5ouG="Ih?EvdPw"
jaraH=Factor("P9wsDV|4ALK",["d umF","WebhKMB",_O5ouG,"bkzNVmobGno",Level("ZZ2DuB",3),Level("<Avw3cfdY",7),'(NWTBTwG'])

### EXPERIMENT
design=[jaraH]
crossing=[jaraH]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_0"))
### END