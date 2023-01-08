from sweetpea import *
import os
_dir=os.path.dirname(__file__)
fxxe = Factor("fxxe", ["sfmiza", "nfch"])
constraints = []
crossing = [fxxe]


design=[fxxe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_2"))

### END