from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
doyez = Factor("doyez", ["dkp", "haoio"])
vuul = Factor("vuul", ["ibh", "zlqt"])
utley = Factor("utley", ["wxtryf", "dpd"])

### EXPERIMENT
design=[doyez,vuul,utley]
crossing=[[doyez,vuul,utley],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END