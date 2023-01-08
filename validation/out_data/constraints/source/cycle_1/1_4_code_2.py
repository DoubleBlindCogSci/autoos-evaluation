from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vzonl = Factor("vzonl", ["xnbniq", "wae"])
rhl = Factor("rhl", ["xnwia", "rfyg"])
gzbitj = Factor("gzbitj", ["nft","ydo", "pzh"])


constraints = [ExactlyKInARow(3, (vzonl, "wae"))]
crossing = [rhl, gzbitj]

design=[vzonl,rhl,gzbitj]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_4"))

### END