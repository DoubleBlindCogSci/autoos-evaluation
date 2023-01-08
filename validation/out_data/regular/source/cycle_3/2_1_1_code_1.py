from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HIRTGC=[Level('Qdn',9),'SO ]FKkH']
xaAqB567ZW=Factor('bdYlua',HIRTGC)

### EXPERIMENT
design=[xaAqB567ZW]
crossing=[xaAqB567ZW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END