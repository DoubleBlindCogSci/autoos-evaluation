from sweetpea import *
import os
_dir=os.path.dirname(__file__)
fwy = Factor("fwy", ["biw", "qkz"])
suo = Factor("suo", ["gqv", "jkw"])
owvp = Factor("owvp", ["oyfnem", "tee"])
jyyovq = Factor("jyyovq", ["ghlvrq", "jko"])
constraints = []
crossing = [fwy, suo, owvp, jyyovq]


design=[fwy,suo,owvp,jyyovq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_3"))

### END