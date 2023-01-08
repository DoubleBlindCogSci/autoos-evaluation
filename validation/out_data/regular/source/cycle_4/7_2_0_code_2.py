from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jHDCE = Factor("jHDCE", [Level("MfLUPxpGszDb", 4), "InST:kxae", "FtKxNdDtOn8dri", "KOyK", "InZ|", "dhNtFzbwjDM}O", "EvEKTf"])
LztfSJW_H_WQy = Factor("LztfSJW2H?WQy", [Level("XeaJh?K", 3), "(wvqjawd*mh", "ElzyZldi|FZyZ", "Cs@", "|_PKersD](jwpP", "kjgUIAlozFRoyt", ";laEhTQPABNh"])

design=[jHDCE,LztfSJW_H_WQy]
crossing=[jHDCE,LztfSJW_H_WQy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_0"))

### END
