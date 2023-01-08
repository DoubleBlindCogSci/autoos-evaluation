from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cBEra = Factor("cBEra", ["uEQEp", "zngvOgjInkCCe", "TbrhwXKm:QrEsR"])
yX_wc = Factor("yX>wc", [Level("X|G(", 2), Level("XYf&f gEMX1", 1), Level("aZXs", 1), Level("jQKqc", 1)])

design=[cBEra,yX_wc]
crossing=[cBEra,yX_wc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
