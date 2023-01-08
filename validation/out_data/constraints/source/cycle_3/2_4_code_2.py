from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
redwhu = Factor("redwhu", ["ublct","kcoq", "rdj"])
cip = Factor("cip", ["tor","iib", "uqegf"])
sryfuh = Factor("sryfuh", ["wdvbng","mjg", "wfsfhu"])


constraints = [AtMostKInARow(4, (redwhu, "rdj")), MinimumTrials(22)]
crossing = [sryfuh]

design=[redwhu,cip,sryfuh]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4"))

### END