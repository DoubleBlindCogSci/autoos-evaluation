from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tiLl799pO=[Level("sxu9cN{pecKeH",8),Level('N< LEsp_Pb',9)]
c26tE=Factor('bU3QmWVBkTTKGI',tiLl799pO)

### EXPERIMENT
design=[c26tE]
crossing=[c26tE]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/2_1_1"))
### END