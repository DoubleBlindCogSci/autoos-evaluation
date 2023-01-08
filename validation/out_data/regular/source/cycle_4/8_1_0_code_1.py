from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wTuS=Factor("zXOQ",["tHf<Fxy","CaQdo",'vrTWiae{','htf','yuWaJJe:O','UPddbk',"2Iincw",' dR(sP'])

### EXPERIMENT
design=[wTuS]
crossing=[wTuS]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_0"))
### END