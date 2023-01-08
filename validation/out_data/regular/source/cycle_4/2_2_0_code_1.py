from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Y6eNKic=Factor("TYMlTtvTpAn6",['A&eqHLdg','ubIxn#B'])
gaBb=['I<uQ','*BCeDY#mQzccC']
dhctTxXZr=Factor('hkRCuBJ7',gaBb)

### EXPERIMENT
design=[Y6eNKic,dhctTxXZr]
crossing=[Y6eNKic,dhctTxXZr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END