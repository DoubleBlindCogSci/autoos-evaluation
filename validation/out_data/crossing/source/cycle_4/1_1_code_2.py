from sweetpea import *
import os
_dir=os.path.dirname(__file__)
zmddr = Factor("zmddr", ["mnr", "dypxw"])
njnu = Factor("njnu", ["lteb", "ibcbjo"])
constraints = []
crossing = [zmddr, njnu]


design=[zmddr,njnu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_1"))

### END