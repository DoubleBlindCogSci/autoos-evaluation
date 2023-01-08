from sweetpea import *
import os
_dir=os.path.dirname(__file__)
doyez = Factor("doyez", ["dkp", "haoio"])
vuul = Factor("vuul", ["ibh", "zlqt"])
utley = Factor("utley", ["wxtryf", "dpd"])
constraints = []
crossing = [doyez, vuul, utley]


design=[doyez,vuul,utley]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_2"))

### END