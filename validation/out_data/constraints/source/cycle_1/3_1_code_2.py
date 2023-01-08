from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
crxpce = Factor("crxpce", ["achh", "hlnrh"])
bhxrvp = Factor("bhxrvp", ["yexbb","ccist", "vpejld"])
wgnnv = Factor("wgnnv", ["byh","rcxqaj","pnz", "ytrjy"])
flirem = Factor("flirem", ["ytfomo", "dhyhj"])
rgp = Factor("rgp", ["hlnzfs", "gylt"])


constraints = [ExactlyK(4, (crxpce, "hlnrh")), ExactlyK(2, (bhxrvp, "vpejld")), AtMostKInARow(2, (wgnnv, "ytrjy"))]
crossing = [flirem, rgp]

design=[crxpce,bhxrvp,wgnnv,flirem,rgp]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END