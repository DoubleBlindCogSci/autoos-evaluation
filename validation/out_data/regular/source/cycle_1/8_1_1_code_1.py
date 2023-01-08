from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MwfIuqaL5=Factor("mR#oSR",[Level('Qcux',3),'mtnbsZU','HTkhTRh>*GQn',Level('CAhqRP',6),'fpaeaYph[','b@FCjC',"M8xlMpWVkYW]B",Level("uv@Z*lKW>Sy",8)])

### EXPERIMENT
design=[MwfIuqaL5]
crossing=[MwfIuqaL5]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/8_1_1"))
### END