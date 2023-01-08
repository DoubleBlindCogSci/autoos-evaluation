from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tDd3cDyO=['oLXg1ht','1efKq8Up[Yi*s','p9d&M H']
VMqha3ci=Factor('ouOm',tDd3cDyO)

### EXPERIMENT
design=[VMqha3ci]
crossing=[VMqha3ci]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END