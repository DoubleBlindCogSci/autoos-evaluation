from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fwy = Factor("fwy", ["biw", "qkz"])
suo = Factor("suo", ["gqv", "jkw"])
owvp = Factor("owvp", ["oyfnem", "tee"])
jyyovq = Factor("jyyovq", ["ghlvrq", "jko"])

### EXPERIMENT
design=[fwy,suo,owvp,jyyovq]
crossing=[[fwy,suo,owvp,jyyovq],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_3"))
### END