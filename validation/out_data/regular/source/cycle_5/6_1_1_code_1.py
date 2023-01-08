from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Gn1yIt9=Factor("TJOpNGo)",["SbqF*Urr*f","UR@",'~AAJpmVvWE',"nvTlf_a",' <V',"vYwMJ"])

### EXPERIMENT
design=[Gn1yIt9]
crossing=[Gn1yIt9]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_1"))
### END