from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bvcz = Factor("bvcz", ["mqsq","tlefs", "mwcwko"])
mfp = Factor("mfp", ["aevk","hmq", "zfqow"])
stnz = Factor("stnz", ["yscyq", "sebkz"])


constraints = [MinimumTrials(24)]
crossing = [mfp, stnz]

design=[bvcz,mfp,stnz]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_0"))

### END