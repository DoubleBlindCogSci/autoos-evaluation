from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pfqbgl = Factor("pfqbgl", ["jjdrdd", "ihrd"])
zwpkf = Factor("zwpkf", ["wvo", "bput"])
kmidu = Factor("kmidu", ["gdcuv", "cestss"])

### EXPERIMENT
design=[pfqbgl,zwpkf,kmidu]
crossing=[[pfqbgl,zwpkf],[kmidu],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_0"))
### END