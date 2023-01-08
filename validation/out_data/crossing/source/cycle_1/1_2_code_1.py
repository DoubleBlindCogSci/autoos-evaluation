from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fxxe = Factor("fxxe", ["sfmiza", "nfch"])

### EXPERIMENT
design=[fxxe]
crossing=[[fxxe],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END