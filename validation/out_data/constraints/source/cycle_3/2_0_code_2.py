from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mnv = Factor("mnv", ["dlnfch","lku","fjcmr", "vyjo"])
fkt = Factor("fkt", ["jdpa", "etamjz"])
ttuvp = Factor("ttuvp", ["prk","ivfe","uwfj", "ggdx"])
cxo = Factor("cxo", ["edpxtg","swka", "vkjkbt"])


constraints = [AtMostKInARow(3, (mnv, "vyjo")), ExactlyK(2, (fkt, "etamjz"))]
crossing = [ttuvp, cxo]

design=[mnv,fkt,ttuvp,cxo]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END