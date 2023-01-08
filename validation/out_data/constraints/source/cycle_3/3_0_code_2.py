from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tbyfg = Factor("tbyfg", ["ngiwi","kzz","nxzyuj", "mwlhwt"])
anytdq = Factor("anytdq", ["edyin","lwhk", "uvwcrg"])
bkshp = Factor("bkshp", ["meri","slcus", "ginhi"])
thpzr = Factor("thpzr", ["vhh", "nnju"])


constraints = [MinimumTrials(48), Exclude((anytdq, "uvwcrg")), AtMostKInARow(4, (tbyfg, "mwlhwt"))]
crossing = [thpzr]

design=[tbyfg,anytdq,bkshp,thpzr]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_0"))

### END