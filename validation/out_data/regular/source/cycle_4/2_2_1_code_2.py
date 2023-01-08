from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HKaVPV = Factor("HKaVPV", ["eBdb", "xo&"])
bkCi_P = Factor("bkCi_P", [Level("q&wIDJIGEb", 1), Level("fTIAKbvgDKKRN|", 3)])

design=[HKaVPV,bkCi_P]
crossing=[HKaVPV,bkCi_P]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
