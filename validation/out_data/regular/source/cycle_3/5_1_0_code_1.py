from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
YELFAOWyuY0=["hte^5etuv",'EROyZw$hUj',Level("mF]",8),'m~hSy','RcM#P']
Oh4B3=Factor("mUb5",YELFAOWyuY0)

### EXPERIMENT
design=[Oh4B3]
crossing=[Oh4B3]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_0"))
### END