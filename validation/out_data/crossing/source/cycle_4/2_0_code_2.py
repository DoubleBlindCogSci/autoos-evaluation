from sweetpea import *
import os
_dir=os.path.dirname(__file__)
pfqbgl = Factor("pfqbgl", ["jjdrdd", "ihrd"])
zwpkf = Factor("zwpkf", ["wvo", "bput"])
kmidu = Factor("kmidu", ["gdcuv", "cestss"])
constraints = []
crossing = [[pfqbgl, zwpkf], [kmidu]]


design=[pfqbgl,zwpkf,kmidu]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END