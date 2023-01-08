from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
K22WD=Factor('oMYO}MLKoqNdZ',['oMhVhE',"h2pQyTw","Sfb>qHF","n6btJvN7Cx&ya"])

### EXPERIMENT
design=[K22WD]
crossing=[K22WD]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_1"))
### END